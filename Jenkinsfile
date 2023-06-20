pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                    bat 'pip install --upgrade pillow==9.2.0'
                }
            }
        }

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
                script {
                    bat 'C:\\Users\\minah\\AppData\\Roaming\\npm\\snyk.cmd test --all-projects'
                }
            }
        }
    }
}
