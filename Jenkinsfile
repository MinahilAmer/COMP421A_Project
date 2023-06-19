pipeline {
    agent any

    stages {
        stage('Static Code Analysis') {
            steps {
                withSonarQubeEnv('jk1') {
                    script {
                        bat 'sonar-scanner -Dsonar.projectKey=project -Dsonar.report.export.path=sonar-report.json'
                        def sonarReport = readFile('sonar-report.json')
                        echo "SonarQube Analysis Report:\n${sonarReport}"
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
                    def snykReport = readFile('snyk-report.json')
                    echo "Snyk Security Scan Report:\n${snykReport}"
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

