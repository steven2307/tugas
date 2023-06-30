#!/usr/bin/env python
# coding: utf-8

# In[2]:


def hitung_gaji(golongan, jam_kerja):
    if golongan == "A":
        gaji_pokok = 10000000
    elif golongan == "B":
        gaji_pokok = 7000000
    elif golongan == "C":
        gaji_pokok = 5000000
    elif golongan == "D":
        gaji_pokok = 3000000
    else:
        print("Golongan tidak valid.")
        return
    
    if jam_kerja > 48:
        gaji_total = gaji_pokok + (jam_kerja - 40) * (gaji_pokok / 40) * 1.5
    else:
        gaji_total = gaji_pokok
    
    return gaji_total

def main():
    golongan = input("Masukkan golongan (A/B/C/D): ")
    jam_kerja = float(input("Masukkan jam kerja per bulan: "))
    
    while jam_kerja <= 0:
        print("Jam kerja harus lebih besar dari 0.")
        jam_kerja = float(input("Masukkan jam kerja per bulan: "))
    
    gaji = hitung_gaji(golongan, jam_kerja)
    print("Gaji pokok karyawan adalah Rp", format(gaji, ",.2f"))

if __name__ == "__main__":
    main()

