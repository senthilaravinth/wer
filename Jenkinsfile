pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fib-calculator"
        CONTAINER_NAME = "fib-runner"
    }

    stages {
        stage('Docker Build') {
            steps {
                // Use 'bat' instead of 'sh' for Windows
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Docker Run') {
            steps {
                script {
                    // Windows batch syntax for ignoring errors if container doesn't exist
                    bat "docker rm -f %CONTAINER_NAME% 2>nul || exit 0"
                    bat "docker run --name %CONTAINER_NAME% %DOCKER_IMAGE%"
                }
            }
        }

        stage('Verify Output') {
            steps {
                script {
                    echo "Reading the Fibonacci results:"
                    // Copy file from container to current workspace
                    bat "docker cp %CONTAINER_NAME%:/app/fibonacci_results.txt ."
                    // 'type' is the Windows equivalent of 'cat'
                    bat "type fibonacci_results.txt"
                }
            }
        }
    }

    post {
        always {
            // Clean up using Windows batch
            bat "docker rm -f %CONTAINER_NAME% 2>nul || exit 0"
        }
    }
}