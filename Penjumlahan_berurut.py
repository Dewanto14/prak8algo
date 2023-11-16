# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:07:42 2023

@author: Huawei
"""

def jumlah_berurut(jumlah, current=1, total=0):
    if current > jumlah:
        return total
    else:
        angka = float(input("Masukkan angka ke-{}: ".format(current)))
        return jumlah_berurut(jumlah, current + 1, total + angka)

jumlah = int(input("Masukkan Jumlah: "))
hasil = jumlah_berurut(jumlah)
print("Hasil penjumlahan berurut:", hasil)
