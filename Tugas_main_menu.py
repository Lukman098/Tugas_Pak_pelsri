from queue import Queue

def MainMenu():
    q = Queue(maxsize=3);
    pilih = "y";
    
    while pilih.lower() == "y":
        print("\nMenu Queue");
        print("1. Masukkan data");
        print("2. Hapus data");
        print("3. Panjang queue");
        print("============================");
        
        pilihan = input("Masukkan pilihan: ");
        
        if pilihan == "1":
            if q.full():
                print("Queue sudah penuh!.");
            else:
                obj = input("Objek yang ingin ditambahkan: ");
                q.put(obj);
                print(f"Object '{obj}' telah ditambahkan.");
                
        elif pilihan == "2":
            if q.empty():
                print("Queue kosong .");
            else:
                popped = q.get();
                print(f"Object '{popped}' dihapus.");
                
        elif pilihan == "3":
            print("Panjang dari queue saat ini:", q.qsize());
            print("Kapasitas maksimal queue:", q.maxsize);
        else:
            print("Pilihan tidak valid.");

        pilih = input("Apakah ingin kembali ke menu? (y/n): ");

if __name__ == "__main__":
    MainMenu()
