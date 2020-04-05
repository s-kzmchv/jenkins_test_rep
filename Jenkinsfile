pipeline {
    agent { docker {image 'python:3.5.1'} }
    stages {
        stage('build') {
            steps {
		sh 'apt-get install -y python3-pip'
		sh 'pip3 install numpy'
                sh 'python3 test.py'
            }
        }
    }
}
