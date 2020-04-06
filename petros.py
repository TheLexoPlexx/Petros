import discord
import asyncio
import logging
import os
from discord.ext import commands

channels = {
    "rainbowsix_casual": [
        "467415318826975232",
        "467415365484412929",
        "471711656733573131"
        ],
    "rainbowsix_ranked": [
        "467657555640975372",
        "467657594996260874",
        "471712022791192588"
        ],
    "theforest": [
        "467415410598215683",
        "467658694310756352"
        ],
    "arma": [
        "467415502449278998",
        "467658957905723392",
        "470219773427580928",
        "470219997818388483",
        "470220108632162304"
        ],
    "pubg": [
        "467415439425798144",
        "467658376143306753",
        "470132175505850379"
        ],
    "fortnite": [
        "473827692601540618",
        "473827750332071947",
        "473827802571997184"
        ],
    "rocketleague": [
        "474573615439020032",
        "474575675886665739"
        ],
    "wow": [
        "478210241289388033",
        "478211296941309963"
        ]
}

def foo():
    return

async def setRead(next_channel, yesno):
    ow = discord.PermissionOverwrite()
    ow.read_messages = yesno
    await bot.edit_channel_permissions(next_channel, bot.get_server("467406309755715595").default_role, ow)


logging.basicConfig(level=logging.INFO)

TOKEN = os.environ['PETROS_TOKEN']
description = '''Supreme Commander Petros'''
bot = commands.Bot(command_prefix='/', description="31LB-Bot")
server = bot.get_server("467406309755715595")

@bot.event
async def on_ready():
    print('--------------------------------------------------------------')
    print('Logged in as ' + bot.user.name + ' [' + bot.user.id + ']')
    print('Running on: v' + discord.__version__)
    print('--------------------------------------------------------------')

#Print all Voice Channels with id
    for channel in bot.get_server("467406309755715595").channels:
        if channel.type == discord.ChannelType.voice:
            print(channel.id + " -> " + channel.name)

@bot.event
async def on_voice_state_update(before, after):
    if before.mute != after.mute:
        return
    if before.self_mute != after.self_mute:
        return
    if before.deaf != after.deaf:
        return
    if before.self_deaf != after.self_deaf:
        return
       
    after_channel = after.voice.voice_channel
    if after_channel is not None:
        category = "default_after"
        index_current = -1
        sel_list = []
        for key, value in channels.items():
            try:
                index_current = value.index(after_channel.id);
                category = key
                sel_list = value
            except ValueError:
                foo()

        if (index_current == -1):
            foo()
        else:
            openedchannel = False
            for channel in sel_list:
                if sel_list[index_current] != channel:
                    if len(bot.get_channel(channel).voice_members) == 0:
                        if channel != sel_list[0]:
                            await setRead(bot.get_channel(channel), True)
                            openedchannel = True
                            break
            if openedchannel == False:
                print("WARNING: " + category + " is full!")

    before_channel = before.voice.voice_channel
    if before_channel is not None:
        category = "default_before"
        index_current = -1
        sel_list = []
        for key, value in channels.items():
            try:
                index_current = value.index(before_channel.id);
                category = key
                sel_list = value
            except ValueError:
                foo()
                
        if (index_current == -1):
            foo()
        else:            
            if before_channel.id != sel_list[0]:
                if len(before_channel.voice_members) == 0:
                    await setRead(before_channel, False)

            if before_channel.id == sel_list[0]:
                next_channel = bot.get_channel(sel_list[1])
                if len(next_channel.voice_members) == 0:
                    await setRead(next_channel, False)
                
@bot.command()
async def hello():
    '''test'''
    await bot.say('Hallo :)')

bot.run(TOKEN)
