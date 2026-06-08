@Library('jenkins_shared_library') _
pipeline { 
    agent any

    stages {

        // stage('init') {
        //  steps {
        //    script {
        //      gv = load 'script.groovy'
        //           }
        //         }
        //                }

        stage('build docker image') {
            steps {
               script{
                build ('atiyadocker/wandarlustfrontpipeline:latest' , 'atiyadocker/wandarlustbackpipeline:latest') 
                echo "building through SL"
               }
            }
        }
          stage('push docker image') {
            steps {
               script{
            push('atiyadocker/wandarlustfrontpipeline:latest' , 'atiyadocker/wandarlustbackpipeline:latest')
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
