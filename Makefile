build:
    docker-compose build

helm:
    helm install -f charts/values.yaml hello-k8s charts
