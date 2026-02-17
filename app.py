import re
from datetime import datetime
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


def get_gram_gold_price():
    url = "https://api.genelpara.com/json/"
    params = {"list": "altin", "sembol": "GA"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            gram_satis = data.get("data", {}).get("GA", {}).get("satis")
            if gram_satis:
                return float(gram_satis)
    except Exception:
        pass
    return None


def get_altins1_price():
    url = "https://www.borsa.net/hisse/altins1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            text = response.text
            match = re.search(r"güncel fiyatı\s+([\d,.]+)\s*₺", text, re.IGNORECASE)
            if not match:
                match = re.search(r"Güncel\s+([\d,.]+)\s*₺", text)
            if not match:
                match = re.search(r"ALTINS1\s*</[^>]+>\s*([\d,.]+)\s*₺", text, re.DOTALL)
            if match:
                price_str = match.group(1).replace(".", "").replace(",", ".")
                return float(price_str)
    except Exception:
        pass
    return None


def calculate_spread():
    gram_price = get_gram_gold_price()
    altins1_price = get_altins1_price()
    if not gram_price or not altins1_price:
        return {"ok": False, "error": "Veri alınamadı"}
    altins1_gram_equivalent = altins1_price * 100
    spread_tl = altins1_gram_equivalent - gram_price
    spread_percentage = (spread_tl / gram_price) * 100
    return {
        "ok": True,
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "gram_price": gram_price,
        "altins1_price": altins1_price,
        "altins1_gram_equivalent": altins1_gram_equivalent,
        "spread_tl": spread_tl,
        "spread_percentage": spread_percentage,
        "borsa_daha_pahali": spread_tl > 0,
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/spread")
def api_spread():
    data = calculate_spread()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
