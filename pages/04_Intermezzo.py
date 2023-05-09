import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>Intermezzo</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Isi waktumu dengan membaca info-info menarik tentang unsur kimia</h2>", unsafe_allow_html=True)


image1 = Image.open('Resource/image/Intermezzo/tabel-periodik.jpg')
st.image(image1,caption = "Sumber: scincenotes.org")

optiongolongan = st.selectbox(
  "Pilih materi yang kamu mau",
  ("--- Pilih Golongan ---", "Golongan I", "Golongan II","Golongan III","Golongan IV","Golongan V","Golongan VI","Golongan VII", "Golongan VIII"))

#Golongan I
if optiongolongan == "Golongan I":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Hidrogen (H)")
    opsi5 = st.button("Rubidium (Rb)")
  with col2:
    opsi2 = st.button("Litium (Li)")
    opsi6 = st.button("Sesium (Cs)")
  with col3:
    opsi3 = st.button("Natrium (Na)")
    opsi7 = st.button("Fransium (Fr)")
  with col4:
    opsi4 = st.button("Kalium (K)")
  if opsi1:
      st.markdown("<h2 style='text-align: center; color: raisin black;'>Hidrogen (H)</h2>", unsafe_allow_html=True)
      st.write(
        """
Ar : 1

Nomor Atom: 1

Konfigurasi Atom: 1S^1

Banyak ditemukan: Hidrogen ada dimana saja, dan merupakan unsur yang paling banyak ditemukan di alam semesta

Golongan: alkali

Wujud: Gas

Pada suhu dan tekanan standar, hidrogen tidak berwarna, tidak berbau, bersifat non-logam, bervalensi tunggal, dan merupakan gas diatomik yang paling gampang terbakar
""")
  elif opsi2:
        st.markdown("<h2 style='text-align: center; color: black;'>Lithium (LI)</h2>", unsafe_allow_html=True)
        st. write (
            """
Ar : 7

Nomor Atom: 3

Konfigurasi Atom: 1S^2 2s^1

Banyak ditemukan: Litium tidak pernah terdapat sebagai unsur bebas di alam, tapi hanya sebagai senyawa (biasanya ionik)
Golongan: Logam Alkali

Wujud: Logam lunak berawarna keperakan

Cara Pembuatan: Logam litium dihasilkan melalui elektrolisis dari campuran leburan 55% litium klorida dan 45% kalium klorida pada suhu sekitar 450 °C

litium sangat reaktif dan terkorosi dengan cepat dan menjadi hitam di udara yang lembap.
""")
  elif opsi3:
        st.markdown("<h2 style='text-align: center; color: black;'>Natrium (Na)</h2>", unsafe_allow_html=True)
        st.write(
          """
Ar : 23

Nomor Atom:11

Konfigurasi Atom: 1S^2 2s^2 2P^6 3S^1

Banyak ditemukan: Natrium adalah unsur keenam paling melimpah dalam kerak bumi, dan terdapat di banyak mineral seperti feldspar, sodalit dan halit

Golongan: Logam Alkali

Wujud: logam lunak, putih keperakan

Na sangat reaktif, apinya berwarna kuning, beroksidasi dalam udara, dan bereaksi kuat dengan cairan, sehingga wajib disimpan dalam minyak. Sebab sangat reaktif, natrium hampir tidak pernah ditemukan dalam bentuk unsur murni
""")
  elif opsi4:
         st.markdown("<h2 style='text-align: center; color: black;'>Kalium (K)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar : 39

Nomor Atom: 19

Konfigurasi Atom: 1S^2 2s^2 2P^6 3S^2 3P^6 4S^1

Banyak ditemukan: Kalium di alam hanya terdapat pada garam ionik.

Golongan: Logam Alkali

Wujud: logam lunak berwarna putih keperakan

unsur K  teroksidasi dengan cepat di udara dan bereaksi hebat dengan air, menghasilkan panas yang cukup untuk menyalakan hidrogen yang dipancarkan dalam reaksi dan terbakar dengan api berwarna ungu. Ia ditemukan terlarut dalam air laut
""")
  elif opsi5:
         st.markdown("<h2 style='text-align: center; color: black;'>Rubidium (Rb)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar : 85

Nomor Atom: 37

Konfigurasi Atom:5s1

Banyak ditemukan: rubidium hadir dalam jumlah signifikan pada mineral lain seperti lepodite (1,5%), pollucite, dan carnallite

Golongan: Logam Alkali

Wujud: logam abu-abu keputihan yang sangat lunak

Cara pembuatan: memperoleh Rubidium di lakukan melalui metode reduksi

Rubidium tidak dapat disimpan di bawah oksigen atmosfer, karena reaksi eksoterm yang sangat tinggi akan terjadi, kadang-kadang bahkan mengakibatkan logam ini terbakar.
""")
  elif opsi6:
         st.markdown("<h2 style='text-align: center; color: black;'>Cesium (Cs)</h2>", unsafe_allow_html=True)
         st.write(
           """
Ar: 133

Nomor Atom: 55

Konfigurasi Elaktron:[Xe] 6s1

Banyak ditemukan: cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.(1,5%), pollucite, dan carnallite

Golongan: Logam Alkali

Wujud: cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.

cesium sendiri merupakan elemen yang secara alami ditemukan dalam jumlah kecil di dalam batu, tanah, dan debu.
""")
  elif opsi7:
       st.markdown("<h2 style='text-align: center; color: black;'>Fransium (Fr)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 223

Nomor Atom: 87

Konfigurasi Elektron:[Rn] 7s1

Banyak ditemukan: Fr adalah hasil peluruhan alfa dariAc dan dapat ditemukan dalam jumlah kecil dalam mineral uranium

Golongan: Logam Alkali

Wujud: Logam berwarna merah bata

Cara pembuatan: Fransium dapat disintesis melalui reaksi fusi ketika target emas-197 dibombardir dengan seberkas atom oksigen-18 dari akselerator linear dalam proses yang awalnya dikembangkan di departemen fisika Universitas Negeri New York di Stony Brook pada tahun 1995.
""")
      
#Golongan II
if optiongolongan == "Golongan II":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Berilium (Be)")
    opsi5 = st.button("Barium (Ba)")
  with col2:
    opsi2 = st.button("Magnesium (Mg)")
    opsi6 = st.button("Radium (Ra)")
  with col3:
    opsi3 = st.button("Kalsium (Ca)")
  with col4:
    opsi4 = st.button("Stronsium (Sr)")
  if opsi1:
      st.markdown("<h2 style='text-align: center; color: raisin black;'>Berylium (Be)</h2>", unsafe_allow_html=True)
      st.write(
        """
Ar: 9

Nomor Atom: 4

Konfigurasi Elektron:[He] 2s²

Banyak ditemukan:Beryllium dapat ditemukan dalam beberapa mineral, seperti beryl, kriptoklas, dan epidot

Golongan: Logam Alkali

Wujud: logam alkali tanah berwarna abu-abu-baja yang kuat

Batu permata terkenal yang mengandung berilium tinggi adalah beril (akuamarin, zamrud) dan krisoberil.
""")
  elif opsi2:
       st.markdown("<h2 style='text-align: center; color: black;'>Magnesium (Mg)</h2>", unsafe_allow_html=True)
       st.write(
        """
Ar: 24

Nomor Atom: 12

Konfigurasi Elektron:[Ne] 3s^2

Banyak ditemukan:paling melimpah di alam semesta, biasanya banyak terakumulasi pada batuan beku

Golongan: Logam alkali tanah

Wujud: padatan abu-abu mengkilap 

Magnesium diproduksi dalam penuaan bintang besar dari penambahan sekuensial tiga inti helium ke inti karbon. 
""")
  elif opsi3:
       st.markdown("<h2 style='text-align: center; color: black;'>Kalsium (Ca)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 40

Nomor Atom: 20

Konfigurasi Elektron:[Ar] 4s^2

Banyak ditemukan: Kalsium paling banyak ditemukan di batu kapur

Golongan: Logam alkali tanah

Wujud: Dalam bentuk logam, kalsium berwarna perak hingga abu-abu yang seiring waktu bisa berubah warna menjadi kuning pucat

Sifat fisik dan kimianya paling mirip dengan homolognya yang lebih berat, stronsium dan barium. Ia adalah unsur paling melimpah kelima di kerak Bumi, dan logam paling melimpah ketiga, setelah besi dan aluminium
""")
         
  elif opsi4:
       st.markdown("<h2 style='text-align: center; color: black;'>Stronsium (Sr)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 87

Nomor Atom: 38

Konfigurasi Elektron:[Kr] 5s^2

Banyak ditemukan: Stronsium banyak terdapat di alam sebagai mineral Celestite (SrSO4) dan Strontianite (SrCO3)

Golongan: Logam alkali tanah

Wujud: Logam yang tekstur yang lembut dan berwarna putih

Logam stronsium membentuk lapisan oksida gelap ketika terkena udara, Titik lebur (777 °C) dan didihnya (1377 °C) lebih rendah daripada kalsium (masing-masing 842 °C dan 1484 °C)
""")
  elif opsi5:
       st.markdown("<h2 style='text-align: center; color: black;'>Barium (Ba)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 137

Nomor Atom: 56

Konfigurasi Elektron: [Xe] 6s^2

Banyak ditemukan: Barium tidak pernah ditemukan di alam sebagai unsur bebas karena reaktivitas kimianya yang tinggi.

Golongan: Logam alkali tanah

Wujud: logam lunak putih keperakan, dengan sedikit nuansa emas saat ultra m
""")

         
  elif opsi6:
       st.markdown("<h2 style='text-align: center; color: black;'>Radium (Ra)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 226

Nomor Atom: 88

Konfigurasi Elektron:[Rn] 7s2

ditemukan: Radium, dalam bentuk radium klorida, ditemukan oleh Marie dan Pierre Curie pada tahun 1898 dari bijih yang ditambang di Jáchymov. Mereka mengekstraksi senyawa radium dari uraninit dan menerbitkan penemuan tersebut di Akademi Sains Prancis lima hari kemudian

Golongan: Logam alkali tanah

Wujud:Radium murni berwarna putih keperakan

Radium mudah bereaksi dengan nitrogen (daripada oksigen) saat terpapar udara, membentuk radium nitrida (Ra3N2) dengan lapisan permukaan hitam
""")
  

#Golongan III
if optiongolongan == "Golongan III":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Boron (B)")
    opsi5 = st.button("Talium (Tl)")
  with col2:
    opsi2 = st.button("Alumunium (Al)")
    opsi6 = st.button("ununtrium (Uut)")
  with col3:
    opsi3 = st.button("Galium (Ga)")
  with col4:
    opsi4 = st.button("Indium (In)")
  if opsi1:
      st.markdown("<h2 style='text-align: center; color: raisin black;'>Boron (B)</h2>", unsafe_allow_html=True)
      st.write(
         """
Ar: 10

Nomor Atom: 5

Konfigurasi Elektron:[He] 2s²2p¹

ditemukan: Mineral boron secara alami terdapat di dalam sayuran, buah, atau kacang.

Golongan: non Logam 

Wujud:bubuk kecoklatan
""")
  elif opsi2:
       st.markdown("<h2 style='text-align: center; color: black;'>Alumunium (Al)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 27

Nomor Atom: 13

Konfigurasi Elektron:[Ne] 3s^ 3p^1

ditemukan: banyak ditemukan di perut bumi

Golongan: Logam berat

Wujud: padatan metalik abu-abu keperakan
""")
      
  elif opsi3:
       st.markdown("<h2 style='text-align: center; color: black;'>Galium (Ga))</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 69

Nomor Atom: 31

Konfigurasi Elektron:[Ar] 4s^2 3d^10 4p^1

ditemukan: banyak ditemukan di perut bumi

Golongan: Logam miskin

Wujud: padatan biru keperakan
""")
  elif opsi4:
       st.markdown("<h2 style='text-align: center; color: black;'>Indium (In)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 204

Nomor Atom: 81

Konfigurasi Elektron:[Xe] 4f^14 5d^10 6s^2 6p^1

ditemukan: banyak ditemukan di perut bumi

Golongan: Logam 

Wujud: padatan abu-abu berkilau keperakan
""")
  elif opsi5:
       st.markdown("<h2 style='text-align: center; color: black;'>Talium (Tl)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 114

Nomor Atom: 49

Konfigurasi Elektron:[Kr] 4d^10 5s^2 5p^1

ditemukan: banyak ditemukan di perut bumi

Golongan: Logam 

Wujud: padatan putih keperakan
""")
  elif opsi6:
       st.markdown("<h2 style='text-align: center; color: black;'>ununtrium (Uut)</h2>", unsafe_allow_html=True)
       st.write(
         """
Ar: 286

Nomor Atom: 113

Konfigurasi Elektron:[Rn] 5f^14 6d^10 7s^2 7p^1

ditemukan: banyak ditemukan di perut bumi

Golongan: Logam 

Wujud: 
unsur ini jarang ditemukan karena hanya dibuat dalam jumlah sangat kecil dan dapat membusuk dalam hitungan detik
""")
        
#Golongan IV
if optiongolongan == "Golongan IV":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Karbon (C)")
    opsi5 = st.button("Timbal (Pb)")
  with col2:
    opsi2 = st.button("Silikon (Si)")
    opsi6 = st.button("flerovium (Fl)")
  with col3:
    opsi3 = st.button("Germanium (Ge)")
  with col4:
    opsi4 = st.button("Timah (Sn)")
  if opsi1:
     st.markdown("<h2 style='text-align: center; color: raisin black;'>Karbon(C)</h2>", unsafe_allow_html=True)
     st.write(
        """
Ar : 12

Nomor Atom: 6

Konfigurasi Atom: 1s^2 2s^2 2p^2

Banyak ditemukan: Hidrogen ada dimana saja, dan merupakan unsur yang paling banyak ditemukan di alam semesta

Golongan: non-logam

Wujud: Karbon di atmosfer berbentuk karbon monoksida,karbon dioksida, dan metana.

Karbon merupakan konstituen kunci dari mineral karbonat dan hidrogen karbonat yang mana ditemukan di laut. Info mengejutkan bahwa 22,8% tubuh manusia terdiri dari karbon. Karbon biasa juga disebut arang.
""")
  elif opsi2:
       st.markdown("<h2 style='text-align: center; color: black;'>Silikon(Si)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 28

Nomor Atom: 14

Konfigurasi Atom: [Ne] 3s² 3p²

Banyak ditemukan: Silikon dapat dijumpai di kerak bumi dengan konsentrasi 28%. 

Golongan: non-logam

Wujud: -

Konsentrasi silicon pada air laut bervariasi antara 30 ppb (part per billion) di permukaan air laut hingga 2000 ppb di kedalaman. Debu silikon sering terjadi di atmosfer bumi. Mineral silikat merupakan mineral yang paling banyak ditemukan di alam. Di tubuh manusia, silikon ada sekitar 14,3%.
""")
  elif opsi3:
       st.markdown("<h2 style='text-align: center; color: black;'>Germanium(Ge)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 72,61

Nomor Atom: 32

Konfigurasi Atom: [Ar] 3d¹⁰ 4s² 4p²

Banyak ditemukan: Germanium ditemukan di tanah dengan rata-rata konsentrasi 1 ppm. Di air laut, germanium ada sekitar 0,5 ppt. Germanium dijumpai di tubuh manusia dengan konsentrasi 72,44 ppb.

Golongan: non-logam

Wujud: -

Germanium menyusun sekkitar 2 ppm kerak bumi. Germanium merupakan unsur paling melimpah urutan ke 52.
""")
  elif opsi4:
       st.markdown("<h2 style='text-align: center; color: black;'>Timah(Sn)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 118,71

Nomor Atom: 50

Konfigurasi Atom: [Ar] 3d¹⁰ 4s² 4p²

Banyak ditemukan: Timah(IV) oksida sering dijumpai di tanah dengan konsentrasi 0,1 hinggga 300 ppm.

Golongan: non-logam

Wujud: -

Timah ada di kerak bumi dengan kelimpahan sekitar 2 ppm. Timah merupakan unsur paling melimpah nomor 49. Rata-rata timah ditemukan dengan konsentrasi 1 ppm. 
""")
  elif opsi5:
       st.markdown("<h2 style='text-align: center; color: black;'>Timbal(Pb)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 207,2

Nomor Atom: 82

Konfigurasi Atom: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p²

Banyak ditemukan: Timbal dijumpai di air laut dengan konsentrasi sekitar 2 ppt. Timbal menyusun 0,17% di tubuh manusia.

Golongan: non-logam

Wujud: -

keberadaan timbal di bumi adalah sekitar 14 ppm. Timbal merupakan unsur paling melimpah ke-36. Di tanah rata-rata timbal ada sekitar 23 ppm. Tetapi jumlah tersebut dapat meningkat hingga 2000 ppm (2%) di drkat pertambangan timbal. 
""")
  elif opsi6:
       st.markdown("<h2 style='text-align: center; color: black;'>Flerofium( FI)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 289

Nomor Atom: 114

Konfigurasi Atom: [Rn] 5f^14 6d^10 7s^2 7p^2

Banyak ditemukan: -

Golongan: non-logam

Wujud: -

Flerofium hanya terdapat di akselerator partikel. sebelumnya bernama Ununquadium adalah unsur kimia buatan dalam sistem periodik unsur yang memiliki lambang Fl (sebelumnya Uuq) dan nomor atom 114. Flevorium diduga memiliki sifat-sifat gas mulia ketimbang sifat-sifat logam. Pada tanggal 29 Mei 2012 nama Flerovium telah disetujui oleh IUPAC setelah sebelumnya menggunakan nama Ununquadium. Nama diambil dari Flerov Laboratory of Nuclear Reactions di Dubna, Rusia, tempat di mana unsur ini dibuat.Oleh karena itu unsur tersebut tidak dapat digambarkan ataupun hanya berbentuk sebuah jumlah kandungan dari unsur tersebut.
""")
           
            
          
    
#Golongan V
if optiongolongan == "Golongan V":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Nitrogen (N)")
    opsi5 = st.button("Bismut (Bi)")
  with col2:
    opsi2 = st.button("Fosfor (P)")
    opsi6 = st.button("Ununpentium (Uup)")
  with col3:
    opsi3 = st.button("Arsenik (As)")
  with col4:
    opsi4 = st.button("Antimon (Sb)")
  if opsi1:
     st.markdown("<h2 style='text-align: center; color: raisin black;'>Nitrogen(N)</h2>", unsafe_allow_html=True)
     st.write(
        """
Ar : 14

Nomor Atom: 7

Konfigurasi Atom: [He] 2s^2 2p^3

Banyak ditemukan:  Nitrogen mengisi 78,08 persen atmosfir Bumi dan terdapat dalam banyak jaringan hidup.

Golongan: non-logam

Wujud: Gas tanpa warna,tidak berbau dan tidakberasa.

Nitrogen adalah zat non yang logam tidak berwarna dan tidak berbau, dengan elektronegatifitas 3.0. Mempunyai 5 elektron di kulit terluarnya. Ikatan rangkap tiga dalam molekul gas nitrogen (N2) adalah yang terkuat. Nitrogen mengembun pada suhu 77K (-196oC) pada tekanan atmosfer dan membeku pada suhu 63K (-210oC)
""")
  elif opsi2:
       st.markdown("<h2 style='text-align: center; color: black;'>Fosfor(P)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 30,97

Nomor Atom: 15

Konfigurasi Atom: : 1s2 2s2 2p6 3s2 3p3.

Banyak ditemukan: tidak terdapat bebas, banyak sekali di kerak bumi dalam kombinasi dengan unsur lain dan juga terdapat dalam mineral. 

Golongan: non-logam

Wujud: padatan lunak, lembut, berwarna putih, serbuk merah kecoklatan, atau padatan coklat

Kegunaan

• Membentu pertumbuhan protein dan miniral yg sangat tinggi bagi tanaman. Bertugas mengedarkan energi keseluruh bagian tanaman.

• Merangsang pertumbuhan dan perkembangan akar.

• Mempercepat membungaan dan pembuahan tanaman.

• Mempercepat pemasakan biji dan buah.

Pembuatan

• Dalam prosesnya, Ca3(PO4)2 dicampur dengan karbon dan silika (SiO2) pada temperature 1400⁰C - 1500⁰C (dengan bunga api listrik). SiO2 bereaksi dengan Ca3(PO4)2 pada temperature tersebut mengahasilkan P4O10 (g).
  Reaksinya sebagai berikut :
    
                             2 Ca3(PO4)2 (l)  + 6 SiO2 (l) → 6 CaSiO3 (l)  + P­4O10 (g)

• Kemudian , P­4O10 (g) direduksi dengan karbon , reaksinya sebagai berikut :
                             
                             P­4O10 (g)  + C (s) → P4 (g)  + 10 CO2 (g)

• P4­ (g) yang terjadi dikristalkan dan disimpan di dalam CS2 cair atau di dalam air. Hal itu guna menghindari terjadinya oksidasi dengan oksigen  dari udara yang cepat terjadi pada temperatur 30⁰C berupa nyala fosfor. P4 hasil pengolahan merupakan salah satu bentuk alotropi fosfor, yaitu fosfor putih.
""")
  elif opsi3:
       st.markdown("<h2 style='text-align: center; color: black;'>Arsen (As)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 208,98

Nomor Atom: 83

Konfigurasi Atom: [Ar] 3d¹⁰ 4s² 4p²

Banyak ditemukan: 

Golongan: non-logam

Wujud: -Non-logam yang berlapis berwarna abu-abu, rapuh

Logam ini bewarna abu-abu, sangat rapuh, kristal dan semi-metal benda padat. Ia berubah warna dalam udara,dan ketika dipanaskan teroksida sangat cepat menjadi arsen oksida dengan baubawang. Arsen dan senyawa-senyawanya sangat beracun.

Kegunaan (As)

• Berbagai macam insektisida dan racun

• material semikonduktor penting dalam sirkuit terpadu. Sirkuit dibuat menggunakan komponen ini lebih cepat tapi juga lebih mahal daripada terbuat dari silikon.
""")
  elif opsi4:
       st.markdown("<h2 style='text-align: center; color: black;'>Antimon (Sb)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 121,76

Nomor Atom: 51

Konfigurasi Atom: [Kr] 4d^10 5s^2 5p^3

Banyak ditemukan: Timah(IV) oksida sering dijumpai di tanah dengan konsentrasi 0,1 hinggga 300 ppm.

Golongan: non-logam

Wujud: kristal padat yang rapuh.

Antimon merupakan unsur dengan warna putih keperakan, berbentuk kristal padat yang rapuh. Daya hantar listrik (konduktivitas) dan panasnya lemah. Zat ini menyublim (menguap dari fase padat) pada suhu rendah. Sebagai sebuah metaloid, antimon menyerupai logam dari penampilan fisiknya tetapi secara kimia ia bereaksi berbeda dari logam sejati. Termasuk racun .

Kegunaan Antimon (Sb)

• produksi industri semikonduktor dalam produksi diode dan detektor infra merah.

• sebagai sebuah campuran, logam semu ini meningkatkan kekuatan mekanik bahan.

• sebagai penguat timbal untuk batere. Kegunaan-kegunaan lain adalah campuran antigores, korek api, obat-obatan, dan pipa. 
""")
  elif opsi5:
       st.markdown("<h2 style='text-align: center; color: black;'>Bismut(Bi)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 208,98

Nomor Atom: 83

Konfigurasi Atom:  [Xe] 4f14 5d10 6s2 6p3

Banyak ditemukan: Ia muncul di alam tersendiri.

Golongan: non-logam

Wujud: kristal putih

Unsur ini merupakan kristal putih, logam yang rapuh dengan campuran sedikit bewarna merah jambu. Ia muncul di alam tersendiri. Bismut merupakan logam paling diamagnetik, dan konduktor panas yang paling rendah di antara logam, kecuali raksa. Ia memiliki resitansi listrik yang tinggi dan memiliki efek Hall yang tertinggi di antara logam (kenaikan yang paling tajam untuk resistansi listrik jika diletakkan di medan magnet).

Kegunaan BISMUT

•      Bismut oxychloride digunakan dalam bidang kosmetik dan bismut subnitratedan subcarbonate digunakan dalam bidang obat-obatan.

•      Magnet permanen yang kuat bisa dibuat dari campuran bismanol (MnBi)

•      Bismut digunakan dalam produksi besi lunak 

•      Bismut sedang dikembangkan sebagai katalis dalam pembuatan acrilic fiber 29
""")
  elif opsi6:
       st.markdown("<h2 style='text-align: center; color: black;'>Ununpentium(Uup)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 288

Nomor Atom: 115

Konfigurasi Atom: [Rn] 5f14 6d10 7s2 7p3

Banyak ditemukan: -

Golongan: -

Wujud: -

Ununpentium atau sekarang ini disebut dengan Moscovium adalah unsur sintetis radioaktif yang sedikit diketahui. Ini diklasifikasikan sebagai logam dan diharapkan padat pada suhu kamar. Ini meluruh dengan cepat ke elemen lain, termasuk nihonium.

Elemen itu sebelumnya telah diberi nama ununpentium, sebuah nama pengganti yang berarti satu-satu-lima dalam bahasa Latin. Pada bulan November 2016, The International Union of Pure and Applied Chemistry (IUPAC) menyetujui nama moscovium untuk elemen 115.

Untuk membuat Ununpentium, para ilmuwan di Rusia dan Amerika Serikat membombardir atom americium dengan ion kalsium dalam sebuah siklotron. Ini menghasilkan empat atom Ununpentium.
""")

           

    
#Golongan VI
if optiongolongan == "Golongan VI":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Oksigen (O)")
    opsi5 = st.button("Polonium (Po)")
  with col2:
    opsi2 = st.button("Sulfur (S)")
    opsi6 = st.button("Livermorium (Lv)")
  with col3:
    opsi3 = st.button("Selenium (Se)")
  with col4:
    opsi4 = st.button("Telurium (Te)")
  if opsi1:
     st.markdown("<h2 style='text-align: center; color: raisin black;'>Oksigen (O)</h2>", unsafe_allow_html=True)
     st.write(
        """
Ar : 16

Nomor Atom: 8

Konfigurasi Atom: [He] 2s²2p⁴

Banyak ditemukan: Oksigen adalah unsur ketiga terbanyak yang ditemukan berlimpah di matahari

Golongan: non-logam

Wujud: gas 

Oksigen merupakan unsur paling melimpah ketiga di alam semesta berdasarkan masa dan unsur paling melimpah di kerak bumi. Merupakan komponen paling umum ke-2 dalam atmosfir bumi.

Setiap makhluk hidup pasti membutuhkan gas ini, rata - rata setiap kali kita bernafas membutuhkan sekitar 2 liter oksigen. Di bidang Industri oksigen digunakan pada pengolahan besi menjadi baja di tanur terbuka  (tanur oksigen); saat dicampur dengan bahan bakar, digunakan untuk pengelasan, pemotongan, pemanasan dan penyepuhan; untuk membuat methanol, etilin oksida, titanium dioksida dan untuk memperkaya udara tungku untuk pencairan tembaga, seng, dan sebagainya; di pabrik kertas oksigen digunakan untuk memutihkan pulp, oksidasi dari cairan limbah pekat dan pemurnian limbah.

Pembuatan:
Setiap makhluk hidup pasti membutuhkan gas ini, rata - rata setiap kali kita bernafas membutuhkan sekitar 2 liter oksigen. Di bidang Industri oksigen digunakan pada pengolahan besi menjadi baja di tanur terbuka  (tanur oksigen); saat dicampur dengan bahan bakar, digunakan untuk pengelasan, pemotongan, pemanasan dan penyepuhan; untuk membuat methanol, etilin oksida, titanium dioksida dan untuk memperkaya udara tungku untuk pencairan tembaga, seng, dan sebagainya; di pabrik kertas oksigen digunakan untuk memutihkan pulp, oksidasi dari cairan limbah pekat dan pemurnian limbah.

kegunaan:
Setiap makhluk hidup pasti membutuhkan gas ini, rata - rata setiap kali kita bernafas membutuhkan sekitar 2 liter oksigen. Di bidang Industri oksigen digunakan pada pengolahan besi menjadi baja di tanur terbuka  (tanur oksigen); saat dicampur dengan bahan bakar, digunakan untuk pengelasan, pemotongan, pemanasan dan penyepuhan; untuk membuat methanol, etilin oksida, titanium dioksida dan untuk memperkaya udara tungku untuk pencairan tembaga, seng, dan sebagainya; di pabrik kertas oksigen digunakan untuk memutihkan pulp, oksidasi dari cairan limbah pekat dan pemurnian limbah.
""")
  elif opsi2:
       st.markdown("<h2 style='text-align: center; color: black;'>Sulfur atau belerang (S)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 32

Nomor Atom: 16

Konfigurasi Atom: [Ne] 3s2 3p4

Banyak ditemukan: Belerang terjadi secara alamiah di sekitar daerah pegunungan dan hutantropis. Sulfir tersebar di alam sebagai pirit, galena, sinabar, stibnite, gipsum, garamepsom, selestit, barit dan lain-lain

Golongan: non-logam

Wujud: padat

Sebagian besar belerang didunia digunakan untuk membuat asam sulfat. Belerang tersebar luas di alam. Bisa didapatkan langsung berupa belerang atau berbentuk senyawa.Belerang berwarna kuning pucat, padatan yang rapuh, yang tidak larut dalam air tapi mudah larut dalam CS2 (karbon disulfida).  Dalam berbagai bentuk, baik gas, cair maupun padat, unsur belerang terjadi dengan bentuk alotrop yang lebih dari satu atau campuran

pembuatan:

1.    Proses Frasch, cadangan bawah tanah belerang biasanya terdapat pada kedalaman antara 150-750 m dan tebalnya kira-kira 30 m. Pipa berdiameter 20 cm dimasukkan hingga ke dasar endapan belerang. Pipa lain yang lebih kecil, berdiameter 10 cm dan lebih pendek dimasukkan dalam pipa pertama. Pipa terakhir, bediameter 2,5 cm dimasukkan ke dalam pipa kedua. Pipa terakhir mempunyai panjang setengah dari pipa pertama (lihat gambar di bawah ini).Mula-mula air bersuhu 165oC dialirkan ke bawah melalui pipa pertama. Air panas ini akan melelehkan belerang di sekitarnya dan mendorong cairan belerang naik melalui pipa. Air bertekanan tinggi dipompa melalui pipa yang paling kecil, menghasilkan buih bermassa jenis kecil yang akan naik ke permukaan tanah melewati pipa berukuran sedang. Buih ini mengandung belerang, udara, dan air. Di permukaan tanah, campuran ini didinginkan dan menghasilkan kristal belerang berwarna kuning dari cairannya yang berwarna ungu. Kristal belerang dihancurkan dengan dinamit menjadi pecahan yang berukuran lebih kecil sehingga mudah diangkut ke tempat lain.

2.    Proses Claus, pada proses Claus, mula-mula gas alam dialirkan dalam etanol amin, HOCH2CH2NH2 dan terjadi reaksi: HOCH2CH2NH2(l) + H2S(g) ⇆ HOCH2CH2NH3+ + HS- Setelah dipisahkan, campuran kemudian dipanaskan sehingga H2S dilepaskan sebagai gas. Gas ini kemudian dicampur dengan gas oksigen untuk membakar sepertiga H2S menjadi gas SO2 dan air. Gas SO2 bereaksi dengan H2S sisa membentuk belerang dan air.

3.    Pemanasan Pirit, pirit dipanaskan tanpa udara akan menyebabkan dekomposisi S22- menjadi belerang dan FeS.

kegunaan:
Belerang adalah komponen serbuk mesiu dan digunakan dalam proses vulkanisasi karet alam dan juga berperan sebagai fungisida. Belerang digunakan besar-besaran dalam pembuatan pupuk fosfat.   Asam Sulfat (H2SO4) digunakan untuk berbagai keperluan, seperti pembersih logam, bahan baku industri dan sebagai cairan pengisi akumulator. Berton-ton belerang digunakan untuk menghasilkan asam sulfat, bahan kimia yang sangat penting. Belerang juga digunakan untuk pembuatan kertas sulfit dan kertas lainnya, untuk mensterilkan alat pengasap, dan untuk memutihkan buah kering.
""")
  elif opsi3:
       st.markdown("<h2 style='text-align: center; color: black;'>Selenium (Se)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 78,96

Nomor Atom: 34

Konfigurasi Atom: [Ar]3d10 4s2 1p4

Banyak ditemukan:-

Golongan: non-logam

Wujud: padat

Selenium ini paling sering dihasilkan dari bijih sulfida selenide di banyak, seperti tembaga, perak, atau timah. Hal ini diperoleh sebagai hasil sampingan dari pengolahan bijih ini, dari lumpur anoda kilang tembaga dan lumpur dari ruang utama tanaman asam sulfat. Lumpur tersebut dapat diproses oleh sejumlah sarana untuk memperoleh selenium gratis.

pembuatan:

Selenium diperoleh dari memanggang endapan hasil elektrolisis dengan soda atau asam sulfat. Atau dengan meleburkan endapan tersebut dengan soda dan niter (mineral yang mengandung kalium nitrat). Namun, dari sumber lainnya dikatakan bahwa selenium terjadi secara alami di lingkungan. Sebagai salah satu elemen, selenium tidak dapat diciptakan ataupun dihancurkan, meskipun selenium dapat berubah bentuk dalam lingkungan. 

kegunaan:
Selenium digunakan dalam xerografi untuk memperbanyak salinan dokumen, surat dan lain-lain. Juga digunakan oleh industri kaca untuk mengawawarnakan kaca dan untuk membuat kaca dan lapisan email gigi yang berwarna rubi. Juga digunakan sebagai tinta fotografi dan sebagai bahan tambahan baja tahan karat.
""")
  elif opsi4:
       st.markdown("<h2 style='text-align: center; color: black;'>Telurium (Te)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 127,6

Nomor Atom: 52

Konfigurasi Atom: [Kr] 4d10 5s2 5p4

Banyak ditemukan: -

Golongan: logam

Wujud: kristal

Telurium kadang-kadang dapat ditemukan di alam, tapi lebih sering sebagai senyawa tellurida dari emas (kalaverit), dan bergabung dengan logam lainnya. Telurium didapatkan secara komersil dari lumpur anoda yang dihasilkan selama proses pemurnian elektrolisis tembaga panas.

pembuatan:

Deposisi anoda berisi selenides dan tellurides dari logam mulia dalam senyawa dengan rumus M2Se atau M2Te (M = Cu, Ag, Au). Pada suhu 500 ° C anoda lumpur dipanggang dengan karbonat natrium di bawah udara. Ion logam direduksi menjadi logam, sementara Telluride diubah menjadi tellurite natrium.

kegunaan:

Telurium digunakan dalam tellurida kadmium (CdTe) sebagai panel surya. Panel surya CdTe ini digunakan untuk mencapai beberapa efisiensi sel tertinggi dalam pembangkit listrik tenaga surya. Produksi panel surya CdTe untuk komersial dilakukan oleh Perusahaan First Solar.
""")
  elif opsi5:
       st.markdown("<h2 style='text-align: center; color: black;'>Polonium (Po)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 209

Nomor Atom: 8

Konfigurasi Atom: [Xe] 6s2 4f14 5d10 6p4

Banyak ditemukan: -

Golongan: logam

Wujud: padat

Polonium adalah unsur alam yang sangat jarang. Dalam bijih uranium hanya mengandung sekitar 100 mikrogram unsur polonium per tonnya. Ketersediaan polonium hanya sekitar 0.2% dari radium. Para ahli menemukan bahwa ketika menembak bismut alam (209bi) dengan neutron, diperoleh 210bi yang merupakan induk polonium.

pembuatan:

Sejumlah milligram polonium kini didapatkan dengan cara seperti ini, dengan menggunakan tembakan neutron berintensitas tinggi dalam reaktor nuklir. Polonium-210 adalah yang paling banyak tersedia. Isotop dengan massa 209 (masa paruh waktu 103 tahun) dan massa 208(masa paruh waktu 2.9 tahun) bisa didapatkan dengan menembakkan alfa, proton, atau deutron pada timbal atau bismut dalam siklotron, tapi proses ini terlalu mahal. Logam polonium telah dibuat dari polonium hidroksida dan senyawa polonium dengan adanya ammonia cair anhidrat atau ammonia cair pekat.

kegunaan:

Ø  Digunakan untuk menghasilkan radiasi sinar alfa.

Ø  Digunakan pada peralatan mesin cetak dan fotografi.

Ø  Digunakan pada alat yang dapat mengionisasi udara untuk menghilangkan akumulasi muatan -muatan listrik .

Ø  Digunakan sebagai sumber panas yang ringan sebagai sumber energi termoelektrik pada satelit angkasa.
""")
  elif opsi6:
       st.markdown("<h2 style='text-align: center; color: black;'>Livemorium(Lv)</h2>", unsafe_allow_html=True)
       st.write(
           """
Ar : 293

Nomor Atom: 116

Konfigurasi Atom:  5f14 6d10 7s2 7p4

Banyak ditemukan: -

Golongan: logam

Wujud: padat

Livermorium adalah logam radioaktif sintetis, dibuat melalui pemboman nuklir, dan hanya diproduksi dalam jumlah kecil. Livermorium diproduksi dengan cara membombardir 248Cm dengan 48Ca.
""")

  
    
#Golongan VII
if optiongolongan == "Golongan VII":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Fluorin (F)")
    opsi5 = st.button("Astatin (At)")
  with col2:
    opsi2 = st.button("Klorin (Cl)")
    opsi6 = st.button("Ununseptium (Uus)")
  with col3:
    opsi3 = st.button("Bromin (Br)")
  with col4:
    opsi4 = st.button("Iodin (I)")
  if opsi1:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Fluorin (F)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 19

Nomor Atom: 9

Konfigurasi Elektron: [He] 2s²2p⁵

Banyak ditemukan: Unsur ini ditemukan dalam air, batuan, tumbuhan, dan tanah sebagai Fluorida.
      
Golongan: Halogen

Wujud: Gas

Fluorin merupakan Halogen yang paling ringan dan muncul pada kondisi standar sebagai gas diatomik kuning pucat yang sangat beracun
       """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Klorin (Cl)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 35,5

Nomor Atom: 17

Konfigurasi Elektron:[Ne] 3s²3p⁵

Banyak ditemukan: Klorin banyak ditemukan bersenyawa dengan unsur natrium membentuk garam dapur, serta ditemukan dalam karnalit dan silvit.
      
Golongan: Halogen
      
Wujud: Gas

Unsur ini merupakan elemen sangat reaktif dan oksidator kuat, klorin mempunyai afinitas elektron tertinggi dan elektronegativitas ketiga tertinggi di belakang oksigen dan fluor
      """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Bromin (Br)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 80

Nomor Atom: 35

Konfigurasi Elektron: [Ar] 4s²3d¹⁰4p⁵

Banyak ditemukan: bromin dalam bentuk bromida banyak ditemukan di alam pada batuan mineral dan air laut. 
      
Golongan: Halogen
      
Wujud: Cairan

Unsur dari deret kimia halogen ini berbentuk cairan berwarna merah pada suhu kamar dan memiliki reaktivitas di antara klor dan yodium. Dalam bentuk cairan, zat ini bersifat korosif terhadap jaringan sel manusia dan uapnya menyebabkan iritasi pada mata dan tenggorokan. Dalam bentuk gas, bromin bersifat toksik.
      """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Iodin (I)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 127

Nomor Atom: 53

Konfigurasi Elektron:[Kr] 4d¹⁰ 5s² 5p⁵

Banyak ditemukan: Iodin dapat ditemukan di makanan yang bersumber dari tanah atau laut. Iodin juga dapat ditemukan terutama pada makanan protein hewani dan sayuran laut. Selain itu, mineral ini juga terdapat pada makanan seperti roti, sereal, dan susu
      
Golongan: Halogen
      
Wujud: iodin adalah benda padat abu-abu yang menyublim menjadi uap warna ungu. 
      """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Astatin (At)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 85

Konfigurasi Elektron: [Xe] 4f¹⁴5d¹⁰6s²6p⁵

Banyak ditemukan: Astatin merupakan unsur alami yang paling langka di kerak bumi, hanya terjadi sebagai produk peluruhan dari berbagai unsur yang lebih berat.
      
Golongan: Halogen
      
Wujud: Padatan

Astatin adalah sebuah unsur yang sangat radioaktif; semua isotopnya memiliki waktu paruh 8,1 jam atau kurang, meluruh menjadi isotop astatin lainnya, bismut, polonium, atau radon. Sebagian besar isotopnya sangat tidak stabil, dengan waktu paruh satu detik atau kurang.
      """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununseptium (Uus)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar:-

Nomor Atom: 117

Konfigurasi Elektron: 5f14 6d10 7s2 7p5 (diprediksi)

Banyak ditemukan: Ununseptium adalah unsur super berat yang dibuat secara artifisial dan tidak ditemukan secara bebas di bumi.
      
Golongan: Halogen
      
Wujud : -

Meskipun saat ini ditempatkan sebagai anggota terberat dari keluarga halogen, tidak ada bukti eksperimental yang sifat kimia dari ununseptium cocok dengan anggota ringan seperti yodium atau astatin dan analisis teoretis menunjukkan mungkin ada beberapa perbedaan penting. Ununseptium secara resmi dikenal sebagai Tennessine
     """)

    
    
#Golongan VIII
if optiongolongan == "Golongan VIII":
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    opsi1 = st.button("Helium (He)")
    opsi5 = st.button("Xenon (Xe)")
  with col2:
    opsi2 = st.button("Neon (Ne)")
    opsi6 = st.button("Radon (Rn)")
  with col3:
    opsi3 = st.button("Argon (Ar)")
    opsi7 = st.button("Ununoktium (UuO)")
  with col4:
    opsi4 = st.button("Kripton (Kr)")
  if opsi1:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Helium (He)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 2

Nomor Atom: 2

Konfigurasi Elektron: 1s2

Banyak ditemukan: Helium ditemukan dalam jumlah besar dalam mineral uranium dan torium, termasuk kleveit, uraninit. karnotit, dan monazit, karena mineral-mineral ini mengemisi partikel alfa (inti helium He2+).
      
Golongan: Gas Mulia
      
Wujud : gas terkecuali pada kondisi yang sangat ekstrem.

Helium tak berwarna, tak berbau, tak berasa, tak beracun, hampir inert, berupa gas monatomik, dan merupakan unsur pertama pada golongan gas mulia dalam tabel periodik. Titik didih dan titik lebur gas ini merupakan yang terendah di antara semua unsur. 
     """)
  elif opsi2:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Neon (Ne)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: 20,2

