from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "ShopAssist AI"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200

    products = response.json()["products"]
    assert len(products) >= 1
    assert any(p["name"] == "Laptop Pro 14" for p in products)


def test_search_laptop_under_800():
    response = client.post(
        "/chat",
        json={"message": "Find a laptop under 800"},
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data["products"]) >= 1
    assert data["products"][0]["name"] == "Laptop Pro 14"
    assert data["products"][0]["price"] < 800


def test_shipping_question():
    response = client.post(
        "/chat",
        json={"message": "How long does shipping take?"},
    )

    assert response.status_code == 200
    assert "3-5 business days" in response.json()["answer"]


def test_returns_question():
    response = client.post(
        "/chat",
        json={"message": "What is your return policy?"},
    )

    assert response.status_code == 200
    assert "30 days" in response.json()["answer"]


def test_unknown_product():
    response = client.post(
        "/chat",
        json={"message": "Find a spaceship"},
    )

    assert response.status_code == 200
    assert response.json()["products"] == []
    assert "could not find" in response.json()["answer"]


def test_empty_message_is_rejected():
    response = client.post(
        "/chat",
        json={"message": ""},
    )

    assert response.status_code == 422
