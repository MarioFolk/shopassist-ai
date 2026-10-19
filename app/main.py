from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="ShopAssist AI",
    description="E-commerce product search and customer support API",
    version="0.1.0",
)

PRODUCTS = [
    {
        "id": 1,
        "name": "Laptop Pro 14",
        "category": "electronics",
        "price": 749.00,
        "description": "Laptop with 16 GB RAM and 512 GB SSD",
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "category": "accessories",
        "price": 24.90,
        "description": "Wireless ergonomic computer mouse",
    },
    {
        "id": 3,
        "name": "USB-C Headphones",
        "category": "accessories",
        "price": 59.90,
        "description": "Wired headphones with USB-C connection",
    },
]


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)


class ChatResponse(BaseModel):
    answer: str
    products: list[dict] = Field(default_factory=list)


@app.get("/")
def home():
    return {
        "name": "ShopAssist AI",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/products")
def list_products():
    return {"products": PRODUCTS}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message.strip().lower()

    if not message:
        return ChatResponse(
            answer="Please enter a question.",
            products=[],
        )

    if any(word in message for word in [
        "shipping", "delivery", "doprava", "doručenie"
    ]):
        return ChatResponse(
            answer=(
                "Standard shipping takes 3-5 business days. "
                "This is demo information and must be confirmed "
                "against the actual store policy."
            ),
            products=[],
        )

    if any(word in message for word in [
        "return", "refund", "vrátenie", "reklamácia"
    ]):
        return ChatResponse(
            answer=(
                "Demo return policy: items can be returned within "
                "30 days. Please verify the real store policy "
                "before using this information with customers."
            ),
            products=[],
        )

    max_price = None

    import re

    price_match = re.search(
        r"(?:under|below|less than|max(?:imum)?|under €|do)\s*€?\s*(\d+(?:\.\d+)?)",
        message,
    )

    if price_match:
        max_price = float(price_match.group(1))

    search_words = [
        word for word in message.split()
        if word not in {
            "find", "search", "show", "me", "a", "an", "the",
            "for", "please", "product", "products", "under",
            "below", "less", "than", "maximum", "max",
            "do", "eur", "euro", "euros",
        }
        and not word.replace(".", "", 1).isdigit()
        and "€" not in word
    ]

    matches = []

    for product in PRODUCTS:
        searchable = (
            product["name"] + " " +
            product["category"] + " " +
            product["description"]
        ).lower()

        if max_price is not None and product["price"] > max_price:
            continue

        if any(word in searchable for word in search_words):
            matches.append(product)

    if matches:
        return ChatResponse(
            answer=f"I found {len(matches)} matching product(s).",
            products=matches,
        )

    return ChatResponse(
        answer=(
            "I could not find a matching product. "
            "Try searching for a laptop, mouse, headphones, "
            "or ask about shipping and returns."
        ),
        products=[],
    )
