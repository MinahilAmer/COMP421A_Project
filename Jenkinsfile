pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'C:\\Users\\minah\\sonar-scanner-cli-4.8.0.2856-windows\\sonar-scanner-4.8.0.2856-windows\\bin\\sonar-scanner -Dsonar.projectKey=project'
                    }
                }
            }
        }

        stage('Snyk Security Scan') {
            steps {
                bat 'C:\\Users\\minah\\AppData\\Roaming\\npm\\snyk.cmd test --file="C:\\Users\\minah\\OneDrive\\Desktop\\Login page\\register.py"'
            }
        }
    }
}
