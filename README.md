# Ciaran's Python Project Template

This is a project template for general-purpose Python project
bootstrapping. It provides a basic Poetry project with a run script, a
Dockerfile, and Visual Studio Code debugging pre-configured so you can
get things running as quickly as possible.

## Inspiration

- Claudio Jolowicz' [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) articles
- GitHub's stock Python [gitignore file](https://github.com/github/gitignore/blob/main/Python.gitignore) (it's overkill, but it works)

## Build and run with Poetry

Just `cd` into this directory and run:
`./build_run.sh`

## Build and run with Docker

Just `cd` into this directory and run:
`docker build -q . | xargs docker run`
