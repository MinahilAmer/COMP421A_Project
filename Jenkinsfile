pipeline {
    agent any

    stages {
        // ...

        stage('Snyk Security Scan') {
            steps {
                script {
                    // Install Snyk CLI
                    bat 'npm install -g snyk'

                    // Authenticate with Snyk (with debug flag)
                    bat 'snyk auth cf631823-b723-46a4-9f6e-1d423648fd56 -d'

                    // Perform Snyk security scan on Java project
                    bat 'snyk test --all-projects'
                }
            }
        }
    }
}
