pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '$BRANCh']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/msiudowski/aplikacja_kalkulator_tdd/']]])
            }
        }
        stage('Static analysis') {
            steps {
                script {
                    sh 'python3 -m flake8 $WORKSPACE'
                }
            }
        }
        stage('Unit tests') {
            steps {
                script {
                    sh 'python3 -m pytest -m $TEST_LEVEL $WORKSPACE'
                }   
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}