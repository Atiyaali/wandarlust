pipeline { 
    agent any

    environment {
        // Environment variables
        BRANCH_NAME = 'jenkins_branch'   
    }

    stages {

        stage('building') {
            when {
                expression {
                    env.BRANCH_NAME == "jenkins_branch"
                }
            }
            steps {
                echo 'buildind docker from jenkins branch'
                // git url: 'https://github.com/user/repo.git'
            }
        }

        stage('Build') {
            when {
                expression {
                    env.BRANCH_NAME == "main"
                }
            }
            steps {
                echo 'Building from main branch'
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

    post {
        always {
            echo 'Pipeline finished'
        }

        success {
            echo 'Pipeline succeeded'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}