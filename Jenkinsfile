def gv
pipeline { 
    agent any

 tools {
    nodejs "Node"
}

    environment {
        BRANCH_NAME = 'jenkins_branch' 
        // DOCKER_CREDS = credentials("dockerhub_creds")  
    }

  parameters {
 string(name:'VERSION' , defaultValue: '' , description: 'this is my version')
 choice(name: 'VERSIONCHOICE' , choices : ['1.0.0','2.0.0','3.0.0'] ,  description : 'this is my version choices')
 booleanParam(name: 'executeTest' , defaultValue: true , description: 'this is my test will be true or false')
  }

    stages {
        stage('init') {
   steps {
    script {
        gv = load 'script.groovy'
    }
   }
        }
        stage('building') {
            when {
                expression {
                    env.BRANCH_NAME == "jenkins_branch"
                }
            }
            steps {
               script{
                gv.building()
               }
            }
        }

        stage('Test') {
            when{
                expression{
                    params.executeTest == true
                }
            }
            steps {
              script{
                gv.testing()
                echo "environmental variable from stage deply ${variable}"
              }
            }
        }

        stage('Deploy') {
            // input {
            //     message "select the deploy enviroment"
            //     ok "done"
            //     parameters{
            //          choice(name: 'ENV' , choices : ['dev','staging','producction'] ,  description : 'this is my enviroment choices')
            //     }
            // }
            steps {
              script{
                env.variable = input message: "select the deploy enviroment" ,  ok "done" ,  parameters{
                     choice(name: 'ENV' , choices : ['dev','staging','producction'] ,  description : 'this is my enviroment choices')
                }
                gv.deploying(variable)
                echo "${variable}"
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



//         stage('DOCKER LOGIN') {
          
//             steps {
//                 echo 'Building from main branch'
//                 // echo 'Login to docker with ${env.DOCKER_CREDS}'
// //              withCredentials([
// //     usernamePassword(
// //         credentialsId: 'dockerhub_creds',
// //         usernameVariable: 'USER',
// //         passwordVariable: 'PWD'
// //     )
// // ]) {
// //     sh 'echo "Username: $USER Password: $PWD"'
// // }
//             }
//         }
