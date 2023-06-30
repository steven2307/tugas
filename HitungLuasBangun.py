#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hitung_luas_bangun(nama_bangun, nilai):
    if nama_bangun.lower() == "trapesium":
        luas = (nilai[0] + nilai[1]) * nilai[2] / 2
    elif nama_bangun.lower() == "lingkaran":
        luas = 3.14 * nilai[0]**2
    elif nama_bangun.lower() == "balok":
        luas = nilai[0] * nilai[1] * nilai[2]
    elif nama_bangun.lower() == "segitiga":
        luas = 0.5 * nilai[0] * nilai[1]
    elif nama_bangun.lower() == "persegi panjang":
        luas = nilai[0] * nilai[1]
    elif nama_bangun.lower() == "persegi":
        luas = nilai[0]**2
    else:
        luas = None
        print("Nama bangun tidak valid.")
    return luas

def main():
    nama_bangun = input("Masukkan jenis bangun (trapesium/lingkaran/balok/segitiga/persegi panjang/persegi): ")
    nilai = []

    if nama_bangun.lower() == "trapesium":
        nilai.append(float(input("Masukkan sisi sejajar 1: ")))
        nilai.append(float(input("Masukkan sisi sejajar 2: ")))
        nilai.append(float(input("Masukkan tinggi: ")))
    elif nama_bangun.lower() == "lingkaran":
        nilai.append(float(input("Masukkan jari-jari: ")))
    elif nama_bangun.lower() == "balok":
        nilai.append(float(input("Masukkan alas: ")))
        nilai.append(float(input("Masukkan lebar: ")))
        nilai.append(float(input("Masukkan tinggi: ")))
    elif nama_bangun.lower() == "segitiga":
        nilai.append(float(input("Masukkan panjang alas: ")))
        nilai.append(float(input("Masukkan tinggi: ")))
    elif nama_bangun.lower() == "persegi panjang":
        nilai.append(float(input("Masukkan panjang: ")))
        nilai.append(float(input("Masukkan lebar: ")))
    elif nama_bangun.lower() == "persegi":
        nilai.append(float(input("Masukkan panjang sisi: ")))
    else:
        print("Nama bangun tidak valid.")
        return
    
    luas = hitung_luas_bangun(nama_bangun, nilai)
    if luas is not None:
        print("Luas", nama_bangun, "adalah", luas)

if __name__ == "__main__":
    main()

