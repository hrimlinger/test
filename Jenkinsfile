pipeline {
    agent any
    tools {
        jdk 'JDK 1.7'
    } 
    stages {
        stage('Spotbugs') {
            steps {
                sh "./gradlew spotbugsMain"
            }
        }

    }
}
