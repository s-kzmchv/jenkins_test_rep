pipeline {
    agent { docker {image 'skzmchv/jenkins_test_image:1.0'} }
    stages {
        stage('build') {
            steps {
                sh 'python3 app.py compare'
            }
        }
	stage('Test') {
	    steps {
		sh 'robot test.robot'
	    }
	}
    }
}
