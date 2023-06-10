pipeline {
    agent any

    environment {
        nodePath = 'C:\\Program Files\\nodejs\\node.exe'
        npmPath = 'C:\\Program Files\\nodejs\\npm.cmd'
        snykScript = 'C:\\Program Files\\nodejs\\snyk.cmd'
    }

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    // Perform your static code analysis steps here
                    // Example: executing SonarScanner
                    bat 'C:\\Users\\minah\\sonar-scanner-cli-4.8.0.2856-windows\\sonar-scanner-4.8.0.2856-windows\\bin\\sonar-scanner -Dsonar.projectKey=project'
                }
            }
        }
        
        stage('Snyk Security Scan') {
            steps {
                bat "call ${snykScript} test"
            }
        }
    }
}
