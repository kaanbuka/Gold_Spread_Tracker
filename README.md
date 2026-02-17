# Gold Spread Tracker

Gram Altın (serbest piyasa) ile Borsa İstanbul AltınS1 (Darphane Altın Sertifikası) arasındaki makas farkını izleyen uygulama. Hem terminal arayüzü hem de web arayüzü sunar.

🔗 [GitHub](https://github.com/kaanbuka/Gold_Spread_Tracker)

## Özellikler

- **Gram Altın:** GenelPara API üzerinden anlık satış fiyatı
- **AltınS1:** Borsa İstanbul’da işlem gören Darphane Altın Sertifikası fiyatı
- **Makas hesabı:** 1 AltınS1 = 0,01 gram altına denk; 100 adet AltınS1 = 1 gram karşılığı
- **Terminal:** `main.py` ile konsolda sonuç
- **Web:** Şık dashboard ile tarayıcıda görüntüleme, dakikada bir otomatik yenileme

## Kurulum

```bash
git clone https://github.com/kaanbuka/Gold_Spread_Tracker.git
cd Gold_Spread_Tracker
pip install -r requirements.txt
```

## Kullanım

### Terminal

```bash
python main.py
```

Çıktı örneği:
```
[14:30:25] Piyasalar taranıyor...

==================================================
 📊 GOLD-SPREAD TRACKER (BIST vs Serbest Piyasa)
==================================================
 🥇 Fiziki/Gram Altın:          6.966,82 ₺
 📜 AltınS1 (1 Adet):           82,83 ₺
 ⚖️ AltınS1 (1 Gram Karşılığı): 8.283,00 ₺
--------------------------------------------------
 🔴 Borsa daha PAHALI (Sertifika Primli)
    Makas Farkı: +1.316,18 ₺ (+18.89%)
==================================================
```

### Web Arayüzü

```bash
python app.py
```

Tarayıcıda **http://127.0.0.1:5000** adresini açın.

## Proje Yapısı

```
Gold_Spread_Tracker/
├── app.py           # Flask web uygulaması
├── main.py          # Terminal CLI
├── requirements.txt
├── templates/
│   └── index.html   # Web arayüzü
└── README.md
```

## Veri Kaynakları

| Veri      | Kaynak |
|----------|--------|
| Gram Altın | [GenelPara API](https://api.genelpara.com/) |
| AltınS1   | [borsa.net](https://www.borsa.net/hisse/altins1) |

## Lisans

MIT
