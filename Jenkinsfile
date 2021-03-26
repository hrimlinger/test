pipeline {
    agent any
    stages {
        stage('hello') {
            steps {
                echo "Hello World"
                zip (
                    zipFile : "health_test_bbp.zip" ,
                    archive : false,
                    dir : "python_script/*.*"
                )
                echo "zip ok"
                archiveArtifacts artifacts : "health_test_bbp.zip" , fingerprint : true
            }
        }

    }
}
