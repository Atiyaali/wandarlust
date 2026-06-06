def build(){
    docker build -t atiyadocker/wandarlustfrontpipeline:latest ./frontend
    docker build -t atiyadocker/wandarlustbackpipeline:latest ./backend
}
def push(){
    docker push atiyadocker/wandarlustfrontpipeline:latest
    docker push atiyadocker/wandarlustbackpipeline:latest
}