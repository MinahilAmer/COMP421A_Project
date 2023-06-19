pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'sonar-scanner -Dsonar.projectKey=project -Dsonar.analysis.mode=preview -Dsonar.report.export.path=sonar-report.json'
                        bat 'sonar-scanner -Dsonar.login=YOUR_SONAR_LOGIN_TOKEN -Dsonar.host.url=SONAR_SERVER_URL -Dsonar.projectKey=project -Dsonar.projectName="My Project" -Dsonar.projectVersion="1.0" -Dsonar.report.export.path=sonar-report.json -Dsonar.report.export.format=json'
                    }
                }
            }
        }

        stage('Snyk Security Scan') {
            steps {
                script {
                    bat 'npm install -g snyk'
                    bat 'snyk auth cf631823-b723-46a4-9f6e-1d423648fd56 -d'
                    bat 'snyk test --all-projects --json > snyk-report.json'
                    bat 'snyk test --all-projects --json > snyk-report.json && snyk monitor --all-projects --file=snyk-report.json'
                }
            }
        }

        stage('Python Code Execution') {
            steps {
                bat 'python project.py'
            }
        }
    }
}

