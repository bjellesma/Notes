A containerization engine differs from a virtualization engine as a virtualization engine will divide up physical resources whereas a containerization
engine will divide up OS resources. For example, a hypervisor will run on bare metal and give the virtual machines chunks of the physical resources. Containerization
engines will give OS resources to each container so that each container will get its own root file system, etc.

![Containerization example](https://www.bbvaopenmind.com/wp-content/uploads/2015/10/BBVA-OpenMind-Ahmed-Banafa-cointenarization-4-1.jpg)

The **docker engine** consists of both the docker client and the docker daemon.

# First Docker Container

Run your first container with
```bash
docker run hello-world
```

You will see output similar to the following:

```bash
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
 ```

1. The docker client made an API call out to our docker daemon.
2. The docker daemon looked to see if it had a local copy of hello world image which it did not
3. Since the daemon didn't have this image locally, it went out do dockerhub  to pull the latest version of this image.*
4. The docker daemon creates a new container from that image
5. The image runs the executable that produces the above output
5. The daemon returns the output to the docker client, which interacts with your terminal. 

* You can configure docker to go to our registries such as an on premises registry.

We can verify that the container is no longer running:
```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

```
But we can see that the container was running at one time with
```bash
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
360da7ec65b4        hello-world         "/hello"            8 minutes ago       Exited (0) 8 minutes ago                       quizzical_liskov
```


And we can also see in info that we do have a container now but it's in the stopped state
```bash
$ docker info
Containers: 1
 Running: 0
 Paused: 0
 Stopped: 1
Images: 1
Server Version: 18.09.2
Storage Driver: overlay2
 Backing Filesystem: extfs
 Supports d_type: true
 Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 9754871865f7fe2f4e74d43e2fc7ccd237edcbce
runc version: 09c8266bf2fcf9519a651b04ae54c967b9ab86ec
init version: fec3683
Security Options:
 seccomp
  Profile: default
Kernel Version: 4.14.98-boot2docker
Operating System: Boot2Docker 18.09.2 (TCL 8.2.1)
OSType: linux
Architecture: x86_64
CPUs: 1
Total Memory: 989.4MiB
Name: default
ID: AGGD:7G3M:LIGS:V2RD:HYDG:7TKH:IFA3:H6GH:CLM2:VZTV:DZNG:EHCH
Docker Root Dir: /mnt/sda1/var/lib/docker
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
Labels:
 provider=virtualbox
Experimental: false
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false
```

We can also see extended info about the images

```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              fce289e99eb9        7 weeks ago         1.84kB

```

# Working with images

An **image** can be thought of as a stopped contianer whereas a **container** can be thought of as just a running image.

We can pull an image from dockerhub (or whichever repo that we specify with

```bash
$ sudo docker pull alpine
Using default tag: latest
latest: Pulling from library/alpine
6c40cc604d8e: Pull complete 
Digest: sha256:b3dbf31b77fd99d9c08f780ce6f5282aba076d70a513a8be859d8d3a4d0c92b8
Status: Downloaded newer image for alpine:latest
```
If we've been following along to this point, notice that we now have 2 images:
```bash
sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              caf27325b298        3 weeks ago         5.53MB
hello-world         latest              fce289e99eb9        7 weeks ago         1.84kB
```

Notice that dockerhub provides its own security assessment for all of its hosted containers:

![Docker Security](https://docs.docker.com/v17.12/docker-cloud/builds/images/scan-single.png)

We can remove the image that we just tagged with the following:

```bash
bjellz@bjellz-ubuntu:~$ sudo docker rmi alpine
Untagged: alpine:latest
Untagged: alpine@sha256:b3dbf31b77fd99d9c08f780ce6f5282aba076d70a513a8be859d8d3a4d0c92b8
Deleted: sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019
Deleted: sha256:503e53e365f34399c4d58d8f4e23c161106cfbce4400e3d0a0357967bad69390
bjellz@bjellz-ubuntu:~$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              fce289e99eb9        7 weeks ago         1.84kB
bjellz@bjellz-ubuntu:~$ 
```

# Container Lifecycle

You can run more advanced docker containters. The following will run a small web app.

```bash
bjellz@bjellz-ubuntu:~$ sudo docker run -d --name web -p 80:8080 nigelpoulton/pluralsight-docker-ci
[sudo] password for bjellz: 
Unable to find image 'nigelpoulton/pluralsight-docker-ci:latest' locally
latest: Pulling from nigelpoulton/pluralsight-docker-ci
a3ed95caeb02: Pull complete 
3b231ed5aa2f: Pull complete 
7e4f9cd54d46: Pull complete 
929432235e51: Pull complete 
6899ef41c594: Pull complete 
0b38fccd0dab: Pull complete 
Digest: sha256:7a6b0125fe7893e70dc63b2c42ad779e5866c6d2779ceb9b12a28e2c38bd8d3d
Status: Downloaded newer image for nigelpoulton/pluralsight-docker-ci:latest
14e15b2ffa321af4065154c0d71edcab72d0687bfeb1631e43a883ec6111b7d9
bjellz@bjellz-ubuntu:~$ 
```

To find the ip address for the container so that we can access this:

```bash
bjellz@bjellz-ubuntu:~$ ifconfig
docker0: BLAH

```

the `-d` tells docker to run in **detached mode** (in the background). `-p` tells docker to map port 80 of the host to port 8080 of the container. `--name` will allow you to specify a name for the containter.

You can also interact with the terminal of the container that you've created with **interactive mode**, `-it`. The following will create the latest version of ubuntu in a container and put the user at the bash.

```bash
sudo docker run -it ubuntu:latest /bin/bash
```
Keep in mind that containers are very lightweight and have no software packaged with them so even `ping` will render a `command not found`.

To stop all running containers:
```bash
docker stop $(docker ps -aq)
```
