pipeline { 
    agent any

    environment {
        // Environment variables
        APP_NAME = "my-app"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                // git url: 'https://github.com/user/repo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                // sh 'npm install'
                // sh 'mvn package'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // sh 'npm test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // sh 'docker compose up -d'
            }
        }
    }

  
}