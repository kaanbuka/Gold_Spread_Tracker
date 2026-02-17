import requests
import re
from datetime import datetime

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
    except Exception as e:
        print(f"Gram Altın fiyatı çekilirken hata oluştu: {e}")
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
    except Exception as e:
        print(f"AltınS1 fiyatı çekilirken hata oluştu: {e}")
        return None


def main():
    zaman = datetime.now().strftime('%H:%M:%S')
    print(f"[{zaman}] Piyasalar taranıyor...\n")
    gram_price = get_gram_gold_price()
    altins1_price = get_altins1_price()
    if gram_price and altins1_price:
        altins1_gram_equivalent = altins1_price * 100
        spread_tl = altins1_gram_equivalent - gram_price
        spread_percentage = (spread_tl / gram_price) * 100
        print("=" * 50)
        print(" 📊 GOLD-SPREAD TRACKER (BIST vs Serbest Piyasa)")
        print("=" * 50)
        print(f" 🥇 Fiziki/Gram Altın:          {gram_price:,.2f} ₺")
        print(f" 📜 AltınS1 (1 Adet):           {altins1_price:,.2f} ₺")
        print(f" ⚖️ AltınS1 (1 Gram Karşılığı): {altins1_gram_equivalent:,.2f} ₺")
        print("-" * 50)
        if spread_tl > 0:
            print(f" 🔴 Borsa daha PAHALI (Sertifika Primli)")
            print(f"    Makas Farkı: +{spread_tl:,.2f} ₺ (+%{spread_percentage:.2f})")
        else:
            print(f" 🟢 Borsa daha UCUZ (Sertifika İskontolu)")
            print(f"    Makas Farkı: {spread_tl:,.2f} ₺ (%{spread_percentage:.2f})")
        print("=" * 50)
    else:
        print("Verilerden biri eksik olduğu için makas hesaplanamadı.")

if __name__ == "__main__":
    main()
