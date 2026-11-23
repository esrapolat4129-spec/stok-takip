"""Stok takibinin iş mantığı.

Arayüzden (app.py) bağımsız tutuldu; böylece pytest ile doğrudan test edilebilir.
"""
from dataclasses import dataclass


@dataclass
class Urun:
    ad: str
    stok: int
    kritik_seviye: int


class StokHatasi(ValueError):
    """Kullanıcıya gösterilecek doğrulama hataları için."""


def urun_ekle(urunler: list[Urun], ad: str, stok: int, kritik_seviye: int) -> Urun:
    """Girdileri doğrular, geçerliyse ürünü listeye ekler ve döndürür."""
    ad = ad.strip()
    if not ad:
        raise StokHatasi("Ürün adı boş olamaz.")
    if stok < 0:
        raise StokHatasi("Stok miktarı negatif olamaz.")
    if kritik_seviye < 0:
        raise StokHatasi("Kritik seviye negatif olamaz.")
    if any(u.ad.casefold() == ad.casefold() for u in urunler):
        raise StokHatasi(f"'{ad}' adlı ürün zaten kayıtlı.")

    urun = Urun(ad=ad, stok=stok, kritik_seviye=kritik_seviye)
    urunler.append(urun)
    return urun


def kritik_mi(urun: Urun) -> bool:
    """Stok kritik seviyeye eşit veya altındaysa True döner."""
    return urun.stok <= urun.kritik_seviye


def kritik_urunler(urunler: list[Urun]) -> list[Urun]:
    """Stoğu kritik seviyede veya altında olan ürünleri döndürür."""
    return [u for u in urunler if kritik_mi(u)]
