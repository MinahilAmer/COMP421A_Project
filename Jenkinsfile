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
                    bat 'snyk test'

                    // Check if vulnerabilities were found
                    def snykScanOutput = bat returnStdout: true, script: 'snyk test'
                    if (snykScanOutput.contains('found 0 issues')) {
                        echo 'No vulnerabilities found. Proceeding with the build.'
                        // Add your build steps here
                    } else {
                        echo 'Vulnerabilities found. Attempting to fix.'
                        
                        // Manually upgrade dependencies
                        bat 'pip install --upgrade numpy==1.22.2'
                        
                        // Rerun Snyk test
                        snykScanOutput = bat returnStdout: true, script: 'snyk test'
                        if (snykScanOutput.contains('found 0 issues')) {
                            echo 'Vulnerabilities fixed. Proceeding with the build.'
                            // Add your build steps here
                        } else {
                            echo 'Failed to fix vulnerabilities. Stopping the build.'
                            error('Fix the vulnerabilities before proceeding.')
                        }
                    }
                }
            }
        }
    }
}
