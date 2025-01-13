import streamlit as st

# Data Keranjang
cart = []

# Fungsi untuk menambah barang ke keranjang
def add_to_cart(product, price):
    cart.append({"product": product, "price": price})

# Judul Aplikasi
st.title("Aplikasi Kasir Toko Baju")

# Input Produk
product_name = st.text_input("Nama Produk")
product_price = st.number_input("Harga Produk", min_value=0.0, format="%.2f")

if st.button("Tambahkan ke Keranjang"):
    add_to_cart(product_name, product_price)
    st.success(f"{product_name} berhasil ditambahkan ke keranjang dengan harga Rp{product_price:.2f}!")

# Menampilkan Keranjang
st.subheader("Keranjang")
if cart:
    for item in cart:
        st.write(f"{item['product']} - Rp{item['price']:.2f}")
else:
    st.write("Keranjang kosong")

# Total
if cart:
    total = sum(item['price'] for item in cart)
    st.subheader(f"Total: Rp{total:.2f}")
    if st.button("Proses Pembayaran"):
        st.success("Pembayaran berhasil diproses!")
else:
    st.subheader("Silakan tambahkan produk ke keranjang")

