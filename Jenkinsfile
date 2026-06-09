// @Library('jenkins_shared_library') _
// library identifier: 'jenkins_SL_project@main' , retriever: modernSCM(
//     [$class: 'GitSCMSource',
//     remote:'https://github.com/Atiyaali/jenkins_shared_library.git',
//     credentialsId:'jenkins_github'

//     ]

// )
library(
    identifier: 'jenkins_SL_project@main',
    retriever: modernSCM(
        [$class: 'GitSCMSource',
         remote: 'https://github.com/Atiyaali/jenkins_shared_library.git',
         credentialsId: 'jenkins_github']
    )
)
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

                sh 'git fetch --tags'
                  def tag = sh(
                
                script: 'git describe --tags',
                returnStdout: true
            ).trim()
                build ("atiyadocker/wandarlustfrontpipeline:${tag}" , "atiyadocker/wandarlustbackpipeline:${tag}") 
                echo "building through SL"
               }
            }
        }
          stage('login and push image to docker') {
            steps {
            script{
                sh 'git fetch --tags'
                def tag = script.sh(
                sh 'git fetch --tags'
                script: 'git describe --tags',
                returnStdout: true
            ).trim()
            dockerlogin()
            push("atiyadocker/wandarlustfrontpipeline:${tag}" ,"atiyadocker/wandarlustbackpipeline:${tag}")
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
