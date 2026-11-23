import pytest

from stok import StokHatasi, urun_ekle


def test_gecerli_urun_eklenir():
    urunler = []
    urun_ekle(urunler, "Vida M8", 120, 20)
    assert len(urunler) == 1
    assert urunler[0].ad == "Vida M8"
    assert urunler[0].stok == 120


def test_bosluklar_temizlenir():
    urunler = []
    urun_ekle(urunler, "  Somun  ", 5, 1)
    assert urunler[0].ad == "Somun"


@pytest.mark.parametrize(
    "ad, stok, kritik",
    [("", 10, 2), ("   ", 10, 2), ("Pul", -1, 2), ("Pul", 10, -5)],
)
def test_gecersiz_girdi_reddedilir(ad, stok, kritik):
    urunler = []
    with pytest.raises(StokHatasi):
        urun_ekle(urunler, ad, stok, kritik)
    assert urunler == []


def test_ayni_isim_tekrar_eklenemez():
    urunler = []
    urun_ekle(urunler, "Vida M8", 10, 2)
    with pytest.raises(StokHatasi):
        urun_ekle(urunler, "vida m8", 5, 1)
    assert len(urunler) == 1
