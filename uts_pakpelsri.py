from collections import deque

class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

daftar_produk = [
    Produk("1", "Beras 5kg", 60000),
    Produk("2", "Minyak Goreng 2L", 28000),
    Produk("3", "Gula 1kg", 14000),
    Produk("4", "Sabun Mandi", 6000),
    Produk("5", "Susu Kaleng", 12000)
]

riwayat_transaksi = deque()

def tampilkan_produk():
    print("=== Daftar Produk ===")
    for produk in daftar_produk:
        print(f"{produk.kode} - {produk.nama} : Rp{produk.harga}")

def cari_produk(kode):
    for produk in daftar_produk:
        if produk.kode == kode:
            return produk
    return None

def transaksi():
    keranjang = []  
    while True:
        kode = input("Masukkan kode produk: ").upper()
        produk = cari_produk(kode)
        if produk:
            try:
                jumlah = int(input(f"Masukkan jumlah untuk {produk.nama}: "))
                keranjang.append((produk, jumlah))
            except ValueError:
                print("Jumlah tidak valid!")
        else:
            print("Produk tidak ditemukan!")

        lanjut = input("Tambah barang lain? (y/n): ").lower()
        if lanjut != 'y':
            break

    print("\n=== Rincian Belanja ===")
    total = 0
    for item, qty in keranjang:
        subtotal = item.harga * qty
        print(f"{item.nama},{qty} = Rp{subtotal}")
        total += subtotal

    print(f"Total Belanja: Rp{total}")

    while True:
        try:
            bayar = int(input("Masukkan uang dibayar: Rp"))
            if bayar >= total:
                kembalian = bayar - total
                print(f"Kembalian: Rp{kembalian}")
                break
            else:
                print("Uang tidak cukup.")
        except ValueError:
            print("Masukkan angka yang valid.")

    riwayat_transaksi.append({
        "keranjang": keranjang,
        "total": total,
        "bayar": bayar,
        "kembalian": kembalian
    })

    print("\nTransaksi berhasil disimpan ke riwayat.\n")


if __name__ == "__main__":
    while True:
        tampilkan_produk()
        transaksi()

        lagi = input("Ingin transaksi lagi? (y/n): ").lower()
        if lagi != 'y':
            break

    print("\n=== Riwayat Transaksi ===")
    for i, transaksi in enumerate(riwayat_transaksi, start=1):
        print(f"\nTransaksi #{i}")
        for item, qty in transaksi["keranjang"]:
            print(f"{item.nama}.{qty} = Rp{item.harga * qty}")
        print(f"Total: Rp{transaksi['total']}, Bayar: Rp{transaksi['bayar']}, Kembalian: Rp{transaksi['kembalian']}")
