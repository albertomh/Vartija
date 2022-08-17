# Vartija


## Setup


## Develop

### Prerequisites
Ensure you have recent versions of Docker and docker-compose available on your system.

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