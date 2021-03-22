pipeline {
    agent any
    stages {
        stage('Spotbugs') {
            steps {
                sh "./gradlew spotbugsMain"
            }
        }

    }
}
