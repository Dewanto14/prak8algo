# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:26:11 2023

@author: Huawei
"""

def pangkat_hasil(jumlah, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat > 0:
        return jumlah * pangkat_hasil(jumlah, pangkat - 1)
    else:
        return 1 / (jumlah * pangkat_hasil(jumlah, -pangkat - 1))
  
while True:
    print("Ini adalah program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    jumlah_str = (input("Masukkan Angka: "))
    if not jumlah_str:
        print("Terimakasih")
        break   
    jumlah = int(jumlah_str)
    pangkat = float(input("Masukkan Pangkat: "))
    hasil = pangkat_hasil(jumlah, pangkat)
    print(f"Hasilnya adalah = {hasil}")
