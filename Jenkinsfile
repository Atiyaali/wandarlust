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
                gv.build()
               }
            }
        }
          stage('push docker image') {
            steps {
               script{
               gv.push()
               }
            }
        }

        stage('Deploy') {
            steps {
              script{
               gv.deploy()
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
