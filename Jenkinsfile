pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fib-calculator"
        CONTAINER_NAME = "fib-runner"
    }

    stages {
        stage('Check Files') {
            steps {
                // This will show us if the file actually exists in the workspace
                bat "dir"
            }
        }

        stage('Docker Build') {
            steps {
                // Building the image
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Docker Run') {
            steps {
                script {
                    // Clean up old container and run new one
                    bat "docker rm -f %CONTAINER_NAME% 2>nul || exit 0"
                    bat "docker run --name %CONTAINER_NAME% %DOCKER_IMAGE%"
                }
            }
        }

        stage('Verify Output') {
            steps {
                script {
                    // Pull the result out of the container to the Jenkins workspace
                    bat "docker cp %CONTAINER_NAME%:/app/fibnocci_results.txt ."
                    bat "type fibnocci_results.txt"
                }
            }
        }
    }

    post {
        always {
            bat "docker rm -f %CONTAINER_NAME% 2>nul || exit 0"
        }
    }
}