Nomor Atom: 10

Konfigurasi Elaktron: [He] 2s²2p⁶

Banyak ditemukan: Di bumi, satu-satunya sumber neon adalah dari ekstraksi udara cair. Neon juga ditemukan di berlian dan beberapa rongga vulkanik. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Neon adalah gas monoatomik lengai yang nirwarna dan nirbau pada kondisi standar, dengan massa jenis sekitar dua pertiga udara. Neon memberikan pancaran oranye kemerahan yang berbeda saat digunakan pada lampu pijar neon bertegangan rendah, tabung lucutan, dan tanda iklan neon.[13][14] Garis emisi merah dari neon juga menyebabkan lampu merah dari laser helium–neon. Neon digunakan dalam beberapa tabung plasma dan aplikasi pendingin tetapi memiliki beberapa kegunaan komersial lainnya.
     """)
  elif opsi3:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Argon (Ar)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 18

Konfigurasi Elektron: [Ne] 3s²3p⁶

Banyak ditemukan: Argon adalah gas mulia yang paling melimpah dan menyumbang sekitar 0,94% dari atmosfer bumi dan sekitar 1,6% dari atmosfer Mars. Atmosfer tipis planet Merkurius terdiri dari sekitar 70% argon.
      
Golongan: Gas Mulia
      
Wujud : Gas

Argon memiliki kelarutan mirip oksigen dan sekitar 2,5 kali lebih mudah larut dalam air dari nitrogen.

Unsur kimia inert ini tidak berwarna dan tidak berbau baik dalam bentuk cair dan gas.

Argon diisolasi dari udara dengan fraksinasi, paling sering dengan distilasi fraksional kriogenik, suatu proses yang juga menghasilkan nitrogen murni, oksigen, neon, kripton dan xenon
     """)
  elif opsi4:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Kripton (Kr)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 36

