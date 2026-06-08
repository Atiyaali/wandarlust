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
               }
            }
        }
          stage('push docker image') {
            steps {
               script{
            push()
               }
            }
        }

        stage('Deploy') {
            steps {
              script{
              deploy()
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
