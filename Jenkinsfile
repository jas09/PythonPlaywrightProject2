pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
				// specify branch and set correct credential id// specify branch and set correct credential id
				git branch: 'main',
					credentialsId: 'bed7e560-3801-49d8-836a-9f230934a63a',
					url: 'https://github.com/jas09/PythonPlaywrightProject2.git'
            }
        }

        stage('Build & Test') {
            steps {
                sh 'pytest tests/'  // or your Playwright/Robot Framework command
            }
        }

        stage('Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'index.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}