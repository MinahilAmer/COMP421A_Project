pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'sonar-scanner -Dsonar.projectKey=project -Dsonar.host.url=http://localhost:9000/projects -Dsonar.login=4d5576dd4b0599819c31248cbd0707f152aae8b1'
                        echo "SonarQube Analysis Report:"
                        def sonarReport = readFile('.scannerwork/report-task.txt')
                        echo sonarReport
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
                    echo "Snyk Security Scan Report:"
                    def snykReport = readFile('snyk-report.json')
                    echo snykReport
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
