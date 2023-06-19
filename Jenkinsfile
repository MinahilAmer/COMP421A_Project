pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                // SonarQube analysis step
                // ...
            }
        }

        stage('Snyk Security Scan') {
            steps {
                bat 'C:\\Users\\minah\\AppData\\Roaming\\npm\\snyk test'
            }
        }
    }
}


