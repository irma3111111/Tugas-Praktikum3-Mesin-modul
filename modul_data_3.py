# %%
import pandas as pd

# %%
# Membaca data dari file CSV
data = pd.read_csv("students.csv")

# %%
# Menampilkan 10 baris pertama
print(data.head(10))

# %%
# Menampilkan informasi dataset
data.info()

# %%
# Mengecek missing value
data.isna().sum()

# %%
# Handling missing value
# Mengisi missing value pada fitur 'lunch' dengan modus
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)

# Mengisi missing value pada fitur 'reading score' dengan mean
data['reading score'].fillna(data['reading score'].mean(), inplace=True)

# Mengisi missing value pada fitur 'grade' dengan median
data['grade'].fillna(data['grade'].median(), inplace=True)

# %%
# Memeriksa kembali informasi dataset setelah handling missing value
data.info()

# %%
# Alternatif metode handling missing value
# Menggunakan teknik interpolasi (linear)
data['reading score'].interpolate(method='linear', inplace=True)

# Menggunakan teknik backwardfill
data['grade'].fillna(method='bfill', inplace=True)

# Menggunakan teknik forwardfill
data['grade'].fillna(method='ffill', inplace=True)

# Menghapus baris dengan missing value
data.dropna(axis=0, inplace=True)

# Menghapus fitur jika lebih dari 50% nilainya adalah NaN
data.dropna(axis=1, inplace=True)

# %%
# Menampilkan informasi dataset setelah semua proses
data.info()
