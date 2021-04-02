# Docker

If you want to try out the Docker container, first install Docker on your computer. 
Then, after you launch the Docker Daemon (basically when you see the little whale on your taskbar),
cd to your repo on your machine and run

        ./docker/launch.sh

This will run the following two commands for you, which first build the image from the recipe in the dockerfile and then launch a new container from that image. Alternatively, you can just run these commands in a command prompt or terminal.

Building the image (-f points to the docker file, and -t gives the image a name):
        docker build -f ./docker/Dockerfile -t osr_ev:latest .

Launching the container:
        docker run -d --name osr_survey -p 5000:5000 osr_evaluation 

Either way you do this, open your browser and go to localhost:5000 and you'll see the web app running in the docker container.

Note: you can see the running container and its corresponding base image in the Docker Dashboard.

If you want to clean up the docker container and image, you can use the commands in `./docker/cleanup.sh` to delete the container and the image (or just run the script to do both instantly).