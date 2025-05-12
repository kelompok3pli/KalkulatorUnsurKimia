import streamlit as st

# Judul aplikasi
st.set_page_config(page_title="Kalkulator Massa Relatif", layout="centered")
st.title("Kalkulator Massa Relatif")

# Sidebar navigasi
menu = st.sidebar.selectbox("Navigasi", ["Beranda", "Kalkulator", "Tentang"])

# Konten untuk masing-masing halaman
if menu == "Beranda":
    st.header("Selamat Datang di Kalkulator Massa Relatif")
    st.write("""
        Aplikasi ini membantu Anda menghitung massa relatif dari suatu unsur atau senyawa 
        berdasarkan rumus kimia yang diberikan. 
        Gunakan menu di samping untuk mulai menggunakan kalkulator atau mempelajari lebih lanjut.
    """)

elif menu == "Kalkulator":
    st.header("Kalkulator Massa Relatif")
    formula = st.text_input("Masukkan rumus kimia (misalnya: H2O, CO2, C6H12O6):")

    # Data massa atom relatif sederhana
    massa_atom = {
        'H': 1.008, 'C': 12.01, 'O': 16.00, 'N': 14.01, 'S': 32.07,
        'Na': 22.99, 'Cl': 35.45, 'K': 39.10, 'Mg': 24.31, 'Ca': 40.08
    }

    import re
    from collections import defaultdict

    def parse_formula(f):
        pattern = r'([A-Z][a-z]*)(\d*)'
        matches = re.findall(pattern, f)
        elements = defaultdict(int)
        for (el, count) in matches:
            if el not in massa_atom:
                st.warning(f"Unsur '{el}' tidak dikenali.")
                return None
            count = int(count) if count else 1
            elements[el] += count
        return elements

    if formula:
        parsed = parse_formula(formula)
        if parsed:
            massa_total = sum(massa_atom[el] * n for el, n in parsed.items())
            st.success(f"Massa relatif dari {formula} adalah {massa_total:.2f} g/mol")

elif menu == "Tentang":
    st.header("Tentang Aplikasi Ini")
    st.write("""
        Aplikasi ini dikembangkan menggunakan Streamlit dan bertujuan untuk membantu siswa dan guru
        dalam menghitung massa relatif zat kimia secara cepat dan interaktif.
        
        Dibuat oleh: [Nama Anda]  
        Versi: 1.0  
        Lisensi: Open Source
    """)
