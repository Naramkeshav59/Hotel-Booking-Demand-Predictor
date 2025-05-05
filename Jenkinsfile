pipeline {
    agent any
    
    stages {
        stage('Cloning from github repo') {
            steps {
                script {
                    echo 'Cloning from github repo...'
                    docker.build("mlops")
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-github-token', url: 'https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor.git']])
                }
            }
        }
    }
}