# php --version
# node --version
# echo "hello this is atiya"
echo "building front image"
docker build -t atiyadocker/wandarlustfrontendjenkins:latest ./frontend
echo "building back image"
docker build -t atiyadocker/wandarlustbackendjenkins:latest ./backend
echo "done both"
echo  "loging"
docker login -u $USERNAME -p $PASSWORD
echo "pushing frontend image"
docker push atiyadocker/wandarlustfrontendjenkins:latest
echo "pushing backend image"
docker push atiyadocker/wandarlustbackendjenkins:latest