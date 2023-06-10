stage('Static Code Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            // Configure SonarQube properties
            def scannerHome = tool 'SonarQubeScanner'
            withEnv(["SONAR_SCANNER_HOME=$scannerHome"]) {
                sh '${scannerHome}/bin/sonar-scanner'
            }
        }
    }
}
