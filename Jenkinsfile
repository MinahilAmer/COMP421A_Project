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
                snykSecurityScan()
            }
        }
    }
}

def snykSecurityScan() {
    withEnv(["PATH+NODEJS=${env.NODEJS_HOME}"]) {
        bat 'snyk test'
    }
}
