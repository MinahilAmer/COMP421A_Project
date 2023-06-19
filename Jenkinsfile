pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'C:\\Users\\minah\\sonar-scanner-cli-4.8.0.2856-windows\\sonar-scanner-4.8.0.2856-windows\\binsonar-scanner -Dsonar.projectKey=project'
                    }
                }
            }
        }
    }
}

