pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        sh 'sonar-scanner -Dsonar.projectKey=your_project_key'
                    }
                }
            }
        }

        stage('Snyk Security Scan') {
            steps {
                script {
                    sh 'npm install -g snyk'
                    sh 'snyk auth cf631823-b723-46a4-9f6e-1d423648fd56 -d'
                }
            }
        }

        stage('Python Code Execution') {
            steps {
                // Run the Python script in the background
                sh 'start /B python project.py'
            }
        }
    }
}
