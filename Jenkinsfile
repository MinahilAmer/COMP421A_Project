pipeline {
    agent any

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
                // Define the path to the Node.js executable (node.exe)
                def nodePath = "C:\\Program Files\\nodejs\\node.exe"

                // Run the Snyk security scan command
                bat "\"${nodePath}\" C:\\Users\\minah\\AppData\\Roaming\\npm\\snyk.cmd test"
            }
        }
    }
}
