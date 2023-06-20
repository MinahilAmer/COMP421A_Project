pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install Pillow==8.3.1 mysql-connector-python==8.0.27'
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
                bat 'C:\\Users\\minah\\AppData\\Roaming\\npm\\snyk.cmd test --file="C:\\Users\\minah\\OneDrive\\Desktop\\Login page\\register.py"'
            }
        }
    }
}
