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
                script {
                    bat 'npm install -g snyk'
                    bat 'snyk auth cf631823-b723-46a4-9f6e-1d423648fd56 -d'
                }
            }
        }

        stage('Python Code Execution') {
            steps {
                // Run the Python script
                bat 'python project.py'
            }
        }
    }
}
