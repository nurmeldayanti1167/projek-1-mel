def hitung():
    harga = float(input("Harga: "))
    print(f"Harga awal: {harga}")
hitung()

persen = float(input("Diskon (%): "))
potongan = harga * (persen / 100)
total = harga - potongan