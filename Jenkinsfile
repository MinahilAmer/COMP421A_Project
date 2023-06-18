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
                    bat 'pip install -r requirements.txt'  // Install project dependencies
                    bat 'snyk auth 4136a6ed-35c5-495c-b2e6-ce33b0e9c092'
                    bat 'snyk test'
                }
            }
        }
    }
}
