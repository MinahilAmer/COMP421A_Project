pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    // Perform your static code analysis steps here
                    // Example: executing SonarScanner
                    bat 'sonar-scanner'
                }
            }
        }
    }
}
