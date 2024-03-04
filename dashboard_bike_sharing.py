import streamlit as st
from PIL import Image

st.title("Analisis Data Pengguna Sepeda-Bersama")
tab1, tab2 = st.tabs(["Definisi", "Hasil Analisis"])
 
image=Image.open('Number of Users Between Seasons.png')
image2=Image.open('Number of Users in Every Windspeed.png')
image3=Image.open('Bike.jpg')

with tab1:
    st.header('Pengguna Rental Sepeda-Bersama')
    st.image(image3, caption='Source: https://images.app.goo.gl/tbzY66fGxXXaJhpq6')
    st.write(
            """Sistem rental Bike-Sharing (Sepeda-Bersama) adalah sebuah penyewaan sepeda dengan 
            teknologi yang secara otomatis dapat menyesuaikan pemakaian. Melalui sistem ini, setiap 
            pengguna dapat dengan mudah melakukan penyewaan untuk melakukan mobilisasi disekitar
             Selain aplikasi dunia nyata yang menarik dari sistem berbagi sepeda, karakteristik 
             data yang dihasilkan oleh sistem-sistem ini membuatnya menarik untuk penelitian. 
             Berbeda dengan layanan transportasi lain seperti bus atau kereta bawah tanah, 
             durasi perjalanan, posisi keberangkatan, dan kedatangan secara eksplisit dicatat 
             dalam sistem-sistem ini. Fitur ini mengubah sistem berbagi sepeda menjadi jaringan 
             sensor virtual yang dapat digunakan untuk mendeteksi mobilitas di kota. Oleh karena itu, 
             diharapkan bahwa sebagian besar peristiwa penting di kota dapat dideteksi melalui pemantauan data ini.
             """)
 
with tab2:
    st.header("Hasil Analisis Data Pengguna Sepeda-Bersama")
    st.image(image, caption='Angka pengguna berdasarkan musim')
    st.subheader("Pada musim apa pengguna sepeda bersama cenderung lebih dominan?")
    st.write(
            """Berdasarkan data dan line chart yang terlampir, dapat disimpulkan bahwa pengguna
              lebih dominan menggunakan sepeda bersama pada musim gugur dan turun secara signifikan 
              pada musim dingin. Musim gugur menjadi titik puncak dalam line chart telah disajikan.
            """
        )

    st.subheader("Apakah kecepatan udara memengaruhi jumlah pengguna?")
    st.image(image2, caption='Angka pengguna berdasarkan kecepatan udara')
    st.write(
            """Berdasarkan data yang ada, dapat disimpulkan bahwa kecepatan udara mmemengaruhi pengguna.
              Pengguna sepeda bersama cenderung menggunakan rental pada kecepatan udara sebesar 0.1 hingga 
              0.4 mph, selebihnya secara signifikan pengguna berkurang. Di sisi lain, pengguna justru paling 
              banyak menggunakan sepeda bersama pada saat kecepatan udara yang tenang sekitar 0.1 hingga 0.2 mph.
            """
        )