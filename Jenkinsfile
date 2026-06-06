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
            withCredentials([
        usernamePassword(credentialsId: 'dockerhub_creds' , usernameVariable: USER , passwordVariable: PASSWORD )]){
            sh 'echo $PASSWORD | docker login -u $USER --password-stdin'
        }
               gv.push()
               }
            }
        }

        // stage('Deploy') {
        //     steps {
        //       script{
           
        //       }
        //     }
        // }
      
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
