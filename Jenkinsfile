pipeline {
    agent any

     environment {
        VENV_DIR = 'venv'
        DOCKERHUB_CREDENTIAL_ID = 'mlops-dockerhub'
        DOCKERHUB_REGISTRY = 'https://registry.hub.docker.com'
        DOCKERHUB_REPOSITORY = 'keshav3654/hotel-booking-demand-predictor'
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

        stage('Building Docker Image') {
            steps {
                script {
                    // Building Docker Image
                    echo 'Building Docker Image........'
                    dockerImage = docker.build("${DOCKERHUB_REPOSITORY}:latest")
                }
            }
        }

          stage('Scanning Docker Image') {
            steps {
                script {
                    // Scanning Docker Image
                    echo 'Scanning Docker Image........'
                    sh "trivy image ${DOCKERHUB_REPOSITORY}:latest --format table -o trivy-image-scan-report.html"
                }
            }
        }

        stage('Pushing Docker Image') {
            steps {
                script {
                    // Pushing Docker Image
                    echo 'Pushing Docker Image........'
                    docker.withRegistry("${DOCKERHUB_REGISTRY}" , "${DOCKERHUB_CREDENTIAL_ID}"){
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('AWS Deployment') {
    environment {
        AWS_DEFAULT_REGION = 'us-east-1' // or your region
    }


    steps {
        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-cred']]) {
            script {
                echo 'AWS Deployment........'
                sh '''
                    aws ecs update-service --cluster mlops-ecs --service mlops_service --force-new-deployment
                '''
            }
        }
    }
}



        
    }
}