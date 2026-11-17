# ShopAssist AI

A containerized e-commerce chatbot REST API built with **Python 3.12** and **FastAPI**, with automated testing using **pytest** and continuous integration through **GitHub Actions**.

## Features

- Product search by name and category
- Product filtering by maximum price
- Demo FAQ for shipping and returns
- REST API with interactive Swagger documentation
- Input validation using Pydantic
- Automated API tests with pytest
- Multi-stage Docker build (production and test images)
- Docker Compose for local deployment
- Non-root user in the production container
- Docker health check
- GitHub Actions CI workflow

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Docker
- Docker Compose
- GitHub Actions

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Run Tests

Run the automated test suite:

```bash
python -m pytest -v
```

## Run with Docker

Build and start the production application:

```bash
sudo docker compose up --build -d app
```

Check container status:

```bash
sudo docker compose ps
```

Check application health:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Stop the application:

```bash
sudo docker compose down
```

## Run Tests in Docker

Run the dedicated test service:

```bash
sudo docker compose --profile test run --rm tests
```

Alternatively, build and run the test image directly:

```bash
sudo docker build --target test -t shopassist-ai:test .
sudo docker run --rm shopassist-ai:test
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status and version |
| GET | `/health` | Health check |
| GET | `/products` | List available products |
| POST | `/chat` | Chatbot product search and FAQ |

Interactive API documentation: `/docs`

## Continuous Integration

GitHub Actions automatically:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs development dependencies.
4. Runs the pytest suite.
5. Builds the production Docker image.
6. Builds the test Docker image.
7. Executes tests inside Docker.

The workflow is defined in `.github/workflows/ci.yml`.

## Project Structure

```text
shopassist-ai/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Current Test Results

- **8 automated API tests passing**
- Production Docker image builds successfully
- Test Docker image builds successfully
- API responds successfully in Docker
- Container runs as a non-root user
- Docker health check reports healthy

## Limitations

This is a prototype using demo product data and illustrative shipping and returns policies.

It does not currently include a live language model, database, authentication, or real e-commerce integrations.
