class Transaction:
    def __init__(self):
        """
        Inisialisasi objek transaksi dengan atribut items, yaitu list kosong untuk menyimpan item-item yang akan dibeli.
        """
        self.items = []

    def add_item(self, item):
        """
        Fungsi untuk menambahkan item ke dalam list items.

        Parameter:
        item (list): List yang berisi nama item, jumlah item, dan harga per item.

        Output:
        Pesan yang memberitahu bahwa item sudah berhasil ditambahkan ke dalam list items.
        """
        self.items.append(item)
        print("-" * 60)
        print(f"{item} telah berhasil ditambahkan ke keranjang")
        self.show_items()

    def update_item_name(self, old_name, new_name):
        """
        Fungsi untuk mengganti nama item pada list items.

        Parameter:
        old_name (string): Nama item yang akan diganti.
        new_name (string): Nama baru untuk item yang akan diganti.

        Output:
        Pesan yang memberitahu bahwa nama item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name

        print(f"Item {old_name} telah berhasil diubah menjadi {new_name} ")
        self.show_items()

    def update_item_qty(self, name, qty):
        """
        Fungsi untuk mengganti jumlah item pada list items.

        Parameter:
        name (string): Nama item yang ingin diubah jumlahnya.
        new_qty (int): Jumlah baru untuk item yang ingin diubah.

        Output:
        Pesan yang memberitahu bahwa jumlah item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == name:
                item[1] = qty

        print(f"Jumlah {name} telah diubah menjadi {qty} ")
        self.show_items()

    def update_item_price(self, name, price):
        """
        Fungsi untuk mengganti harga per item pada list items.

        Parameter:
        name (string): Nama item yang ingin diubah harganya.
        new_price (int): Harga per item yang baru untuk item yang ingin diubah.

        Output:
        Pesan yang memberitahu bahwa harga per item sudah berhasil diubah.
        """
        for item in self.items:
            if item[0] == name:
                item[2] = price

        print(f"Harga {name} telah diubah menjadi {price} ")
        self.show_items()

    def delete_item(self, name):
        """
        Fungsi untuk menghapus item dari list items.

        Parameter:
        name (string): Nama item yang ingin dihapus dari list items.

        Output:
        Pesan yang memberitahu bahwa item sudah berhasil dihapus dari list items.
        """
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)

        print(f"Anda telah menghapus : {name} ")        # print item yang dibeli
        self.show_items()

    def reset_transaction(self):
        """
        Fungsi untuk menghapus semua item dari list items.

        Output:
        Pesan yang memberitahu bahwa semua item sudah berhasil dihapus dari list items.
        """
        self.items = []

        print(f"Anda telah mereset transaksi ini. Semua item telah dihapus.")

    def check_order(self):
        """
        Fungsi untuk mengecek apakah input data sudah benar atau tidak.

        Output:
        Jika semua input data sudah benar, fungsi akan mengeluarkan pesan "Pemesanan Anda Sudah Benar".
        Jika terdapat kesalahan pada input data, fungsi akan mengeluarkan pesan "Terdapat kesalahan input data".
        Jika input data sudah benar, fungsi akan mengeluarkan output berupa tabel berisi item, jumlah item,
        harga satuan, dan total harga.
        """
        error = False
        for item in self.items:
            if (None, "", 0) in item or not all(item):
                error = True
        if error:
            print("Terdapat kesalahan input data")
        else:
            print("Pesanan Anda Sudah Benar")
            self.show_items()

    def show_items(self):
        """
        Fungsi untuk menampilkan nama item, jumlah item, harga satuan dan total harga

        Output:
        Tabel nama item, jumlah item, harga satuan dan total harga
        """
        print("=" * 60)
        print("Item\t\tJumlah\tHarga Satuan\tTotal Harga")
        print("-" * 60)
        for item in self.items:
            total_price = item[1] * item[2]
            print("{}\t\t{}\t{}\t\t{}".format(item[0], item[1], item[2], total_price))
        print("-" * 60)

    def total_price(self):
        """
        Fungsi untuk menghitung total harga dari seluruh item pada list items.
        Menghitung diskon dengan ketentuan yang telah ditetapkan sebelumnya.

        Output:
        Total harga dari seluruh item pada list items.
        """
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        if total > 500000:
            discount = total * 0.1
        elif total > 300000:
            discount = total * 0.08
        elif total > 200000:
            discount = total * 0.05
        else:
            discount = 0
        total -= discount
        print("Total Harga: {}\nDiskon: {}\nTotal yang harus dibayar: {}".format(total + discount, discount, total))