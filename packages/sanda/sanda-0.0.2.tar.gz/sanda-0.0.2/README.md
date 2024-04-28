# Sanda

## Proof of concept
A proof of concept for a simple workflow runner build on top of component of Airflow/Luigi,
and a simple web interface to manage the workflow. The runner executes tasks on Kubernetes cluster.
All tasks in a workflow are defined in a YAML file, similar to GitHub Actions.

### Description

Sanda, a Kubernetes-based proof-of-concept workflow runner, simplifies cloud-agnostic
workflow definition, execution, and management through YAML workflows,
open-source extensibility, multiple access points, and containerized tasks

### Key Features

1. **Cloud-Agnostic:** Works seamlessly on any cloud platform using Kubernetes for flexibility and scalability.
2. **Easy Workflow Definition:** Define workflows in familiar YAML format.
3. **Open Source and Extensible:** Built with inspiration from Airflow and Luigi for broad application and customization.
4. **Multiple Access Points:** Use Sanda via CLI, Python package, or RESTful APIs.
5. **Containerized Tasks:** Leverage Docker containers for task execution, allowing any compatible task within Sanda.


### How to use

`pip install sanda`

### Design and architecture

[Design and system guide](DESIGN.md)

### How to contribute

[Contribution Guide](CONTRIBUTION.md)
