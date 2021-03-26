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
            }
        }

    }
}