Konfigurasi Elaktron: [Ar] 3d¹⁰4s²4p⁶

Banyak ditemukan: Kripton terdapat di udara dengan konsentrasi sekitar 1 ppm. Gas ini ditandai dengan spektrum garis-garis cerah hijau dan oranye.
      
Golongan: Gas Mulia
      
Wujud : Gas

Pada kondisi normal, kripton bersifat tidak berwarna dan tidak berbau. Namun, apabila diletakkan pada medan listrik bertegangan tinggi, kripton akan memancarkan cahaya berwarna putih.
     """)
  elif opsi5:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Xenon (Xe)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 54

Konfigurasi Elaktron:  [Kr] 4d¹⁰5s²5p⁶

Banyak ditemukan: Xenon adalah anggota gas mulia atau gas inert. Terdapat di atmosfer kta dengan kandungan satu bagian per dua puluh juta bagian atmosfer. Unsur ini ditemukan dalam bentuk gas, yang dilepaskan dari mineral mata air tertentu, dan dihasilkan secara komersial dengan ekstraksi udara cair. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Xenon berupa gas mulia, tak berwarna, tak berbau dan tidak ada rasanya.

Xenon diperoleh dari udara yang dicairkan. Xenon dipergunakan untuk mengisi lampu sorot, dan lampu berintensitas tinggi lainnya, mengisi bilik gelembung yang dipergunakan oleh ahli fisika untuk mempelajari partikel sub-atom.
     """)
  elif opsi6:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Radon (Rn)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 86

