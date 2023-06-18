pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        def scannerHome = tool 'sonar-scanner'
                        bat "${scannerHome}\\bin\\sonar-scanner -Dsonar.projectKey=project"
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

