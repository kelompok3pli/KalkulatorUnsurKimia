from streamlit_lottie import st_lottie
import requests
import streamlit as st
import re
from collections import defaultdict

# Fungsi memuat animasi Lottie dari URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Massa Relatif", layout="centered")
st.title("Kalkulator Massa Relatif")

# Sidebar Navigasi dengan Emoji
menu = st.sidebar.selectbox("🔍 Navigasi", ["🏠 Beranda", "🧪 Kalkulator", "ℹ️ Tentang"])

# Data massa atom relatif (disingkat di sini, tapi Anda sudah benar)
massa_atom = {
    "H": 1.008, "O": 16.00, "C": 12.01, "Na": 22.99, "Cl": 35.45, "Cu": 63.546, "S": 32.06,
    # ... tambahkan semua elemen dari daftar lengkap Anda sebelumnya
}

# Fungsi parsing formula
def parse_formula(f):
    f = f.replace('·', '.')  # tangani hidrasi, misal: CuSO4·5H2O
    parts = f.split('.')
    total_elements = defaultdict(int)

    for part in parts:
        match = re.match(r'^(\d+)([A-Z].*)', part)
        multiplier = int(match.group(1)) if match else 1
        formula_part = match.group(2) if match else part

        pattern = r'([A-Z][a-z]*)(\d*)'
        matches = re.findall(pattern, formula_part)

        for el, count in matches:
            if el not in massa_atom:
                st.warning(f"Unsur '{el}' tidak dikenali.")
                return None
            jumlah = int(count) if count else 1
            total_elements[el] += jumlah * multiplier

    return total_elements

# Halaman Beranda
if menu == "🏠 Beranda":
    st.header("Selamat Datang di Kalkulator Massa Relatif")

    lottie_url = "https://lottie.host/b592895d-f9e1-43b1-bf8e-dea5b80b8a25/h9K58rIqKT.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="beranda")

    st.write("""
        Aplikasi ini membantu Anda menghitung massa relatif dari suatu unsur atau senyawa 
        berdasarkan rumus kimia yang diberikan. 
        Gunakan menu di samping untuk mulai menggunakan kalkulator atau mempelajari lebih lanjut.
    """)

# Halaman Kalkulator
elif menu == "🧪 Kalkulator":

    lottie_url = "https://lottie.host/5ee6c7e7-3c7b-473f-b75c-df412fe210cc/kF9j77AAsG.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="kalkulator")

    st.header("Kalkulator Massa Relatif")
    formula = st.text_input("Masukkan rumus kimia (misalnya: H2O, CO2, CuSO4·5H2O):")

    if formula:
        parsed = parse_formula(formula)
        if parsed:
            massa_total = sum(massa_atom[el] * n for el, n in parsed.items())
            st.success(f"Massa relatif dari {formula} adalah {massa_total:.2f} g/mol")
        else:
            st.error("Gagal menghitung. Pastikan rumus kimia valid dan elemen dikenali.")

# Halaman Tentang
elif menu == "ℹ️ Tentang":

    lottie_url = "https://lottie.host/49626c27-b23c-475e-8505-981d510c0e61/lag9aGftQv.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="Tentang")

    st.header("Tentang Aplikasi Ini")
    st.write("""
        Aplikasi ini dikembangkan menggunakan Streamlit dan bertujuan untuk membantu siswa dan guru
        dalam menghitung massa relatif zat kimia secara cepat dan interaktif.
    """)

    lottie_url = "https://lottie.host/4a584f69-29b5-40a0-a133-a15f4775ec6d/O3pamPxHLp.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="Tentang2")
        
    st.header("Definisi")
    st.write("""
         Mr adalah jumlah massa atom dari seluruh atom dalam suatu molekul. Digunakan untuk
         menghitung massa molar senyawa dalam satuan g/mol saat dikalikan dengan 1 mol.
    """)

# CSS untuk mengubah latar belakang menjadi abu-abu
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: ##f93ef2;  /* Pink terang */
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0); /* Transparan */
}

[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.9); /* Sidebar putih semi-transparan */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
