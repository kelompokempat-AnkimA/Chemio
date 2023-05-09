import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Chemio"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Chemio</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Student's Chemical Reference</h2>", unsafe_allow_html=True)
st.write("---")
st.subheader("Tanya apa saja ke Fayans")


col1, col2 = st.columns(2)

with col1:
  image1 = Image.open('Resource/image/Main/Fayans1.png')
  st.image(image1)
with col2:
    opsi1 = st.button("Asal mula nama Fayans dari mana?")
    opsi2 = st.button("Curhat boleh?")
    opsi3 = st.button("Disini ada fitur apa aja, Fayans?")
    opsi4 = st.button("Kayaknya ada yang nge-bug deh, Fayans")
    opsi5 = st.button("Mau kenalan sama yang buat ini dong")

if opsi1:
    st.write("Nama Fayans diambil dari argentometri metode Fayans karena tali perak yang Fayans gunakan, selain itu juga karena hidung dan kaki Fayans yang berwarna merah muda")
elif opsi2:
    st.write(
        """
        Wah, boleh banget kak!
        
        kakak bisa langsung chat aja akun Fayans [disini](https://wa.me/message/TULJ2JKFOI4HN1). Fayans selalu siap dengerin keluh kesah kakak.
        """)
elif opsi3:
    st.write(
        """
        Oke oke, Fayans kasih tau di sini ada apa aja
        
        **1.	Materi**
        
        Di halaman materi yang diberi nama "Gaia Library" ini isinya materi-materi mata kuliah kimia dasar, analisis jenis, titrimetri, kimia organik, dan kimia dasar.
        """)
    imageF1 = Image.open('Resource/image/Main/Materi1.png')
    st.image(imageF1)
    st.write(
        """
        **2.	Quiz**
        
        Di halaman bernama "Chemio Test" ini Kakak bisa mencoba mengerjakan soal-soal untuk mengasah kemampuan dan pemahaman kakak terhadap materi-materi yang sudah dipelajari.
        """)
    imageF2 = Image.open('Resource/image/Main/Quiz.png')
    st.image(imageF2)
    st.write(
        """
        **3.	Kalkulator**
        
        Nah, di halaman "Calchemio" ini kakak bisa dengan mudah menghitung molalitas, molaritas, % kadar, normalitas, PPM, dan PPB sesuai dengan data yang dimiliki.
        """)
    imageF3 = Image.open('Resource/image/Main/Kalkulator.png')
    st.image(imageF3)
    st.write(
        """
        **4.	Intermezzo**
        
        Di sini kakak bisa membaca info-info menarik tentang unsur-unsur kimia untuk mengisi waktu luang kakak.
        """)
    imageF4 = Image.open('Resource/image/Main/Intermezzo.png')
    st.image(imageF4)
elif opsi4:
    st.write(
        """
        Wah, kakak bisa langsung kirim saja keluhan kakak di halaman "Report" yang ada di sidebar.
        
        Sini kak, Fayans arahin biar nggak kesasar
        """)
    image1 = Image.open('Resource/image/Main/Tutor1_1.png')
    st.image(image1)
    image2 = Image.open('Resource/image/Main/Tutor1_2.png')
    st.image(image2)
    st.write("Kakak langsung isi aja nama, email, dan keluhan kakak di kotak yang udah disediain. Good luck kak!")
elif opsi5:
    st.write("Wah, ayo ayo sini kak!")
    image1 = Image.open('Resource/image/Main/About_Us.png')
    st.image(image1)
    st.write("Nah, dari sini kakak bisa ngehubungin langsung email dan instagramnya. Aku titip salam buat mereka ya kak!!")
else:
    st.write(
        """
        Halo namaku fayans!
        
        Aku yang akan membantu kakak menggunakan aplikasi ini, jadi...apa ada yang perlu Fayans bantu?
        """)
    
st.sidebar.success("Select a page above")
