# wandb-cicd
ml cicd workflow with github actions and wandb framework

## step 1. hello world github action 
```
name: GitHub Actions Demo
on : [push]

jobs :
    Explore-GitHub-Actions:
        runs-on: ubuntu-latest
        steps:
            - run: echo "the job was automatically tiggered by a ${{github.event_name}} event."
            - run: echo "this job is now running on a ${{runner.os}} server hosted by GitHub!"
            - run: echo "the name of the branch is ${{github.ref}} and your repository is ${{github.repository}}"
```

## step 2. run python file using github actions

```
name: GitHub Actions Demo
on : [push]

jobs :
    Explore-GitHub-Actions:
        runs-on: ubuntu-latest
        steps:
            - run: echo "the job was automatically tiggered by a ${{github.event_name}} event."
            - run: echo "this job is now running on a ${{runner.os}} server hosted by GitHub!"
            - run: echo "the name of the branch is ${{github.ref}} and your repository is ${{github.repository}}"
            - name: Check out the repository code
              uses: actions/checkout@v3
            - run: echo "the ${{github.repository}} has been cloned to the runner"
            - name: List files in the repository
              run: |
                    ls ${{github.workspace}}
            - name: Run python file
              run: |
                pip install -r requirements.txt
                python ci.py

```

## step 3. add trigger for pull-request using github actions

```
name: trigger-demo
on: 
    push:
        branches:
            - main
    pull_request:
    workflow_dispatch:

jobs:
    trigger-demo:
        runs-on: ubuntu-latest
        steps:
            - run: echo "first pull request tigger github action"
```

## step 4. add pr issue github action

```
name: W&B Integration
on:
    issue_comment: # tigger on pr comment

env:
    MAGIC_COMMENT: "/wandb" # this is a parameter you can change

permissions:
    contents: read
    issues: write
    pull-requests: write

jobs:
```



## step 5. Setup EC2 instance

follow below commands 

```
sudo apt-get update -y
sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker
```
## step 6. setup self-hosted runner

1a)
```
# Create a folder
$ mkdir actions-runner && cd actions-runner# Download the latest runner package

$ curl -o actions-runner-linux-x64-2.303.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.303.0/actions-runner-linux-x64-2.303.0.tar.gz

# Optional: Validate the hash
$ echo "e4a9fb7269c1a156eb5d5369232d0cd62e06bec2fd2b321600e85ac914a9cc73  actions-runner-linux-x64-2.303.0.tar.gz" | shasum -a 256 -c

# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.303.0.tar.gz
```

2b)

```
# Create the runner and start the configuration experience

$ ./config.sh --url https://github.com/himasha0421/wandb-cicd --token ANJU2HIWMOBGPDBS2VC6NATEJ564O# Last step, run it!

$ ./run.sh
```






















