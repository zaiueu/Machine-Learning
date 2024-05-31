# Data Set
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
datang = [2, 3, 4, 1, 2, 5, 2]
biaya = [30000, 35000, 25000, 15000, 20000, 30000, 35000]
mahasiswa = ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
total_mahasiswa = sum(datang)
print(f"a) Rata-rata mahasiswa datang pada minggu ini: {total_mahasiswa / len(datang):.2f}")

# b) Kapan biaya tertinggi terjadi?
biaya_tertinggi = max(biaya)
hari_biaya_tertinggi = hari[biaya.index(biaya_tertinggi)]
print(f"b) Biaya tertinggi terjadi pada hari {hari_biaya_tertinggi}")

# c) Hari apa biaya lebih dari 110000?
hari_biaya_lebih_110000 = [hari[i] for i in range(len(hari)) if biaya[i] > 110000]
print(f"c) Hari dengan biaya lebih dari 110000: {', '.join(hari_biaya_lebih_110000)}")

# d) Siapa yang paling banyak datang ke kampus?
frekuensi_mahasiswa = {mahasiswa: datang.count(datang[i]) for i, mahasiswa in enumerate(mahasiswa)}
mahasiswa_terbanyak = max(frekuensi_mahasiswa, key=frekuensi_mahasiswa.get)
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {mahasiswa_terbanyak}")

# e) Siapa yang datang pada hari minggu?
mahasiswa_hari_minggu = mahasiswa[datang.index(2)]
print(f"e) Mahasiswa yang datang pada hari Minggu: {mahasiswa_hari_minggu}")

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi = max(biaya)
biaya_terendah = min(biaya)
print(f"f) Biaya tertinggi: {biaya_tertinggi}, Biaya terendah: {biaya_terendah}")

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_datang = {jumlah: datang.count(jumlah) for jumlah in set(datang)}
frekuensi_tertinggi = max(frekuensi_datang.values())
frekuensi_terendah = min(frekuensi_datang.values())
print(f"g) Frekuensi datang tertinggi: {frekuensi_tertinggi}, Frekuensi datang terendah: {frekuensi_terendah}")