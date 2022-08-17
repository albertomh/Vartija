# Vartija
Vartija is a simple health reporting tool for web apps.  
It provides a configurable uptime monitor to check the endpoints you choose. 
Leverages a serverless architecture hosted on AWS Lambda for cost-efficiency.

```
:construction: This project is under construction! :construction:
```


## Setup


## Develop

Recommended tools for development: VS Code (or PyCharm) and Docker & docker-compose.

### Prerequisites
Ensure you have Python 3.9 and up-to-date versions of Docker & docker-compose available on your system.

Add the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and 
[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extensions
to VS Code.

Create the file `./_docker/dev/.env` with the following contents:
```
AWS_ACCESS_KEY_ID=<KEY>
AWS_SECRET_ACCESS_KEY=<SECRET>
AWS_REGION=eu-west-1
```
This will be automatically be picked up by docker-compose when developing locally.

### Run locally
Create `dynamodb-local` & app containers by running the following from the project root:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml up --build`

Stop the db & app containers:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml down`

### Containerised services
Two services are available as Docker containers when developing locally:  
- `dynamodb-local` Uses [the official Docker image](https://hub.docker.com/r/amazon/dynamodb-local/), running under port 8000.
- `vartija` The app code, running under port 8080.

These are orchestrated via the `_docker/dev/docker-compose.dev.yml` Docker Compose file.

### DynamoDB local
DynamoDB-local is run with the `-inMemory` flag, meaning the database is not 
persisted to disk neither on the host or the container it runs in, existing only 
for the duration of the container.

### Python typings & PEP8 style compliance
Create a virtualenv and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt --quiet
```

Run type annotation checker & PEP8 style validator:
```
mypy -p vartija
pycodestyle vartija
```


---
Copyright 2022 Alberto Morón Hernández  
This software is provided as open-source under the MIT License.