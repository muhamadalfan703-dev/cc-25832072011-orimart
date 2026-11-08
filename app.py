from datetime import datetime, timezone
import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_NAME = "OriMart"
APP_VERSION = "0.1.0"
APP_STATUS = "running"
TAGLINE = "Thrift fashion bermerek yang terverifikasi keasliannya."
CATEGORIES = ["Pakaian", "Sepatu", "Tas/Aksesoris Fashion"]

PRODUCTS = [
    {"name": "Jaket Windbreaker", "brand": "Nike", "condition": "Bagus"},
    {"name": "Sepatu Chuck 70", "brand": "Converse", "condition": "Sangat bagus"},
    {"name": "Celana Jeans 501", "brand": "Levi's", "condition": "Cukup"},
]


@app.get("/")
def index():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        tagline=TAGLINE,
        categories=CATEGORIES,
        products=PRODUCTS,
        app_env=os.getenv("APP_ENV", "development"),
    )


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        environment=os.getenv("APP_ENV", "development"),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/api/info")
def info():
    return jsonify(
        name=APP_NAME,
        version=APP_VERSION,
        status=APP_STATUS,
    )