Konfigurasi Elaktron: [Xe] 4f145d106s26p6

Banyak ditemukan: Konsentrasi radon yang tinggi dapat ditemukan di beberapa mata air dan mata air panas. 
      
Golongan: Gas Mulia
      
Wujud : Gas

Radon adalah sebuah gas mulia yang bersifat radioaktif, tak berwarna, tak berbau, dan tak berasa. Ia terjadi secara alami dalam jumlah kecil sebagai perantara dalam rantai peluruhan radioaktif normal di mana torium dan uranium perlahan-lahan meluruh menjadi berbagai unsur radioaktif berumur pendek dan timbal. Radon sendiri merupakan produk peluruhan langsung dari radium. 
     """)
  elif opsi7:
    st.markdown("<h2 style='text-align: center; color: raisin black;'>Ununoktium (UuO)</h2>", unsafe_allow_html=True)
    st.write(
      """
Ar: -

Nomor Atom: 118

Konfigurasi Elaktron:  5f14 6d10 7s2 7p6 (diprediksi)

Banyak ditemukan: -
      
Golongan: Gas Mulia
      
Wujud : Gas

Ununoktium (dikenal juga dengan nama eka-radon) merupakan nama sementara untuk unsur kimia sintetik super berat yang dalam tabel periodik bersimbolkan Uuo dan bernomor atom 118. Unsur ini diperkirakan memiliki sifat yang sama dengan unsur-unsur segolongannya, yaitu gas luhur.
     """)
  




    
    
    
    
    
    
    
    
