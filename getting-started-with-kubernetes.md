Kubernetes is an open source project by Google and is often shortened to **K8s** (the 8 stands for the 8 letters in between the k and s)

Kubernetes is like a data center OS where you give Kubernetes your app and it will run. Kubernetes will decide what it needs.

Kubernetes will organize all of the microservices (pods) into nodes which can be made up of multiple pods. These nodes are led by masters
as in the following picture:

![Masters and Nodes](Kubernetes/masters-nodes.png)

Masters consist of four parts:

1. apiserver (brain) - commands are sent to the apiserver from the cli
2. Cluster Store (Memory) - the cluster store keeps track of the state of nodes
3. Scheduler - the scheduler will spin up new nodes when it's time
4. Controller - this sits in a loop to watch for changes in the cluster and handles them

![Masters](Kubernetes/masters.png)

Nodes consist of the following three pieces:

1. Kublet - Registers node and watches for assignments from the master's apiserver. They will report back to the master in the case of failure and they will initialize pods when needed. It exposes an endpoint on :10255 so that it can be inspected.
2. 
