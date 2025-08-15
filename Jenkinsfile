pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/jas09/PythonPlaywrightProject2.git'
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
