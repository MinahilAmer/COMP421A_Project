pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'sonar-scanner -Dsonar.projectKey=project'
                    }
                }
            }
        }

        stage('Snyk Security Scan') {
            steps {
                withEnv(["PATH+NODEJS=${tool 'nodejs'}"]) {
                    bat 'snyk test'
                }
            }
        }
    }
}

