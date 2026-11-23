import streamlit as st

from stok import StokHatasi, kritik_mi, kritik_urunler, urun_ekle

st.set_page_config(page_title="Basit Stok Takibi", page_icon="📦")
st.title("📦 Basit Stok Takibi")

# Streamlit her etkileşimde betiği baştan çalıştırır;
# ürün listesini kaybetmemek için session_state'te tutuyoruz.
if "urunler" not in st.session_state:
    st.session_state.urunler = []

# Uyarılar sayfanın en üstünde görünsün diye yer ayırıyoruz.
# İçini, form işlendikten SONRA dolduruyoruz; böylece yeni eklenen
# kritik ürün de aynı anda uyarıda görünür.
uyari_alani = st.container()

st.header("Ürün ekle")
with st.form("urun_ekle_formu", clear_on_submit=True):
    ad = st.text_input("Ürün adı")
    stok = st.number_input("Mevcut stok", step=1, value=0)
    kritik = st.number_input("Kritik seviye", step=1, value=0)
    gonder = st.form_submit_button("Ekle")

if gonder:
    try:
        urun = urun_ekle(st.session_state.urunler, ad, int(stok), int(kritik))
        st.success(f"'{urun.ad}' eklendi.")
    except StokHatasi as hata:
        st.error(str(hata))

with uyari_alani:
    for u in kritik_urunler(st.session_state.urunler):
        st.warning(
            f"⚠️ **{u.ad}** kritik seviyede: stok {u.stok}, "
            f"kritik seviye {u.kritik_seviye}. Sipariş vermeyi düşünün."
        )

st.header("Ürün listesi")
if st.session_state.urunler:
    st.table(
        [
            {
                "Ürün": u.ad,
                "Stok": u.stok,
                "Kritik seviye": u.kritik_seviye,
                "Durum": "⚠️ Kritik" if kritik_mi(u) else "✅ Yeterli",
            }
            for u in st.session_state.urunler
        ]
    )
else:
    st.info("Henüz ürün eklenmedi.")
