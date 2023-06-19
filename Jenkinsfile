pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MinahilAmer/COMP421A_Project.git'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

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
                    bat 'snyk test'
                }
            }
        }
    }
}
