import pandas as pd
import matplotlib.pyplot as plt

fakultas=["Bisnis", "D3Perhotelan", "ICT", "IlmuKomunikasi", "SenidanDesain"]
jumlah_mahasiswa=[260, 28, 284, 465, 735]
warna=["orange","yellow","green","blue","pink"]
akreditasi=["A","A","B","A","A"]


plt.figure(figsize=(6,2))
plt.bar(fakultas,jumlah_mahasiswa,color=warna)
plt.title("Info Mahasiswa")
plt.xlabel("Fakultas",size=11)
plt.ylabel("Jumlah Mahasiswa",size=11)
plt.xticks(size=6)
plt.xticks(size=6)
plt.show()

info = pandas.DataFrame({
    "FAKULTAS":fakultas,
    "Jumlah Mahasiswa":jumlah_mahasiswa,
    "AKREDITASI":akreditasi
})
info