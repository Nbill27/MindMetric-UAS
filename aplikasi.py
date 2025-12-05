import streamlit as st
import pickle
import numpy as np

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="MindMetric Check-up",
    page_icon="🌿",
    layout="centered"
)

# 2. Load Model
try:
    with open('model_depression.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan 'model_depression.pkl' ada.")
    st.stop()


# BAGIAN ATAS: PERKENALAN (INTRO)

st.title("🌿 MindMetric")
st.markdown("### Halo, Apa Kabar Kamu Hari Ini?")

st.info("""
**Selamat datang di MindMetric.** 👋
Aplikasi ini dibuat untuk membantu mahasiswa mengenali kondisi kesehatan mentalnya lebih dini berdasarkan pola akademik dan keseharian.

**Cara kerjanya simpel:**
Cukup jawab beberapa pertanyaan di bawah ini dengan jujur. AI kami akan mencocokkan jawabanmu dengan pola data dari ribuan mahasiswa lain untuk memberikan gambaran kondisi mentalmu saat ini.
""")

st.write("---") 


# BAGIAN TENGAH: FORM INPUT

st.header("📋 Langkah 1: Profil Singkat")
st.caption("Data ini hanya digunakan untuk analisa sesaat dan tidak disimpan.")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    gender_val = 1 if gender == "Laki-laki" else 0
    
    age = st.number_input("Usia saat ini", 17, 30, 20)
    
    year = st.selectbox("Tahun Kuliah", ("Tahun 1", "Tahun 2", "Tahun 3", "Tahun 4", "Akhir"))
    year_val = int(year.split()[1]) if "Tahun" in year else 5

with col2:
    marital = st.selectbox("Status Pernikahan", ("Belum Menikah", "Sudah Menikah"))
    marital_val = 1 if marital == "Sudah Menikah" else 0
    
    cgpa = st.selectbox("Bagaimana performa nilai (IPK) terakhir?", 
        ("Sangat Baik (3.50 - 4.00)", "Baik (3.00 - 3.49)", "Cukup (2.50 - 2.99)", "Perlu Perbaikan (< 2.50)"))
    
    if "3.50" in cgpa: cgpa_val = 3.75
    elif "3.00" in cgpa: cgpa_val = 3.25
    elif "2.50" in cgpa: cgpa_val = 2.75
    else: cgpa_val = 2.0

st.write("") # Spasi
st.header("💭 Langkah 2: Cek Perasaan")
st.caption("Jawablah sesuai dengan apa yang kamu rasakan belakangan ini.")


st.markdown("**1. Tentang Rasa Cemas**")
anxiety = st.radio(
    "Apakah belakangan ini kamu sering merasa gelisah, overthinking, atau khawatir berlebihan yang sulit dikendalikan?", 
    ("Tidak, perasaan saya cukup tenang", "Ya, saya sering merasa begitu"),
)
anxiety_val = 1 if "Ya" in anxiety else 0

st.write("") 

st.markdown("**2. Tentang Reaksi Fisik**")
panic = st.radio(
    "Pernahkah kamu tiba-tiba merasa takut hebat yang disertai gejala fisik (seperti jantung berdebar kencang atau sesak napas) tanpa sebab yang jelas?",
    ("Tidak pernah", "Ya, pernah mengalaminya"),
)
panic_val = 1 if "Ya" in panic else 0

st.write("---")


# BAGIAN BAWAH: TOMBOL & HASIL
if st.button("🔍 Analisa Kondisi Saya", use_container_width=True):
    # Proses Prediksi
    input_data = [[age, gender_val, cgpa_val, year_val, marital_val, anxiety_val, panic_val]]
    hasil = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1] * 100

    if hasil == 1:
        st.warning(f"### ⚠️ Hasil Analisa: Perlu Perhatian ({prob:.0f}%)")
        st.write("""
        Sistem mendeteksi adanya pola yang mirip dengan kondisi tekanan mental atau risiko depresi. 
        **Saran:** Jangan ragu untuk bercerita kepada teman dekat, keluarga, atau mencari layanan konseling kampus. Perasaanmu valid dan pantas didengar.
        """)
    else:
        st.success(f"###  Hasil Analisa: Kondisi Stabil ({prob:.0f}%)")
        st.write("""
        Sistem menganalisa bahwa kondisi mentalmu saat ini tergolong stabil dan terjaga.
        **Saran:** Pertahankan keseimbangan antara kuliah dan istirahat. Lanjutkan hal-hal positif yang sudah kamu lakukan!
        """)


# DISCLAIMER

st.write("")
st.write("")
st.markdown("---")
st.caption("""
**⚠️ DISCLAIMER PENTING:** Aplikasi ini menggunakan teknologi *Machine Learning* (Kecerdasan Buatan) untuk tujuan simulasi dan skrining awal. 
Hasil yang ditampilkan **TIDAK 100% AKURAT** dan **BUKAN PENGGANTI DIAGNOSA DOKTER/PSIKOLOG**. 
Jika kamu merasa butuh bantuan, segera hubungi profesional kesehatan mental.
""")