# README

## What is this?

This is a boilerplate for FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Features

- High performance, on par with NodeJS and Go.
- Fast to code: Increase the speed to develop features by about 200% to 300%.
- Fewer bugs: Reduce about 40% of human (developer) induced errors.
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs.

## Notes

- Execute `poetry shell` to activate the virtual environment.
- Configure the IDE's interpreter to use the virtual environment created by Poetry.
- Use `uvicorn main:app --reload` to start the server.
- Visit `http://localhost:8000/docs` for interactive API documentation.

## Docker Commands

- `make build`: Builds the Docker images without using cache.
- `make migrate`: Executes the migration script.
- `make start`: Starts the Docker containers.
- `make startd`: Starts the Docker containers in the background. Execute the exec commands after running this command.
- `make stop`: Stops the Docker containers.
- `make test`: Runs tests using pytest. Execute this command after running the `startd` command.
- `make lint`: Lints the code using flake8. Execute this command after running the `startd` command.
- `make format`: Formats the code using black. Execute this command after running the `startd` command.
- `make typecheck`: Checks the types using mypy. Execute this command after running the `startd` command.

## Requirements

- Python 3.6+
- Poetry
- Uvicorn
- FastAPI
