pipeline {
    agent any
    stages {
        stage('hello') {
            steps {
                echo "Hello World"
                zip (
                    zipFile : "health_test_bbp.zip" ,7
                    archive : false,
                    dir : "python_script/*.*"
                )
            }
        }

    }
}
