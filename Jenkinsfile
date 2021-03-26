pipeline {
    agent any
    stages {
        stage('hello') {
            steps {
                echo "Hello World"
                zip (
                    zipFile : "health_test_bbp_test_2.zip" ,
                    archive : false,
                    dir : "python_script",
                    glob: '**/*.*'
                )
                echo "zip ok"
                archiveArtifacts artifacts : "health_test_bbp_test_2.zip" , fingerprint : true
            }
        }

    }
}
