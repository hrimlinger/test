pipeline {
    agent any
    stages {
        stage('Clean'){
            cleanWs()
        }
        stage('hello') {
            steps {
                echo "Hello World"
                zip (
                    zipFile : "health_test_bbp_6.zip" ,
                    archive : false,
                    dir : "python_script",
                    glob: '**/*.*'
                )
                echo "zip ok"
            }
        }

    }
}
