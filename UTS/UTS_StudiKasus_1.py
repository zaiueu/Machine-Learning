import pandas as pd

# Data Set
data = {
    'HARI': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'DATANG': [2, 3, 4, 1, 2, 5, 2],
    'BIAYA': [30000*2, 35000*3, 25000*4, 15000*1, 20000*2, 30000*5, 35000*2],
    'MAHASISWA': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']
}

df = pd.DataFrame(data)

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
rata_rata_mahasiswa = df['DATANG'].mean()
print(f"a) Rata-rata mahasiswa datang pada minggu ini: {rata_rata_mahasiswa:.2f}")

# b) Kapan biaya tertinggi terjadi?
biaya_tertinggi = df['BIAYA'].max()
hari_biaya_tertinggi = df.loc[df['BIAYA'] == biaya_tertinggi, 'HARI'].values[0]
print(f"b) Biaya tertinggi terjadi pada hari {hari_biaya_tertinggi}")

# c) Hari apa biaya lebih dari 110000?
hari_biaya_lebih_110000 = df.loc[df['BIAYA'] > 110000, 'HARI'].values
if len(hari_biaya_lebih_110000) > 0:
    print(f"c) Hari dengan biaya lebih dari 110000: {', '.join(hari_biaya_lebih_110000)}")
else:
    print("c) Tidak ada hari dengan biaya lebih dari 110000")

# d) Siapa yang paling banyak datang ke kampus?
mahasiswa_terbanyak = df['MAHASISWA'].value_counts().idxmax()
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {mahasiswa_terbanyak}")

# e) Siapa yang datang pada hari minggu?
mahasiswa_hari_minggu = df.loc[df['HARI'] == 'Minggu', 'MAHASISWA'].values[0]
print(f"e) Mahasiswa yang datang pada hari Minggu: {mahasiswa_hari_minggu}")

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi = df['BIAYA'].max()
biaya_terendah = df['BIAYA'].min()
print(f"f) Biaya tertinggi: {biaya_tertinggi}, Biaya terendah: {biaya_terendah}")

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_datang_tertinggi = df['DATANG'].max()
frekuensi_datang_terendah = df['DATANG'].min()
print(f"Frekuensi datang tertinggi: {frekuensi_datang_tertinggi}, Frekuensi datang terendah: {frekuensi_datang_terendah}")