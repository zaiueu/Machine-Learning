import pandas as pd
import numpy as np

# Daftar mahasiswa
mahasiswa = ["Ani", "Budi", "Joni", "Jono", "Lono"]

# Biaya yang dihabiskan setiap mahasiswa per kunjungan
biaya_mahasiswa = {
   "Ani": 30000,
   "Budi": 35000,
   "Joni": 20000,
   "Jono": 25000,
   "Lono": 15000
}

# Fungsi untuk menghitung total biaya dalam seminggu
def hitung_total_biaya_seminggu(mahasiswa, biaya_mahasiswa):
   total_biaya = 0
   for nama in mahasiswa:
       biaya_per_mahasiswa = biaya_mahasiswa[nama]
       total_biaya += biaya_per_mahasiswa * 7  # Asumsi setiap mahasiswa datang setiap hari dalam seminggu
   return total_biaya

# Memanggil fungsi untuk menghitung total biaya dalam seminggu
total_biaya_seminggu = hitung_total_biaya_seminggu(mahasiswa, biaya_mahasiswa)
print(f"Total biaya yang dihabiskan seluruh mahasiswa dalam seminggu: Rp{total_biaya_seminggu}")