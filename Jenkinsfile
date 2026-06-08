@Library('jenkins_shared_library')
def gv
pipeline { 
    agent any

    stages {

        stage('init') {
         steps {
           script {
             gv = load 'script.groovy'
                  }
                }
                       }

        stage('build docker image') {
            steps {
               script{
                build()
                echo "building through SL"
               }
            }
        }
          stage('push docker image') {
            steps {
               script{
            push()
            echo "pushing through SL"
               }
            }
        }

        stage('Deploy') {
            steps {
              script{
              deploy()
              echo "deploying through SL"
              }
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
