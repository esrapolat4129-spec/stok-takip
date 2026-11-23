import pytest

from stok import StokHatasi, kritik_urunler, urun_ekle


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


def test_kritik_seviyenin_altindaki_urun_listelenir():
    urunler = []
    urun_ekle(urunler, "Vida M8", 5, 20)
    assert [u.ad for u in kritik_urunler(urunler)] == ["Vida M8"]


def test_kritik_seviyeye_esit_urun_listelenir():
    urunler = []
    urun_ekle(urunler, "Somun", 20, 20)
    assert len(kritik_urunler(urunler)) == 1


def test_kritik_seviyenin_ustundeki_urun_listelenmez():
    urunler = []
    urun_ekle(urunler, "Pul", 21, 20)
    assert kritik_urunler(urunler) == []


def test_karisik_listede_sadece_kritikler_doner():
    urunler = []
    urun_ekle(urunler, "Vida M8", 120, 20)
    urun_ekle(urunler, "Somun", 3, 10)
    urun_ekle(urunler, "Pul", 10, 10)
    assert [u.ad for u in kritik_urunler(urunler)] == ["Somun", "Pul"]
