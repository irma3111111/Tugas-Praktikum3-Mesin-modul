# %%
import pandas as pd

# %%
# Membaca data dari file CSV
data = pd.read_csv("DatasetForCoffeeSales2.csv")

# %%
# Menampilkan 10 baris pertama
print(data.head(10))

# %%
# Mengklasifikasikan tipe data
data_types = {
    'Nominal': ['Product', 'City', 'Category', 'Customer_ID'],
    'Ordinal': [],
    'Rasio': ['Sales Amount', 'Final Sales', 'Quantity', 'Unit Price', 'Discount_Amount'],
    'Interval': []
}

# %%
# Menampilkan hasil klasifikasi
total_data_types = {}
for data_type, attributes in data_types.items():
    print(f"{data_type}: {', '.join(attributes)}")
    total_data_types[data_type] = len(attributes)

# %%
# Filter data hanya menampilkan kolom tertentu
filtered_data = data.filter(["City", "Product", "Quantity", "Sales Amount"])
print(filtered_data.head())

# %%
# Sorting berdasarkan jumlah Quantity secara descending
filtered_data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
print(filtered_data.head())

# %%
# Grouping untuk melihat total Sales berdasarkan City
grp1 = data.groupby('City')
result = grp1['Sales Amount'].aggregate('sum')
print(result)
