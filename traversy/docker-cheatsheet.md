# Docker Commands, Help & Tips (Updated by Bill for 2024 and originally made by [Brad Traversy](https://gist.github.com/bradtraversy/89fad226dc058a41b596d586022a9bd3) )

![image](https://github.com/bjellesma/Notes/assets/7660667/8269aa5e-6506-4100-a06f-59c51b882ca9)

#### TIP: ABOUT CONTAINERS

Docker containers are often compared to virtual machines but they are actually just processes running on your host os. In Windows/Mac, Docker runs in a mini-VM so to see the processes youll need to connect directly to that. On Linux however you can run "ps aux" and see the processes directly

### Show commands & management commands

```
$ sudo docker
```

### Docker version info

```
$ sudo docker version
```

### Show info like number of containers, etc

```
$ sudo docker info
```

# WORKING WITH CONTAINERS

### Create and run a container in foreground

it stands for interactice

```
$ sudo docker container run -it -p 8080:80 nginx
```

### Create an run a container in background

Here we use detached mode

```
$ sudo docker container run -d -p 8080:80 nginx
```


### Naming Containers

```
$ sudo docker container run -d -p 80:80 --name nginx-website nginx
```

### TIP: WHAT RUN DID

- Looked for image called nginx in image cache
- If not found in cache, it looks to the default image repo on Dockerhub
- Pulled it down (latest version), stored in the image cache
- Started it in a new container
- We specified to take port 80- on the host and forward to port 80 on the container
- We could do "$ docker container run --publish 8000:80 --detach nginx" to use port 8000
- We can specify versions like "nginx:1.09"

### List running containers (Note that these are only running conainers)

```
$ sudo docker container ls
```

OR

This is an older command but shorter and easier to remember

```
$ sudo docker ps
```

### List all containers (Even if not running)

```
$ sudo docker container ls -a
```

### Stop container

The DockerID can be found in the above docker process commands

```
$ sudo docker container stop [ID]
```

### Shorthand

```
$ sudo docker kill [ID]
```

### Stop all running containers

```
$ sudo docker stop $(docker ps -aq)
```

### Remove container (Can not remove running containers, must stop first)

```
$ sudo docker container rm [ID]
```

### To remove a running container use force(-f)

```
$ sudo docker container rm -f [ID]
```

### Remove all containers

```
$ sudo docker rm $(sudo docker ps -aq)
```

### Get logs (Use name or ID)

```
$ sudo docker container logs [NAME]
```

Example

```
$ sudo docker container logs nginx-website
```

### List processes running in container

```
$ sudo docker container top [NAME]
```

Example

```
$ sudo docker container top nginx-website
```

# IMAGE COMMANDS

You should first login to dockerhub by using the following command (assumes you've made a login on [DockerHub](https://hub.docker.com/)

```
$ sudo docker login
```

### List the images we have pulled

```
$ sudo docker image ls
```

### We can also just pull down images

```
$ sudo docker pull [IMAGE]
```

### Remove image

```
$ sudo docker image rm [IMAGE]
```

### Remove all images

```
$ sudo docker rmi $(sudo docker images -a -q)
```

#### TIP: ABOUT IMAGES

- Images are app bianaries and dependencies with meta data about the image data and how to run the image
- Images are not a complete OS. No kernel, kernel modules (drivers)
- Host provides the kernel, big difference between VM

## CONTAINER INFO

### View info on container

```
$ sudo docker container inspect [NAME]
```

Example

```
$ sudo docker container inspect nginx-website
```

### Specific property (--format)

```
$ sudo docker container inspect --format '{{ .NetworkSettings.IPAddress }}' [NAME]
```

### Performance stats (cpu, mem, network, disk, etc) (similar to ps -aux)

```
$ sudo docker container stats [NAME]
```

## ACCESSING CONTAINERS

### Create new nginx container and bash into

```
$ docker container run -it --name [NAME] nginx bash
```

## TIP

Use `exit` from within the CLI of a container

- i = interactive Keep STDIN open if not attached
- t = tty - Open prompt

**(no bash because ubuntu uses bash by default)**

### Use exec to enter the container from CLI

```
$ sudo docker container exec -it mysql bash
```

### Alpine is a very small Linux distro good for docker

```
$ sudo docker container run -it alpine sh
```

(use sh because it does not include bash)
(alpine uses apk for its package manager - can install bash if you want)

# NETWORKING

### Get port

```
$ sudo docker container port [NAME]
```

### List networks

```
$ sudo docker network ls
```

### Inspect network

```
$ sudo docker network inspect [NETWORK_NAME]
("bridge" is default)
```

### Create network

```
$ sudo docker network create [NETWORK_NAME]
```

### Create container on network

```
$ sudo docker container run -d --name [NAME] --network [NETWORK_NAME] nginx
```

### Connect existing container to network

```
$ sudo docker network connect [NETWORK_NAME] [CONTAINER_NAME]
```

### Disconnect container from network

```
$ sudo docker network disconnect [NETWORK_NAME] [CONTAINER_NAME]
```

### Detach network from container

```
$ sudo docker network disconnect
```

# IMAGE TAGGING & PUSHING TO DOCKERHUB

# tags are labels that point to an image ID

```
$ sudo docker image ls
```

Youll see that each image has a tag

### Retag existing image

- Note that nginx is the name of the image and we're retagging it with bjellesma/nginx
- This makes a copy of the image using your new tag.

```
$ sudo docker image tag nginx bjellesma/nginx-website
```

### DOCKERFILE PARTS

- FROM - The os used. Common is alpine, debian, ubuntu
- ENV - Environment variables
- RUN - Run commands/shell scripts, etc
- EXPOSE - Ports to expose
- CMD - Final command run when you launch a new container from image
- WORKDIR - Sets working directory (also could use 'RUN cd /some/path')
- COPY # Copies files from host to container

### Build image from dockerfile 

reponame should be in the form login/tag and this command expects to find a dockerfile in the current directory

```
$ sudo docker image build -t [REPONAME] .
```

### Upload to dockerhub

This will push the image with the tag bjellesma/nginx-website

```
$ sudo docker image push bjellesma/nginx-website
```

#### TIP: CACHE & ORDER

- If you re-run the build, it will be quick because everythging is cached.
- If you change one line and re-run, that line and everything after will not be cached
- Keep things that change the most toward the bottom of the Dockerfile

# EXTENDING DOCKERFILE

### Custom Dockerfile for html paqge with nginx

```
FROM nginx:latest # Extends nginx so everything included in that image is included here
WORKDIR /usr/share/nginx/html
COPY index.html index.html
```

### Build image from Dockerfile

```
$ sudo docker image build -t nginx-website .
```

### Running it

```
$ sudo docker container run -p 80:80 --rm nginx-website
```

# BIND MOUNTS

- Can not use in Dockerfile, specified at run time (uses -v as well)
- No files will be available in the directory but we should be able to override

```
$ sudo docker container run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html --name nginx-website nginx
```

### Go into the container and check

Image must be named

```
$ sudo docker container exec -it nginx-website bash
$ cd /usr/share/nginx/html
$ ls -al
```

# DOCKER COMPOSE

- Configure relationships between containers
- Save our docker container run settings in easy to read file
- 2 Parts: YAML File (docker.compose.yml) + CLI tool (docker-compose)

### 1. docker.compose.yml - Describes solutions for

- containers
- networks
- volumes

### 2. docker-compose CLI - used for local dev/test automation with YAML files

### Sample compose file (From Bret Fishers course)

```
services:
  jekyll:
    image: bretfisher/jekyll-serve
    volumes:
      - .:/site
    ports:
      - '80:4000'
```

### To run

```
$ sudo docker-compose up
```

### You can run in background with

```
$ sudo docker compose up -d
```

### To cleanup

This will remove the containers

```
$ sudo docker compose down
```
