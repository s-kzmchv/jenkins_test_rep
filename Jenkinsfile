pipeline {
    agent { docker {image 'skzmchv/jenkins_test_image:1.0'} }
    stages {
        stage('build') {
            steps {
		sh 'pip3 install numpy'
                sh 'python3 test.py'
            }
        }
    }
}
