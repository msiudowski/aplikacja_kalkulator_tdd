pipeline {
    agent any

    stages {
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
