import streamlit as st

class Baju:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total_harga(self):
        return self.harga * self.jumlah

class Kasir:
    def __init__(self):
        self.daftar_baju = []

    def tambah_baju(self, baju):
        self.daftar_baju.append(baju)

    def hitung_total(self):
        total = 0
        for baju in self.daftar_baju:
            total += baju.total_harga()
        return total

    def tampilkan_struk(self):
        struk = "Struk Belanja\n" + "-"*27 + "\n"
        for baju in self.daftar_baju:
            struk += f"{baju.nama}: {baju.jumlah} x {baju.harga} = {baju.total_harga()}\n"
        struk += "-"*27 + "\n"
        struk += f"Total: {self.hitung_total()}\n"
        return struk

def main():
    st.title("Program Kasir Baju")
    kasir = Kasir()

    st.subheader("Input Data Baju")
    nama = st.text_input("Masukkan nama baju")
    harga = st.number_input("Masukkan harga baju", min_value=0.0, step=0.01)
    jumlah = st.number_input("Masukkan jumlah baju", min_value=1, step=1)

    if st.button("Tambah Baju"):
        if nama and harga and jumlah:
            baju = Baju(nama, harga, jumlah)
            kasir.tambah_baju(baju)
            st.success(f"{nama} berhasil ditambahkan!")
        else:
            st.error("Silakan lengkapi semua data baju!")

    if st.button("Tampilkan Struk"):
        struk = kasir.tampilkan_struk()
        st.text(struk)

if __name__ == "__main__":
    main()
