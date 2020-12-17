pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                script {
                    sh 'ls -la'
                    sh 'python3 MyScript.py'
                    sh 'curl localhost:5000'
                   
                }
            }
        }
    }
}
