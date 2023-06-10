pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Server') {
                    // Perform your static code analysis steps here
                    // Example: executing SonarScanner
                    bat 'C:\\Users\\minah\\sonar-scanner-cli-4.8.0.2856-windows\\sonar-scanner-4.8.0.2856-windows\\bin\\sonar-scanner'
                }
            }
        }
    }
}

