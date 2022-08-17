# Vartija


## Setup


## Develop
From project root:
Create `dynamodb-local` & app containers:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml up --build`

Stop the db & app containers:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml down`

### Containerisation
Two services are available as Docker containers when developing locally:  
- `dynamodb-local` Created using [the official Docker image](https://hub.docker.com/r/amazon/dynamodb-local/), running under port 8000.
- `vartija` The app code, running under port 8080.

These are orchestrated via the `_docker/dev/docker-compose.dev.yml` Docker Compose file.

**DynamoDB local**  
DynamoDB-local is run with the `-inMemory` flag, meaning the database is not 
persisted to disk neither on the host or the container it runs in, existing only 
for the duration of the container.


---
Copyright 2022 Alberto Morón Hernández  
This software is provided as open-source under the MIT License.