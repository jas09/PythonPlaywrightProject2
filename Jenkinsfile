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
		stage('Setup'){
			steps {
				// Install pytest + Allure adapter
				bat 'pip install pytest allure-pytest'
			}
		}

        stage('Build & Test') {
            steps {
				// Run your tests and generate an HTML report under allure-report/
                bat 'pytest --alluredir=allure-report'
            }
        }

        stage('Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }
    }
}