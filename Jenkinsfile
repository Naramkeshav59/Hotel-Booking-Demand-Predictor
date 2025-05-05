pipeline {
    agent any

     environment {
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Cloning from github repo') {
            steps {
                script {
                    echo 'Cloning from github repo...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-github-token', url: 'https://github.com/Naramkeshav59/Hotel-Booking-Demand-Predictor.git']])
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Setup Virtual Environment
                    echo 'Setup Virtual Environment.........'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                    
                }
            }
        }

        stage('Linting Code') {
            steps {
                script {
                    // Linting Codedocker exec -u root -it jenkins-dind bash
                    echo 'Linting Code.........'
                    sh '''
                        set -e
                        . ${VENV_DIR}/bin/activate
                        pylint application.py main.py --output=pylint-report.txt --exit-zero || echo "Pylint stage completed"
                        flake8 application.py main.py --ignore=E501,E302 --output-file=flake8-report.txt || echo "Flake8 stage completed"
                        black application.py main.py || echo "Black stage completed"
                    '''
                    
                }
            }
        }


        stage('Trivy Scanning') {
            steps {
                script {
                    // Trivy Scanning
                    echo 'Trivy Scanning.........'
                    sh "trivy fs ./ --format table -o trivy-fs-report.html"
                }
            }
        }

    }
}