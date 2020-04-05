pipeline {
    agent { docker {image 'python:3.8.2-alpine3.10'} }
    stages {
        stage('build') {
            steps {
		sh 'pip3 install numpy'
                sh 'python3 test.py'
            }
        }
    }
}
