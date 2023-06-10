pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube Server') {
                    // Perform your static code analysis steps here
                    // Example: executing SonarScanner
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
