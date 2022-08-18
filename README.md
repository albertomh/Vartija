# Vartija
Vartija is a simple health reporting tool for web apps.  
It provides a configurable uptime monitor to check the endpoints you choose. 
Vartija leverages a serverless architecture hosted on AWS Lambda for cost efficiency.

> :construction: This project is under construction! :construction:


## Setup


## Develop
This section walks you through setting up for local development in order to contribute to Vartija. 
Tested using VS Code and PyCharm as IDEs.

### Prerequisites
1. Install Python 3.9+ locally (needed for linter & type annotation checker).
2. Install the latest version of [Docker](docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/).
3. Install [`awscli` v2](docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and configure it for your AWS account.
4. Create the file `./_docker/dev/.env` with the following contents:
```
AWS_ACCESS_KEY_ID=<KEY>
AWS_SECRET_ACCESS_KEY=<SECRET>
AWS_REGION=eu-west-1
```
This will be picked up by docker-compose when developing locally.

**Optional (VS Code users)**  
Add the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and 
[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) extensions
to VS Code.

### Run locally
Create containers for `dynamodb-local` & the vartija app by running the following command from the project root:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml up --build`

Stop the DynamoDB & app containers:  
`docker compose --file ./_docker/dev/docker-compose.dev.yml down`

### Containerised services
Two services are available as Docker containers when developing locally:  
- `dynamodb-local` Uses [the official Docker image](https://hub.docker.com/r/amazon/dynamodb-local/), running on port 8000.
- `vartija` The serverless app, running on port 8080.

These are orchestrated via the `_docker/dev/docker-compose.dev.yml` Docker Compose file.

#### DynamoDB local
DynamoDB-local is run with the `-inMemory` flag, meaning the database is not 
persisted to disk neither on the host or the container it runs in, existing only 
for the duration of the container.

You can interact with DynamoDB-local via the AWS CLI by specifying the endpoint:  
eg. `aws dynamodb list-tables --endpoint-url http://localhost:8000`

#### The Vartija container
The local Vartija container is based on the [amazon/aws-lambda-python](https://hub.docker.com/r/amazon/aws-lambda-python) Docker image. 

Interact with the local instance of Vartija with:  
`curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'`

### Check typings & PEP8 style compliance
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