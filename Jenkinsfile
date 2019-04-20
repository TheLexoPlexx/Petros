#!groovy
node {
    stage("Clone repo") 
        def commitHash = checkout(scm).GIT_COMMIT
    

    stage("Build image")
        app = docker.build("petros/petros")

    stage('Push image') 
        docker.withRegistry(DOCKER_REGISTRY_URI, '') {
            echo BRANCH_NAME
            if (BRANCH_NAME == "master") {
                app.push('latest');
            }
            app.push(BRANCH_NAME);
            app.push(commitHash);
        }
}