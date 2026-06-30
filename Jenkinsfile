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

    environment {
        MONGODB_URI = "mongodb://mongo:27017/wanderlust"
        REDIS_URL   = "redis://redis:6379"
      
         }
    parameters {
    choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'production'], description: 'Environment')
}
    stages {

stage('get version'){
    steps{
    script{
    if (params.DEPLOY_ENV == "production" ){
        sh 'git fetch --tags'
        env.VERSION = sh( 
        script: 'git describe --tags',
        returnStdout: true
        ).trim()}
    else {
        env.VERSION  = env.BUILD_NUMBER
        }
        }
        }
    }
stage("install dependencies"){
parallel{
stage('Install Backend') {
  steps {
    dir('backend') {
      sh 'npm ci'
    }
  }
}
// stage('Install Frontend') {
//   steps {
//     dir('frontend') {
//       sh 'npm ci'
//     }
//   }
// }
        }
    }

stage("linting"){
parallel{
stage('Lint Backend') {
  steps {
    dir('backend') {
      sh 'npm run lint'
    }
  }
}
// stage('Lint Frontend') {
//     steps {
//         dir('frontend') {
//             sh 'npm run lint'
//         }
//     }
// }
}
}
// stage("testing"){
// parallel{
// stage('Test backend') {
//   steps {
//     dir('backend') {
//         sh 'npm test -- --detectOpenHandles --runInBand'
//     }
//     echo 'Backend TEST STAGE FINISHED'
//   }
// }
// stage('Test frontend') {
//   steps {
//     dir('frontend') {
//         sh 'npm test -- --detectOpenHandles --runInBand'
//     }
//     echo 'Frontend TEST STAGE FINISHED'
//   }
// }
//     }
// }
stage("build docker image"){
parallel{
stage('build front image') {    
    steps {
               script{
                // build ("atiyadocker/wandarlustfrontpipeline:${env.VERSION}","frontend/Dockerfile") 
                build ("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustfrontpipeline:${env.VERSION}","frontend/Dockerfile") 


               }
            }
}
stage('build back image') {    
    steps {
               script{
                build ("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustbackpipeline:${env.VERSION}","backend/Dockerfile") 
                // build ("atiyadocker/wandarlustbackpipeline:${env.VERSION}","backend/Dockerfile") 
               }
            }
}
stage('build nginx image') {    
    steps {
    script{
                build ("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustnginxpipeline:${env.VERSION}" ,"nginx/Dockerfile") 
                // build ("atiyadocker/wandarlustnginxpipeline:${env.VERSION}" ,"nginx/Dockerfile") 
               }
            }
}
    }
}


//  stage('Security Scan frontend image') {
//     steps {
//        script{
//         trivyscan("atiyadocker/wandarlustfrontpipeline:${env.VERSION}")
//           echo 'Frontend image scan completed successfully'
//        }

      
//     }
// }
// stage('Security Scan backend image') {
//     steps {
//       script{
//         trivyscan("atiyadocker/wandarlustbackpipeline:${env.VERSION}")
//           echo 'Backend image scan completed successfully'
//       }

      
//     }
// }
//  stage('Security Scan nginx image') {
//     steps {
//        script{
//         trivyscan("atiyadocker/wandarlustnginxpipeline:${env.VERSION}")
//         echo 'nginx image scan completed successfully'
//       }
        
//     }
// }

stage('login ') {
            steps {
            script{  
                
            dockerlogin()
         
            echo "pushing through SL"
                  }
            }
}
         
stage("push docker image"){
    parallel{
     stage("push back image"){
        steps{
script{
    //  push("atiyadocker/wandarlustbackpipeline:${env.VERSION}")
    pushcsr("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustbackpipeline:${env.VERSION}")
    
}
        }
     
     }   
stage("push front image"){
        steps{
            script{
//  push("atiyadocker/wandarlustfrontpipeline:${env.VERSION}")
 pushcsr("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustfrontpipeline:${env.VERSION}")
            }
        }
    
     } 
stage("push nginx image"){
        steps{
            script{
//   push("atiyadocker/wandarlustnginxpipeline:${env.VERSION}")
  pushcsr("590398356271.dkr.ecr.us-east-1.amazonaws.com/wandarlustnginxpipeline:${env.VERSION}")
            }
        }
   
     } 
    }
}

stage('Update ECS Task Definition') {
    steps {
        script {
            sh """
            sed -i 's#wandarlustfrontpipeline:[^"]*#wandarlustfrontpipeline:${BUILD_NUMBER}#' ecs/task.json

            sed -i 's#wandarlustbackpipeline:[^"]*#wandarlustbackpipeline:${BUILD_NUMBER}#' ecs/task.json
            """
        }
    }
}
// stage('Debug JSON') {
//     steps {
//         sh 'cat ecs/task.json'
//     }
// }
stage('Register Task Definition') {
    steps {
        script {
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'aws-creds']
            ]) {

                sh """
                aws ecs register-task-definition \
                --region us-east-1 \
                --cli-input-json file://ecs/task.json
                """
            }
        }
    }
}
stage('Deploy to ECS') {
    steps {
        script {
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'aws-creds']
            ]) {

                sh """
                aws ecs update-service \
                  --region us-east-1 \
                  --cluster wandarlust \
                  --service wandarlust-service-8jkwt2wa \
                  --task-definition wandarlust
                """
            }
        }
    }
}

stage('Production Approval') {
    when {
        expression { params.DEPLOY_ENV == "production" }
    }
    steps {
        input message: "Deploy to PRODUCTION?"
    }
}
stage('Deploy') {
    when {
        expression {
            params.DEPLOY_ENV == "production"
        }
    }
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