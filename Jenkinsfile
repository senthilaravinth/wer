pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fib-calculator"
        CONTAINER_NAME = "fib-runner"
    }

    stages {
        stage('Docker Build') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Docker Run') {
            steps {
                script {
                    bat "docker rm -f %CONTAINER_NAME% 2>nul || exit 0"
                    bat "docker run --name %CONTAINER_NAME% %DOCKER_IMAGE%"
                }
            }
        }

        stage('Verify Output') {
            steps {
                script {
                    echo "Copying results from container..."
                    // We are now looking for results.txt as defined in the Python script
                    bat "docker cp %CONTAINER_NAME%:/app/results.txt ."
                    bat "type results.txt"
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