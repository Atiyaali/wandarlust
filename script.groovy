def build(){
    sh 'docker build -t atiyadocker/wandarlustfrontpipeline:latest ./frontend'
    sh 'docker build -t atiyadocker/wandarlustbackpipeline:latest ./backend'
}
def push(){
    sh 'docker push atiyadocker/wandarlustfrontpipeline:latest'
    sh 'docker push atiyadocker/wandarlustbackpipeline:latest'
}
return this