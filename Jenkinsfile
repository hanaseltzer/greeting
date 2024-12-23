pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials('025670723498')
        AWS_SECRET_ACCESS_KEY = credentials('025670723498') 
    }
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
