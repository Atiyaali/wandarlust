pipeline { 
    agent any
 tools {
    nodejs "Node"
}
    environment {
        // Environment variables
        BRANCH_NAME = 'jenkins_branch' 
        // DOCKER_CREDS = credentials("dockerhub_creds")  
    }
  parameters {
 string(name:'VERSION' , defaultValue: '' , description: 'this is my version')
 choice(name: 'VERSIONCHOICE' , choices : ['1.0.0','2.0.0','3.0.0'] ,  description : 'this is my version choices')
 booleanParam(name: 'executeTest' , defaultValue: true , description: 'this is my test will be true or false')
  }
    stages {

        stage('building') {
            when {
                expression {
                    env.BRANCH_NAME == "jenkins_branch"
                }
            }
            steps {
                echo 'buildind docker from jenkins branch'
                // git url: 'https://github.com/user/repo.git'
            }
        }

        stage('DOCKER LOGIN') {
          
            steps {
                echo 'Building from main branch'
                // echo 'Login to docker with ${env.DOCKER_CREDS}'
//              withCredentials([
//     usernamePassword(
//         credentialsId: 'dockerhub_creds',
//         usernameVariable: 'USER',
//         passwordVariable: 'PWD'
//     )
// ]) {
//     sh 'echo "Username: $USER Password: $PWD"'
// }
            }
        }

        stage('Test') {
            when{
                expression{
                    params.executeTest == true
                }
            }
            steps {
                echo 'Running tests...'
                echo 'running test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo "this is my params for choices ${params.VERSIONCHOICE}"
             
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