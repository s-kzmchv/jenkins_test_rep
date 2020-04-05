pipeline {
    agent { docker {image 'python:slim'} }
    stages {
        stage('build') {
            steps {
		sh 'pip3 install numpy'
                sh 'python3 test.py'
            }
        }
    }
}
