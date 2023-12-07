# FastApi project

This project is for the computing theory class, of the information systems 4th semester.
It was built to create endpoints that recieve an automata and an input for the automata and returns if it is accepted or not.

There are some exemples of json to send in the file "test_main.http", in the root of the project.

The project can be executed with docker (the instructions are in the Dockerfile), and the docker image can be found in my docker hub (https://hub.docker.com/repository/docker/vitorpereira26r/fastapi-teoria-da-computacao/general)

## How to execute

### Requirements

- Docker installed

### Instructions

- Build the image from the Dockerfile
  - docker build -t vitorpereira26r/fastapi-teoria-da-computacao:v0 .
- see the images in the PC
  - docker image ls
- run the image
  - docker container run -p 8000:8000 vitorpereira26r/fastapi-teoria-da-computacao:v0
- see containers running
  - docker container ls
- push to docker hub 
  - docker push vitorpereira26r/fastapi-teoria-da-computacao:v