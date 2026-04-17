pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fib-calculator"
        CONTAINER_NAME = "fib-runner"
    }

    stages {
        stage('Docker Build') {
            steps {
                // Build the image from the Dockerfile in the root
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Docker Run') {
            steps {
                script {
                    // Remove old container if it exists
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    
                    // Run the container and give it a specific name
                    sh "docker run --name ${CONTAINER_NAME} ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Verify Output') {
            steps {
                script {
                    echo "Reading the Fibonacci results from inside the container:"
                    // Copy the result file from the container to the Jenkins workspace to view it
                    sh "docker cp ${CONTAINER_NAME}:/app/fibonacci_results.txt ."
                    sh "cat fibonacci_results.txt"
                }
            }
        }
    }

    post {
        always {
            // Clean up the container
            sh "docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}