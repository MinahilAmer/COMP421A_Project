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
                    bat 'snyk auth cf631823-b723-46a4-9f6e-1d423648fd56'
                    def snykScanOutput = bat returnStdout: true, script: 'snyk test'
                    if (snykScanOutput.contains('found 0 issues')) {
                        echo 'No vulnerabilities found. Proceeding with the build.'
                        // Add your build steps here
                    } else {
                        echo 'Vulnerabilities found. Stopping the build.'
                        error('Fix the vulnerabilities before proceeding.')
                    }
                }
            }
        }
    }
}
