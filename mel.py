def hitung():
    harga = float(input("Harga: "))
    print(f"Harga awal: {harga}")
hitung()

persen = float(input("Diskon (%): "))
potongan = harga * (persen / 100)
total = harga - potongan
print(f"Potongan: Rp{potongan:,.2f}")
print(f"Total Bayar: Rp{total:,.2f}")
try:
    # Jalankan semua kode di atas
except ValueError:
    print("Input harus angka!")