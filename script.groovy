def build(){
    echo "building docker image"
    sh 'docker build -t atiyadocker/wandarlustfrontpipeline:latest ./frontend'
    sh 'docker build -t atiyadocker/wandarlustbackpipeline:latest ./backend'
}
def push(){
    echo "logging to docker hub"
    withCredentials([
        usernamePassword(credentialsId: 'dockerhub_creds' , usernameVariable: 'USER' , passwordVariable: 'PASSWORD' )]){
            sh 'echo $PASSWORD | docker login -u $USER --password-stdin'
        }
    docker "pushing to docker hub"
    sh 'docker push atiyadocker/wandarlustfrontpipeline:latest'
    sh 'docker push atiyadocker/wandarlustbackpipeline:latest'
}

def deploy(){
    echo "deploying"
}
return this