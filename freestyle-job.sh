# php --version
# node --version
# echo "hello this is atiya"
echo "building front image"
# docker build -t atiyadocker/wandarlustfrontendjenkins:latest ./frontend
docker build -t 127.0.0.1:8083/wandarlustfrontendjenkins:latest ./frontend
echo "building back image"
docker build -t 27.0.0.1:8083/wandarlustbackendjenkins:latest ./backend
echo "done both"
echo  "loging"
echo $PASSWORD | docker login -u $USERNAME --password-stdin 127.0.0.1:8083
echo "pushing frontend image"
docker push 127.0.0.1:8083/wandarlustfrontendjenkins:latest
echo "pushing backend image"
docker push 127.0.0.1:8083/wandarlustbackendjenkins:latest