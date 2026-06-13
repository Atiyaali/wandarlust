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
        DEPLOY_ENV = 'staging'    }
    stages {

stage('get version'){
    steps{
    script{
    if (env.DEPLOY_ENV == "production" ){
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
stage("testing"){
parallel{
stage('Test backend') {
  steps {
    dir('backend') {
        sh 'npm test -- --detectOpenHandles --runInBand'
    }
    echo 'Backend TEST STAGE FINISHED'
  }
}
// stage('Test frontend') {
//   steps {
//     dir('frontend') {
//         sh 'npm test -- --detectOpenHandles --runInBand'
//     }
//     echo 'Frontend TEST STAGE FINISHED'
//   }
// }
    }
}
stage("build docker image"){
parallel{
stage('build front image') {    
    steps {
               script{
                buildfront ("atiyadocker/wandarlustfrontpipeline:${env.VERSION}","/frontend/Dockerfile") 
               }
            }
}
stage('build back image') {    
    steps {
               script{
                buildback ("atiyadocker/wandarlustbackpipeline:${env.VERSION}","/backend/Dockerfile") 
               }
            }
}
stage('build nginx image') {    
    steps {
    script{
                buildnginx ("atiyadocker/wandarlustnginxpipeline:${env.VERSION}" ,"/nginx/Dockerfile") 
               }
            }
}
    }
}

stage("security scan"){
parallel{
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
stage('Security Scan backend image') {
    steps {
        sh """
        docker run --rm \
          -v /var/run/docker.sock:/var/run/docker.sock \
          aquasec/trivy:latest image \
          atiyadocker/wandarlustbackpipeline:${env.VERSION}
        """

        echo 'Backend image scan completed successfully'
    }
}
 stage('Security Scan nginx image') {
    steps {
        sh """
        docker run --rm \
          -v /var/run/docker.sock:/var/run/docker.sock \
          aquasec/trivy:latest image \
          atiyadocker/wandarlustnginxpipeline:${env.VERSION}
        """

        echo 'nginx image scan completed successfully'
    }
}
    }
}
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
      backendpush("atiyadocker/wandarlustbackpipeline:${env.VERSION}")
     }   
      stage("push front image"){
     frontendpush("atiyadocker/wandarlustfrontpipeline:${env.VERSION}")
     } 
       stage("push nginx image"){
      nginxpush("atiyadocker/wandarlustnginxpipeline:${env.VERSION}")
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