cd hello_world
docker build --tag hello_world .
docker run hello_world; echo $?
docker save -o hello_world.tar hello_world:latest
