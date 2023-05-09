import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>About Us</h1>", unsafe_allow_html=True)

st.write(" ")

#Nurandita
st.markdown("<h2 style='text-align: center; color: raisin black;'>Nurandita Aranda Putri</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image1 = Image.open('Resource/image/Profile/Nurandita.jpg')
  st.image(image1)
with col3:
  st.write(" ")  
st.write("Seorang mahasiswi yang nggak bisa hidup sehari aja tanpa laptopnya")
st.write("email: nuranditaap6@gmail.com")
st.write("instagram: [@nurandita_a.p](https://www.instagram.com/nurandita_a.p/)")

#Era
st.markdown("<h2 style='text-align: center; color: raisin black;'>Puspita Erawati</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image2 = Image.open('Resource/image/Profile/Era.jpg')
  st.image(image2)
with col3:
  st.write(" ")
st.write("Sujud syukur akhirnya proyek ini kelar juga")
st.write("email: puspita.e.s030304@gmail.com")
st.write("Instagram: [@k.p.era](https://www.instagram.com/k.p.era/)")

#Firli
st.markdown("<h2 style='text-align: center; color: raisin black;'>Nabila Firliana Maudy</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image3 = Image.open('Resource/image/Profile/Nabila.jpg')
  st.image(image3)
with col3:
  st.write(" ")
st.write("Tiada hari tanpa musik")
st.write("email: nabilamaudy12345@gmail.com")
st.write("instagram: [@nabila_firli1212](https://www.instagram.com/nabila_firli1212/)")

#Uswa
st.markdown("<h2 style='text-align: center; color: raisin black;'>Uswatun Hasanah</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image4 = Image.open('Resource/image/Profile/Uswa.jpg')
  st.image(image4)
with col3:
  st.write(" ")
st.write("Mahasiswi yang pulang setiap jumat")
st.write("email: uswahasanah0903@gmail.com")
st.write("instagram: [@bmsn_unf](https://www.instagram.com/bmsn_unf/)")

#Demas
st.markdown("<h2 style='text-align: center; color: raisin black;'>Muhammad Demas Pandya Dharmesta</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
  st.write(" ")
with col2:
  image5 = Image.open('Resource/image/Profile/Demas.jpg')
  st.image(image5)
with col3:
  st.write(" ")
st.write("Nama saya Demas. Saya lahir tanggal 17 Juli 2004 di Bekasi. Umur saya sekarang 19 tahun. Saat ini, saya sedang menempuh pendidikan di Politeknik AKA Bogor.")
st.write("email: demasdharmesta@gmail.com")
st.write("instagram: [@demasdharmesta](https://www.instagram.com/demasdharmesta/)")
