# FastApi project

This project is for the computing theory class, of the information systems 4th semester.
It was built to create endpoints that recieve an automaton and an input for the automaton and returns if it is accepted or not.

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
  - docker push vitorpereira26r/fastapi-teoria-da-computacao:

## Exemples

### Deterministic Finite Automaton

#### Exemple of DFA

Has to finish in "1"

inputs:
- 1111111111111111111110 - false
- 11111111111111111111101 - false
- 111 - true
- 000000000000000001 - true

JSON:

{
    "states": ["q0","q1","q2"],
    "input_symbols": ["0", "1"],
    "transitions": {
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q0", "1": "q2"},
        "q2": {"0": "q2", "1": "q1"}
    },
    "initial_state": "q0",
    "final_states": ["q1"],
    "input_w": "111"
}

### Nondeterministic Finite Automanton

#### Exemple of NFA

Accepts only inputs that starts with an "a", finishes with an "a" and every "b", has to be followed by an "a"

inputs:
- a - true
- ababa - true
- abab - false
- baba - false

JSON:

{
  "states": ["q0", "q1", "q2"],
  "input_symbols": ["a", "b"],
  "transitions": {
    "q0": {"a": ["q1"]},
    "q1": {"a": ["q1"], "": ["q2"]},
    "q2": {"b": ["q0"]}
  },
  "initial_state": "q0",
  "final_states": ["q1"],
  "input_w": "a"
}


### Deterministic Pushdown Automaton

#### Exemple of DPDA

aibi, same number of "a" and "b"

inputs:
- aaabbb - true
- aabbba - false
- aaabb - false
- ab - true

JSON:

{
  "states": ["q0", "q1", "q2", "q3"],
  "input_symbols": ["a", "b"],
  "stack_symbols": ["0", "1"],
  "transitions": {
    "q0": {
      "a": { "0": ["q1", ["1", "0"]] }
    },
    "q1": {
      "a": { "1": ["q1", ["1", "1"]] },
      "b": { "1": ["q2", ""] }
    },
    "q2": {
      "b": { "1": ["q2", ""] },
      "": { "0": ["q3", ["0"]] }
    }
  },
  "initial_state": "q0",
  "initial_stack_symbol": "0",
  "final_states": ["q3"],
  "input_w": "aaaaabbbbb"
}
