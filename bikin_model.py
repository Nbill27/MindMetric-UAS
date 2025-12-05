import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# LOAD DATASET

filename = 'Student Mental health.csv'
try:
    df = pd.read_csv(filename)
    print("Data berhasil dibaca!")
except FileNotFoundError:
    print(f"Error: File '{filename}' tidak ditemukan. Cek lagi nama filenya.")
    exit()

# 2. GANTI NAMA KOLOM
df.columns = ['Timestamp', 'Gender', 'Age', 'Course', 'Year', 'CGPA', 'Marital_Status', 
              'Depression', 'Anxiety', 'Panic_Attack', 'Treatment']

# Cleaning

# Hapus baris yang kosong 
df = df.dropna()

# Fungsi membersihkan format Tahun 
def clean_year(x):
    if isinstance(x, str):
        # Kecilkan huruf, hapus kata 'year', hapus spasi
        x = x.lower().replace('year', '').strip()
        try:
            return int(x)
        except ValueError:
            return 1 
    return x

# Fungsi membersihkan CGPA misal: "3.00 - 3.49" -> diambil tengahnya 3.25
def clean_cgpa(x):
    if isinstance(x, str):
        x = x.strip() 
        if x == '3.50 - 4.00': return 3.75
        elif x == '3.00 - 3.49': return 3.25
        elif x == '2.50 - 2.99': return 2.75
        elif x == '2.00 - 2.49': return 2.25
        elif x == '0 - 1.99': return 1.0
    return 3.25 

# Terapkan fungsi di atas
df['Year'] = df['Year'].apply(clean_year)
df['CGPA'] = df['CGPA'].apply(clean_cgpa)


# ENCODING KATEGORIK KE NUMERIK

# Gender: Female=0, Male=1
df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})

# Ubah Yes/No jadi 1/0
cols_yes_no = ['Marital_Status', 'Depression', 'Anxiety', 'Panic_Attack', 'Treatment']
for col in cols_yes_no:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# Bersihkan lagi barangkali ada yang jadi NaN gara-gara typo/mapping gagal
df = df.dropna()

# TRAINING MODEL

# Fitur Soal:
X = df[['Age', 'Gender', 'CGPA', 'Year', 'Marital_Status', 'Anxiety', 'Panic_Attack']]
# Target (Jawaban):
y = df['Depression']

# 80% belajar, 20% ujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Panggil Algoritma
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Cek Akurasi
pred = model.predict(X_test)
akurasi = accuracy_score(y_test, pred)
print(f"Model selesai dilatih! Akurasi: {akurasi * 100:.2f}%")


# SIMPAN MODEL

with open('model_depression.pkl', 'wb') as f:
    pickle.dump(model, f)

print("File 'model_depression.pkl' berhasil dibuat.")