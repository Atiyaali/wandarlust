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
    // agent {
    //     docker {
    //         image 'node:18'
    //     }
    // }

      environment {
    MONGODB_URI = "mongodb://mongo:27017/wanderlust"
        REDIS_URL   = "redis://redis:6379"
        BRANCH_NAME = 'jenkins_branch' 
        DEPLOY_ENV = 'staging'
        // DOCKER_CREDS = credentials("dockerhub_creds")  
    }
    stages {

        // stage('init') {
        //  steps {
        //    script {
        //      gv = load 'script.groovy'
        //           }
        //         }
        //                }

        stage('get version'){
            steps{
                script{
                    if (env.DEPLOY_ENV == "production" ){
                        sh 'git fetch --tags'
                env.VERSION = sh( 
                script: 'git describe --tags',
                returnStdout: true
            ).trim()
                        
                    }
                    else {
                        env.VERSION  = env.BUILD_NUMBER
                    }
                }
            }
    }
    stage('Install Backend') {
  steps {
    dir('backend') {
      sh 'npm ci'
    }
  }
}

stage('Lint Backend') {
  steps {
    dir('backend') {
      sh 'npm run lint'
    }
  }
}


// stage('Test') {
//   steps {
//    script{
//     testback()
//    }
//   }
// }
stage('Test') {
  steps {
    dir('backend') {
     sh 'jest --runInBand --detectOpenHandles --forceExit'
    }
        echo 'TEST STAGE FINISHED'
  }
}


// stage('Lint Frontend') {
//     steps {
//         dir('frontend') {
//             sh 'npm install'
//             sh 'npm run lint'
//         }
//     }
// }
// stage('Debug Docker') {
//   steps {
//     sh 'whoami'
//     sh 'echo $PATH'
//     sh 'which docker || true'
//     sh 'docker -v'
//   }
// }

        stage('build docker image ') {
           
            steps {
               script{
               
                build ("atiyadocker/wandarlustfrontpipeline:${env.VERSION}" , "atiyadocker/wandarlustbackpipeline:${env.VERSION}") 
                echo "building through SL"
               }
            }
        }
stage('Security Scan frontend image') {
    steps {
        sh """
        docker run --rm \
          -v /var/run/docker.sock:/var/run/docker.sock \
          aquasec/trivy:latest image \
          atiyadocker/wandarlustfrontpipeline:${env.VERSION}
        """

        echo 'Frontend image scan completed successfully'
    }
}
// stage('Security Scan backend image') {
//     steps {
//         sh """
//         docker run --rm \
//           -v /var/run/docker.sock:/var/run/docker.sock \
//           aquasec/trivy:latest image \
//           atiyadocker/wandarlustbackpipeline:${env.VERSION}
//         """

//         echo 'Backend image scan completed successfully'
//     }
// }

          stage('login and push image to docker ') {
           
            steps {
            script{
               
            dockerlogin()
            push("atiyadocker/wandarlustfrontpipeline:${env.VERSION}" ,"atiyadocker/wandarlustbackpipeline:${env.VERSION}")
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