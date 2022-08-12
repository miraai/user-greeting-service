
# User Greeting Service

Small Python webserver which sends a user a hello world message. 
The user can store their name and will be greeted with their name on the next visit.




## Prerequisites

User Greeting Service prerequisites

### Install prerequisites

- [Python 3](https://realpython.com/installing-python/) for your platfom
- [Virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Docker](https://docs.docker.com/engine/install/) for your platform
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) or any local cluster of your choice
## Run Locally

Clone the project

```bash
  git clone https://github.com/miraai/user-greeting-service.git
```

Go to the project directory

```bash
  cd user-greeting-service
```

Create virtualenv
```bash
  virtualenv .env
  source .env/bin/activate
```

Install requirements

```bash
  pip install user_greeting_service/requirements.txt
```

Start the server

```bash
  gunicorn -w 2 -b 0.0.0.0:9090 wsgi:app
```


## Deployment

You can deploy this project using docker-compose or kubectl

### Docker-compose

Start all services
```bash
  docker-compose up -d 
```

Stop all services
```bash
  docker-compose down
```

### K8s (kubectl)

Go to k8s directory
```bash
  cd k8s
```

Start minikube
```bash
  minikube start
```

Create namespace
```bash
  kubectl create ns user-greeting-service
```

Apply files using kubectl
```bash
  kubectl apply -f app-service.yml -n user-greeting-service
  kubectl apply -f app-deployment.yml -n user-greeting-service
  kubectl apply -f redis-configmap.yml -n user-greeting-service
  kubectl apply -f redis-service.yml -n user-greeting-service
  kubectl apply -f redis-deployment.yml -n user-greeting-service
```

Get all pods in the namespace
```bash
  kubectl get pods -n user-greeting-service
```

Port-forward from desired pod to localhost
```bash
  # Example pod, can be done on deployment as well
  kubectl port-forward app-5976748d7b-tv92q 9090:9090 -n user-greeting-service
```
## Usage

Send simple POST request
```bash
  curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Neo\"}" http://localhost:9090
```