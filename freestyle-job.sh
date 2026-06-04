# php --version
# node --version
# echo "hello this is atiya"
echo "building front image"
docker build -t wandarlustfrontendjenkins:latest ./frontend
echo "building back image"
docker build -t wandarlustbackendjenkins:latest ./backend
echo "done both"
