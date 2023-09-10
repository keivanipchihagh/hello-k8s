# hello-k8s
Simple Hello-World single-page site, written in [Python](https://www.python.org/), served by [Flask](https://flask.palletsprojects.com/), integrated with [GitHub Actions](https://github.com/features/actions), Packaged by [Helm](https://helm.sh/), orchestrated by [Kubernetes](https://kubernetes.io/) and Delivered with [FluxCD](https://fluxcd.io/). *Oh wait*, that's the an entire **CI/CD**! 🚀

<p align="center">
  <img src="./archive/img/logo.png" />
</p>

## What is a CI/CD?
CI and CD stand for **continuous integration** and **continuous delivery**/**continuous deployment**. In other words, CI is a modern software development practice in which incremental code changes are made frequently and reliably.

## Installation
### Install Kubernetes
You can follow the [official](https://kubernetes.io/docs/setup/production-environment/tools/) documentation to install a Kubernetes Cluster on production environment. In case you believe the documentation is written in japanese, follow [this](https://www.linuxtechi.com/install-kubernetes-on-ubuntu-22-04/) tutorial.

### Install Helm
To install Helm3, run the script below which will automatically connect to your Kubernetes cluster:
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Install flux
Installing FluxCD is as easy as running the below script:
```bash
curl -s https://fluxcd.io/install.sh | sudo bash
```
However, to bootstamp FluxCD to your repository, follow [these](https://fluxcd.io/flux/installation/) instructions.

## Components
### Python
[Python](https://www.python.org/) is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming ([wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))).

### Flask
[Flask](https://flask.palletsprojects.com/) is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions ([wikipedia](https://en.wikipedia.org/wiki/Flask_(web_framework))).

### GitHub Actions
[GitHub Actions](https://github.com/features/actions) makes it easy to automate all your software workflows, now with world-class CI/CD. Build, test, and deploy your code right from GitHub. Make code reviews, branch management, and issue triaging work the way you want ([github](https://github.com/features/actions)).

### Kubernetes
[Kubernetes](https://kubernetes.io/) is an open-source container orchestration system for automating software deployment, scaling, and management. Originally designed by Google, the project is now maintained by the Cloud Native Computing Foundation. The name Kubernetes originates from Ancient Greek, meaning 'helmsman' or 'pilot' ([wikipedia](https://en.wikipedia.org/wiki/Kubernetes)).

### Helm
[Helm](https://helm.sh/) is a tool that automates the creation, packaging, configuration, and deployment of Kubernetes applications by combining your configuration files into a single reusable package. In a microservice architecture, you create more microservices as the application grows, making it increasingly difficult to manage ([circleci](https://circleci.com/blog/what-is-helm/#:~:text=Helm%20is%20a%20tool%20that,it%20increasingly%20difficult%20to%20manage.)).

### FluxCD
[FluxCD](https://fluxcd.io/) is a Continuous Delivery tool to help keep Kubernetes clusters in sync with configuration sources such as Git repositories and automate configuration updates when available. Flux is built with the GitOps toolkit and supports multi-tenancy and syncing an arbitrary number of Git repositories ([internaldeveloperplatform](https://internaldeveloperplatform.org/cd-operators/flux-cd/)).