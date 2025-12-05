# 🧠 MindMetric

**Sistem Analisis & Deteksi Dini Kesehatan Mental Mahasiswa Berbasis Machine Learning.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Tentang Project
**MindMetric Pro** adalah aplikasi web sederhana yang dirancang untuk mendeteksi potensi risiko depresi pada mahasiswa. Aplikasi ini menganalisis pola berdasarkan data demografis, akademik (IPK), dan riwayat gejala kecemasan.

Project ini dibuat sebagai tugas **Ujian Akhir Semester (UAS)** mata kuliah Machine Learning.

### ✨ Fitur Unggulan
1.  **Dual-Engine AI:** Pengguna dapat memilih dua algoritma berbeda untuk prediksi:
    * 🌲 **Random Forest Classifier** (Akurasi Tinggi & Stabil)
    * 📈 **Logistic Regression** (Efisien & Probabilistik)
2.  **Interactive Dashboard:** Dilengkapi grafik visual (Pie Chart & Bar Chart) untuk melihat data statistik kesehatan mental di kampus.
3.  **User-Friendly Interface:** Tampilan bersih, responsif, dan mudah digunakan.
4.  **Real-time Analysis:** Hasil prediksi keluar seketika beserta persentase risikonya.

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** Python
* **Framework Web:** Streamlit
* **Machine Learning:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Visualisasi:** Plotly Express

---

## 📂 Struktur File
* `aplikasi.py`: File utama untuk menjalankan antarmuka web (Frontend).
* `bikin_model.py`: Script untuk melatih model AI dan menyimpannya ke file `.pkl`.
* `model_depression` : File "otak" AI yang sudah dilatih.
* `Student Mental health.csv`: Dataset mentah (sumber: Kaggle).
* `requirements.txt`: Daftar library yang dibutuhkan.

---

## 🚀 Cara Menjalankan (Installation)

Ikuti langkah ini untuk menjalankan aplikasi di komputer lokal:

1.  **Clone Repository ini:**
    ```bash
    [git clone [https://github.com/USERNAME_KAMU/MindMetric-UAS.git](https://github.com/USERNAME_KAMU/MindMetric-UAS.git)](https://github.com/Nbill27/MindMetric-UAS.git)
    cd MindMetric-UAS
    ```

2.  **Install Library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Latih Model (Opsional):**
    *Jika file .pkl belum ada, jalankan perintah ini dulu:*
    ```bash
    python bikin_model.py
    ```

4.  **Jalankan Aplikasi:**
    ```bash
    python -m streamlit run aplikasi.py
    ```

---

## 📊 Dataset
Dataset yang digunakan berasal dari survei kesehatan mental mahasiswa yang tersedia publik di Kaggle.
* **Total Data:** 101 Mahasiswa
* **Fitur Input:** Gender, Umur, Tahun Kuliah, Status Pernikahan, IPK, Riwayat Kecemasan (Anxiety), Riwayat Panic Attack.
* **Target Output:** Depresi (Ya/Tidak).

---

## ⚠️ Disclaimer
Aplikasi ini merupakan simulasi Machine Learning untuk tujuan **Edukasi & Akademik**. Hasil prediksi hanyalah probabilitas statistik dan **TIDAK 100% AKURAT**. Aplikasi ini bukan pengganti diagnosa medis profesional.

---

## 👨‍💻 Author
**Muhammad Nabil Deja**
* Universitas Bina Insani
