# ShopAssist AI

A Python e-commerce chatbot prototype built with FastAPI.

## Features
- Product search by name, category, and price limit
- Demo shipping and returns FAQ
- REST API and interactive documentation
- Automated tests with pytest

## Run locally
Install dependencies:
    pip install -r requirements.txt

Start the API:
    uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs

## Run tests
    python -m pytest -v

## Limitations
Uses demo products and illustrative shipping and returns policies.
No live language model or real e-commerce integration yet.
