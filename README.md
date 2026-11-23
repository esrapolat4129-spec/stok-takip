# 📦 Basit Stok Takibi

## Problem ve hedef kullanıcı

Küçük işletmeler (atölye, kırtasiye, küçük market) ve öğrenci kulüpleri stoklarını çoğu zaman
defterde ya da dağınık Excel dosyalarında tutar. Bu yüzden bir ürünün bittiği, iş işten geçtikten
sonra fark edilir. Bu uygulama, **ERP sistemi kullanmayan küçük işletme sahipleri** için ürünleri
tek ekranda listeleyen ve stoğu kritik seviyeye düşen ürünleri önceden haber veren basit bir
stok takip aracıdır.

## İş takip panosu

👉 Pano: https://github.com/users/esrapolat4129-spec/projects/1

## Kurulum ve çalıştırma

Python 3.10 veya üzeri gerekir.

```bash
git clone https://github.com/esrapolat4129-spec/stok-takip.git
cd stok-takip
python -m venv .venv
# Windows: .venv\Scripts\activate    |  macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Uygulama tarayıcıda `http://localhost:8501` adresinde açılır.

Otomatik testleri çalıştırmak için:

```bash
pytest
```

## Özellikleri deneme

### 1. Ürün ekleme (#2)

1. "Ürün ekle" formunda ad `Vida M8`, stok `120`, kritik seviye `20` girip **Ekle**'ye basın.
   → Yeşil "eklendi" mesajı çıkar ve ürün tabloda görünür.
2. Adı boş bırakıp **Ekle**'ye basın. → "Ürün adı boş olamaz." hatası çıkar, tabloya bir şey eklenmez.
3. Stok alanına `-5` yazıp ekleyin. → "Stok miktarı negatif olamaz." hatası çıkar.
4. Tekrar `vida m8` adıyla ürün eklemeyi deneyin. → "zaten kayıtlı" hatası çıkar.

### 2. Kritik stok uyarısı (#3)

_Geliştirme devam ediyor._

## Bilinen sınırlamalar

- Veriler şu an yalnızca tarayıcı oturumunda tutulur; sayfa yenilenince silinir
  (kalıcı kayıt panoda ayrı bir görev olarak planlandı).
