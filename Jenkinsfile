pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'docker build hello -t 025670723498.dkr.ecr.us-east-1.amazonaws.com/hanna-demo/hello:%BUILD_ID%'
            }
        }
        stage('Push') {
            steps {
                bat 'docker push 025670723498.dkr.ecr.us-east-1.amazonaws.com/hanna-demo/hello:%BUILD_ID%'
            }
        }
    }
}
