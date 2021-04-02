# Run me from the top level directory with ./docker/docker_launch.sh, or just copy each command separately.
docker build -f ./docker/Dockerfile -t osr_ev:latest .

docker run -d --name osr_survey -p 5000:5000 osr_ev 