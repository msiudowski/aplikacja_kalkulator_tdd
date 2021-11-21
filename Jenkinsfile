pipeline {
    agent any
    parameters {
        gitParameter branchFilter: 'origin/(.*)', defaultValue: 'master', name: 'BRANCH', type: 'PT_BRANCH'
        choice(name: 'TEST_LEVEL', choices: ['smoke', 'regression', 'nightly'], description: '')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '$BRANCH']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/msiudowski/aplikacja_kalkulator_tdd/']]])
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
                    sh 'python3 -m pytest -m $TEST_LEVEL $WORKSPACE --html=report.html'
                }   
            }
        }
        stage('Archive artifacts') {
            steps {
                archiveArtifacts artifacts: 'report.html', followSymlinks: false
            }
        }
    }
}
