pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                script {
                    parameters: [
                        choice(name: 'IMAGE_TAG', choices: getDockerImages(), description: 'Available Docker Images')]
                    sh 'ls -la'
                    sh 'python3 MyScript.py'
                    sh 'curl localhost:5000'
                   
                }
            }
        }
    }
}
