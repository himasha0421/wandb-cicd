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