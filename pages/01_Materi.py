import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: raisin black;'>Gaia Library</h1>", unsafe_allow_html=True)
st.subheader("Apa yang mau kamu pelajari hari ini?")

#Tab mata kuliah
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Fisika Dasar"])

#Materi Kimia Dasar
with tab_1:
    optionkimdas = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Atom, Molekul, dan Ion", "Stoikiometri","Ikatan Kimia","Sifat Fisis Larutan","Kinetika Kimia","Kesetimbangan Kimia","Asam Basa",))
    if optionkimdas == "Atom, Molekul, dan Ion":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Struktur Atom</h2>", unsafe_allow_html=True)
        st.write("Konsep atom pertama kali ditemukan oleh Demo Cristus. Atom berasal dari kata atmos yang dalam bahasa Yunani “at” berarti “tidak” dan “tomos” berarti “dibagi”. Maka, jika digabungkan atom adalah partikel yang sudah tidak dapat dibagi lagi. Menurut Dalton konsep atom Demo Christus ini tidak bertentangan dengan hukum kekekalan massa dan hukum kekekalan energi. Sehingga Dalton membuat teori tentang atom.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Teori Atom</h2>", unsafe_allow_html=True)
        st.write(
            """
            •	Teori Atom Dalton

John Dalton tahun 1803 merumuskan teori atom sebagai berikut: 
1.	Materi tersusun atas partikel-partikel terkecil yang disebut atom
2.	Atom-atom penyusun unsur bersifat identik (sama dan sejenis)
3.	Atom suatu unsur yang tidak dapat diubah menjadi atom unsur lain
4.	Senyawa tersusun atas 2 jenis atom atau lebih dengan perbandingan tetap dan juga tertentu.
5.	Pada reaksi kimia terjadi penataulangan atom-atom yang bereaksi. Reaksi kimia terjadi karena pemisahan atom-atom senyawa untuk kemudian bergabung kembali membentuk senyawa baru.

Kelebihan:
1.	Dapat menerangkan hukum kekekalan massa (hukum Lavoisier)
2.	Dapat menerangkan hukum Perbandingan tetap (Hukum Proust)

Kelemahan:
1.	Tidak dapat menjelaskan sifat listrik atom
2.	Pada kenyataannya atom dapat dibagi lagi menjadi partikel yang lebih kecil yang disebut subatomik.
            """)
        imageKimdas1 = Image.open('Resource/image/Kimdas/Atom1.jpg')
        st.image(imageKimdas1)
        st.write(
            """
            •	Teori Thomson

Setelah tahun 1897 Joseph John Thomson berhasil membuktikan dengan tabung sinar katode bahwa sinar katode adalah berkas partikel yang bermuatan negarif yang ada pada setiap materi maka tahun 1898 J.J Thomson membuat suatu teori atom. Menurut Thomson, atom berbentuk bulat dimana muatan listrik positif yang tersebar merata dalam atom dinetralkan oleh elektron-elektron yang berbeda di antara muatan positif. Elektron-elektron dalam atom diumpamakan seperti butiran kismis dalam roti, maka teori atom Thomson juga sering dikenal teori roti kismis.

Kelebihan: 

Membuktikan adanya partikel lain yang bermuatan negatif dalam atom. Berarti atom bukan merupakan bagian terkecil dari suatu unsur. Selain itu juga memastikan bahwa atom tersusun dari partikel yang bermuatan positif dan negatif untuk membentuk atom netral. Juga membuktikan bahwa elektron terdapat dalam semua unsur.

Kelemahan:

Belum dapat menerangkan bagaimana susunan muatan positif dan jumlah elektron dalam bola.
            """)
        imageKimdas2 = Image.open('Resource/image/Kimdas/Atom2.jpg')
        st.image(imageKimdas2)
        st.write(
            """
            •	Teori Rutherford
            
Pada tahun 1903 Philipp Lenard melalui percobaannya membuktikan bahwa teori atom Thomson yang menyatakan bahwa elekron tersebar merata dalam muatan positif atom adalah tidak benar. Hal ini mendorong ernest Rutherford (1911) tertarik untuk melanjutkan eksperimen Lenard. Dengan bantuan kedua muridnya Hans Geiger dan Ernest Mersden, Rutherford melakukan percobaan dengan hamburan sinar α. Partikel α bermuatan positif. Dari percobaan tersebut disumpulkan bahwa:
1.	Sebagian besar ruang dalam atom adalah tuang hampa; partikel α diteruskan
2.	Didalam atom terdapat suatu bagian yang sangat kecil dan padat yang disebut inti atom; partikel α dipentulkan kembali oleh inti atom
3.	Muatan inti atom dan juga partikel α sejenis yaitu positif; sebagian kecil partikel α dibelokkan

Hasil percobaan tersebut menggugurkan teori atom Thomson. Kemudian Rutherford mengajukan teori atom sebagi berikut: atom tersusun atas inti atom yang bermuatan positif sebagai pusa massa dan keliling elektron-elektron yang bermuatan negative.

Kelebihan:

Membuat hipotesa bahwa atom tersusun dari inti atom dan elektron yang mengelilingi inti dan satu sama lain terpisah oleh ruang hampa.

Kelamahan: 

Model tersebut tidak dapat menerangkan mengapa elektron tidak pernah jatuh ke dalam inti sesuai dengan teori fisika klasik.
            """)
        imageKimdas3 = Image.open('Resource/image/Kimdas/Atom3.jpg')
        st.image(imageKimdas3)
        st.write(
            """
            •	Teori Bohr
            
Diawali dari pengamatan Nels Bohr terhadap spectrum atom, adanya spectrum garis menujukan bahwa elektron hanya beredar pada lintasan-lintasan dengan energi tertentu. Dengan teori mekanikan kuantum planck, bohr (1913) menyampaikan 2 postulat untuk menjelaskan kestabilan atom.

Dua postulat bohr
1.	Elektron mengelilingi inti atom ada lintasan tertentu yang stasioner yang disebut orbit/kulit. Walaupun elektron bergerak cepat tetapi elekton tidak memancarkan atau menyerap energi sehingga energi elekktron konstran. Hal ini berarti elektron yang berputar mengelilingi inti atom memiliki lintasan tetap sehingga elektron tidak jatuh ke inti.
2.	Elektron dapat berpindah dari kulit yang satu ke kulit yang lain dengan memancarkan atau menyerap energi. Energi yang dipancarkan atau diserap ketika elektron berpidah-pindah kulit disebut foton. Besarnya foton dirumuskan.
3.	Energi yang dibawa foton ini bersifat diskrit (catu). Jika suatu atom menyerap energi, maka energi ini digunakan elektron untuk berpindah kulit dari tingkat energi rendah ke tingkat energi tinggi.

Kelebihan :

Mampu membuktikan adanya lintasan elektron untuk atom hidrogen dengan jari-jari bola

Kelamahan :

Hanya dapat menerangkan atom-atom yang memiliki elektron tunggal seperti gas hidrogen, tetapi tidak dapat menerangkan spektrum warna dari atom-atom yang memiliki banyak elektron.
            """)
        imageKimdas4 = Image.open('Resource/image/Kimdas/Atom4.jpg')
        st.image(imageKimdas4)
        st.write(
            """
            •	Teori Mekanika Kuantum
            
Konsep Bohr tentang tingkat-tingkat energi mendasari perkembangan teori atom mekanika kuantum. Elektron terletak pada orbital-orbital. Orbital merupakan suatu ruangan dimana kebolehjadian ditemukannya elektron.
            """)
        st.write(
            """
            Daftar Pustaka: 
           
Diki. 2022. 5 Teori Atom Menurut Para Ahli. https://dosenpintar.com/5-teori-atom-menurut-para-ahli/#Struktur_atom.

L,Admin. 2015. Kelebihan dan Kelemahan Model Atom. https://www.markijar.com/2015/05/kelebihan-dan-kelemahan-model-atom.html.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1Slheotw7HAcpZ-uEzV7PkO1ingI3lATo/view?usp=sharing)")

    if optionkimdas == "Stoikiometri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Stoikiometri</h2>", unsafe_allow_html=True)
        st.write(
            """
            A.	Pengertian Rumus Molekul dan Rumus Empiris
            
Rumus molekul adalah rumus yang menjelaskan mengenai jumlah atom pada tiap unsur di dalam suatu senyawa. Sementara itu, rumus empiris adalah rumus yang menjelaskan mengenai perbandingan atom yang paling sederhana di dalam suatu senyawa.

B.	Menentukan Rumus Molekul

Rumus Molekul pada dasarnya memiliki jumlah atom kelipatan dari rumus empiris. Meskipun ada beberapa senyawa yang rumus molekul dan rumus empirisnya sama. Persamaan yang digunakan untuk menuliskan rumus molekul.

Rumus molekul:
Mr rumus empiris x n = Mr rumus molekul

C.	Menentukan Rumus Empiris. 
1.	Menggunakan rumus molekul, 
caranya dengan menyederhanakan jumlah dari atom penyusun rumus molekul agar menghasilkan bilangan bulat yang paling kecil.
2.	Menggunakan perbandingan mol, 
caranya dengan membandingkan mol unsur penyusun senyawa dengan syarat massanya harus diketahui.

D.	Pengertian Stoikiometri

Stoikiometri pertama kali dikemukakan oleh ilmuwan Jerman Bernama Jeremias Benjamin Richter pada abad akhir ke-19. Ketika itu, ia ingin mencari tahu jumlah relatif reaktan dan produk di dalam suatu reaksi kimia. Jadi, Stoikiometri adalah suatu ilmu kimia yang mempelajari mengenai kuantitas yang terdapat di dalam suatu zat seperti massa, volume, jumlah mol, dan jumlah partikel. Suatu reaksi dikatakan sebagai reaksi stoikiometri apabila suatu reaktan habis sepenuhnya. Pada reaksi stoikiometri, bilangan yang mewakili mol reaktan dan produk di dalam reaksi disebut koefisien stoikiometri yang bertujuan untuk menetapkan perbandingan antara mol reaktan dengan mol produk.

E.	. Hukum Dasar Stoikiometri
1.	Hukum kekekalan massa (Hukum Lavoisier), 
hukum yang menjelaskan mengenai kondisi massa total suatu zat setelah reaksi yang sama dengan massa total sebelum dilakukan reaksi.
2.	Hukum Perbandingan Tetap (Hukum Proust), 
hukum ini menjelaskan perbandingan massa unsur penyusun pada senyawa akan selalu tetap. 
3.	Hukum Perbandingan Berganda (Hukum Dalton), 
hukum ini menjelaskan mengenai kondisi ketika dua unsur yang dapat menghasilkan lebih dari suatu senyawa maka perbandingan massa unsur salah satu unsur adalah bilangan bulat sederhana.
4.	Hukum Perbandingan Volume (Hukum Gay-Lussac), 
hukum ini menyatakan bahwa perubahan suatu volume gas akan dipengaruhi oleh suhu dan tekanan.
5.	Hipotesis Avogadro, 
hipotesis Avogadro menyatakan bahwa suatu partikel unsur tidak selalu atom, tetapi dapat berupa molekul unsur.

F.	Konsep Stoikiometri
1.	Massa Atom Relatif (Ar), massa atom relatif adalah perbandingan massa satu atom dengan 1/12 kali massa dari isotop karbon-12. C-12 dijadikan standar perbandingan karena memiliki kestabilan inti dibandingan dengan yang lain.
2.	Massa Molekul Relatif (Mr), massa molekul relatif adalah massa yang digunakan untuk mencari perbandingan massa dari satu molekul senyawa dengan 1/12 kali massa C-12.
3.	Konsep Mol. konsep mol menyatakan bahwa satu mol suatu zat adalah banyaknya zat tersebut mengandung 6,02 x 1023. Hubungan mol dengan jumlah partikel telah ditetapkan sesuai dengan hipotesis Avogadro.
4.	Molaritas (M), molaritas adalah jumlah mol zat terlarut pada satu liter larutan.
Rumus molaritas:
M = n/V
            """)
        st.write(
            """
            Daftar Pustaka:
            
            SEO Management. 2022. Stoikiometri Adalah : Pengertian, Rumus, Hukum dam Contoh soal. https://www.sampoernaacademy.sch.id/id/stoikiometri-adalah/
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/17M05OfuolzThRbny0_0BwD1OPp8EfEto/view?usp=sharing)")
        
        
    if optionkimdas == "Ikatan Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Ikatan Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            Konfigurasi Elektron Gas Mulia
            
A. Teori Lewis

G.N. Lewis dan W. Kossel mengkaitkan kestabilan gas mulia dengan konfigurasi elektron sebagai berikut :
1. Gas mulia bersifat stabil karena memiliki konfigurasi elektron penuh. Yaitu oktet atau 8 elektron pada kuliat terluar. Kecuali Helium dengan konfigurasi duplet atau 2 elektron pada kulit terluar.
2. unsur unsur lain dapat mencapai konfigurasi elektron oktet atau duplet dengan membentuk ikatan kimia. 

B. Pembentukan ion positif

Ion positif dapat terbentuk karena suatu atom melepaskan elektron terluarnya sehingga atom tersebut mencapai keadaan stabil yaitu oktet atau duplet. Atom logam yang memiliki valensi rendah (elektron valensi 1,2&3) cenderung melepaskan elektron. Elektron valensi sesuai dengan golongan tabel periodik. Jumlah ion positinf sama dengan jumlah elektron yang dilepaskan.
Contoh ; Na dengan nomor atom 11 memiliki konfigurasi elektron 1s1 2s1 2p6 3s1

C. Pembentukan Ion Negatif 

Ion negative terbentuk karena suatu atom menangkap elektron sehingga atom tersebut mencapai keadaan stabil yaitu oktet atau duplet. Atom logam yang memiliki valensi tinggi(elektron valensi 4,6,7) cenderung menangkap elektron.
Contoh : Fluorin dengan nomor atom 9 memiliki konfigurasi elektron 1s2 2s2 2p5

D. Struktur Lewis

Pembentukan ikatan kimia menyangkut pada perubahan konfigurasi elektron, khusunya pada kulit valensi. Oleh karena itu, untuk penyederhanaan, atom atom cukup digambarkan valensinya. Lambang atom yang disertai elektron valensi disebut lambang lewis. Contoh :
Be dengan nomor atom 4 memiliki konfigurasi elektron yaitu 1s2 2s2. Sehingga Be memiliki
elektron valensi 2, sehinga rumus lewis : •BE•

Ikatan Ion

Pada ikatan ion, terjadi transfer elektron dari satu atom ke atom lain. Karena Perpindahan elektron ini maka atom yang mendapatkan elektron yakan bermuatan negatif (Anion) dan yang kehilangan elektron akan bermuatan positif (Kation). Karena adanya perbedaan muatan antar ion, maka ion positif dan ion negative akan saling tarik menarik oleh gaya elektrostatik. Kejadian ini merupakan dasar ikatan ionic.
Contoh :
            """)
        imageKimdas1 = Image.open('Resource/image/Kimdas/Picture2.jpg')
        st.image(imageKimdas1)
        st.write(
            """
Sifat senyawa ion yaitu :
1.	Memiliki titik didih dan titik leleh yang tinggi.
2.	Keras tetapi rapuh.
3.	Berupa padatan pada suhu ruang.
4.	Larut dalam pelarut air, tetapi umumnya tidak larut dalam pelarut organik.
5.	Tidak meghantarkan listrik pada fasa padatan. Tetapi, menghantarkan listrik pada fasa cairan.
            """)
        st.write(
            """
            Ikatan Kovalen
1.	Proses Pembentukan Ikatan Kovalen Tunggal

    Ikatan terjadi karena pemakaian Bersama elektron oleh atom atom yang berikatan. Pasangan elektron yang dipakai Bersama disebut pasangan elektron ikatan dan pasangan elektron valensi yang tidak terlibat dalam pembentukan ikatan kovalen disebut pasangan elektron bebas. Ikatan kovalen umumnya terjadi antara atom atom unsur nonlogam. Senyawa yang hanya mengandung ikatan kovalen disebut senyawa kovalen. Struktur Lewis adalah penggambaran ikatan kovalen yang menggunakan lambang titik lewis dimana Pasangan elektron ikatan dinyatakan dengan garis atau sepasang titik yang diletakkan di antara kedua atom dan Pasangan elektron bebas dinyatakan titik titik pada masing masing atom.
            """)
        imageKimdas2 = Image.open('Resource/image/Kimdas/Picture3.jpg')
        st.image(imageKimdas2)
        st.write(
            """
2.	Proses Pembentukan Ikatan Kovalen Rangkap 2

    Ikatan kovalen rangkap 2 adalah ikatan kovalen yang melibatkan dua pasang elektron bersama. Ikatan kovalen rangkap 2 dinyatakan dengan dua garis. Contohnya :
            """)
        imageKimdas3 = Image.open('Resource/image/Kimdas/Picture6.jpg')
        st.image(imageKimdas3)
        st.write(
            """
3.	Proses Pembentukan Ikatan Kovalen Rangkap 3

    Ikatan kovalen rangkap 3 adalah ikatan kovalen yang melibatkan dua pasang elektron bersama. Ikatan kovalen rangkap 3 dinyatakan dengan tiga garis. Contohnya :
            """)
        imageKimdas4 = Image.open('Resource/image/Kimdas/Picture5.jpg')
        st.image(imageKimdas4)
        st.write(
            """
Sifat senyawa kovalen :
1.	Berupa cairan, padatan lunak,dan gas pada suhu ruang.
2.	Bersifat lunak dan tidak rapuh
3.	Mempunyai titik leleh dan titik didih yang rendah.
4.	Umumnya tidak larut dalam air, namun larut pada pelarut organik.
5.	Tidak menghantarkan listrik.
            """)
        st.write(
            """
**Ikatan Kovalen Koordinasi**
            
Ikatan Kovalen koordinasi adalah ikatan yang terbentuk dari pemakaian pasangan elektron bersama yang berasal dari salah satu atom yang memiliki pasangan elektron bebas. Ciri ikatan kovalen koordinasi adalah pasangan elektron bebas dari salah satu atom yang dipakai secara bersama-sama. Contoh : 
            """)
        imageKimdas5 = Image.open('Resource/image/Kimdas/Picture4.jpg')
        st.image(imageKimdas5)
        st.write(
            """
            Jadi, senyawa HNO3 memiliki satu ikatan kovalen koodinasi dan 2 ikatan kovalen.
            """)
        st.write(
            """
**Ikatan logam**
            
Ikatan logam merupakan ikatan kimia antara atom-atom logam,bukan ikatan ion maupun kovalen. Dalam suatu logam terdapat atom atom sesamanya yang berikatan satu sama lain sehingga suatu logam akan bersifat kuat, keras, dan dapat ditempa. Elektron elektron valensi dari atom atom logam bergerak dengan cepat (membentuk lautan elektron) mengelilingi inti atom. Ikatan yang terbentuk sangat kuat sehingga ikatan antaratom logam sukar dilepaskan. 
Sifat Senyawa Logam :
1.	Berupa padatan pada suhu ruang
2.	Bersifat keras, tetapi lentur/tidak mudah patah jika ditempa.
3.	Mempunya titik didih dan titik leleh yang tinggi.
4.	Penghantar listrik yang baik.
5.	Mempunyai permukaan yang mengkilap.
6.	Memberi efek foto listrik dan Efek Termionik.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1sYRNmfqYGGh6gZio8N5-I-Wo_14qt55w/view?usp=sharing)")        
        
    if optionkimdas == "Sifat Fisis Larutan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Sifat Fisis Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Jenis Larutan

Larutan yang mengandung jumlah zat maksimum yang terkandung pada pelarut pada suhu tersebut disebut latutan jenuh. Sebelum titik tercapai, larutannya disebut larutan tak jenuh. Larutan tak jenuh mengandung zat terlarut lebih sedikit dibandingkan dengan kemampuaanya untuk melarutkan. Sedangkan larutan lewat jenuh, mengandung lebih banyak zat terlarut dibandingkan yang terdapat dilarutan jenuh. Larutan lewat jenuh bukanlah larutan yang sangat stabil. Pada saat,Sebagian zat terlarut akan terpisah dari larutan lewat jenuh sebagai kristal. Proses inilah yang disebut kristalisasi. 

B. Proses Pelarutan Dari Sudut Pandang Molekul.

Gaya tarik menarik memainkan peran penting dalam pembentukan larutan. Bila zat terlarut larut dalam zat pelarut, partikel zat tersebut akan menyebar ke seluruh pelarut. Partikel zat terlarut ini menempati posisi yang biasanya ditempati oleh molekul pelarut. Tiga jenis interaksi :
1.	Interaksi pelarut-pelarut.
2.	Interaksi zat pelarut-zat terlarut.
3.	Interaksi pelarut-zat terlarut.

Proses pelarutan dibagi menjadi tiga tahap:
            """)
        imageKimdas1 = Image.open('Resource/image/Kimdas/fisis1.jpg')
        st.image(imageKimdas1)
        st.write(
            """
Proses pelarutan dipengaruhi oleh dua faktor. Faktor pertama adalah energi, yang menentukan apakah proses berlangsung eksotermik atau endotermik. Faktor kedua adalah kecenderungan hakiki menuju ketidakteraturan dalam semua kejadian dialam. 

C. Satuan Konsentrasi
1.	Jenis Satuan konsentrasi.

    **Persen berdasar massa**

    %zat terlarut = (Massa zat terlarut/massa larutan)x100%	

    **Molaritas**

    M= mol zat terlarut/liter larutan

    Dengan satuan (mol/L)

    **Molalitas**

    m = mol zat terlarut/massa pelarut(kg)

2.	Perbandingan Satuan Satuan Konsentrasi

    V1 X M1=V2 X M2

    Keterangan : V adalah volume pelarut dan M dapat diganti dengan satuan lain sesuai dengan yang diketahui.

D. Pengaruh Suhu terhadap kelarutan
1.	Kelarutan Padatan dan Suhu

    Kelarutan zat padatan meningkat dengan meningkatnya suhu.

2.	Kelarutan Gas dan Suhu

    Kelarutan gas dalam air biasanya menurun dengan meningkatnya suhu. Dengan meningkatnya suhu, molekul udara yang terlarut mulai’mendidih’dan keluar dari larutan jauh sebelum air itu mendidih

E. Pengaruh Tekanan Terhadap Kelarutan Gas

Hubungan Kelarutan gas dan tekanan ditunjukkan oleh hukum Henry yang menyatakan bahwa kelarutan gas dalam cairan berbanding lurus dengan tekanan gas diatas larutannya. 
Dengan rumus : c=kP

Keterangan : 
c : konsentrasi molar(mol per Liter)

P : tekanan

k : konstanta

F. Sifat Koligatif

Sifat koligatif adalah beberapa sifat penting larutan bergantung pada banyaknya partikel zat terlarut dalam larutan dan tidak bergantung pada jenis partikel zat terlarut.

1.	Penurunan Tekanan Uap

    Hubungan tekanan uap larutan dengan tekanan uap pelarut bergantung pada konsentrasi zat terlarut dalam larutan. Hukum Raoult yang menyatakan bahwa tekanan parsial pelarut dari larutan, Pi adalah tekanan uap pelarut murni, Pio dikalikan dengan fraksi mol pelarut dalam larutan Xi.
Pi = Xi. Pio

2.	Tekanan Titik Didih

    Keberadaan zat terlarut yang tidak mudah menguap menurunkan tekanan uap larutan,maka berpengarug pada titik didih. Titik didi adalah suhu pada saat tekanan uap larutan sama 
dengan tekanan atmosfer luar. Kenaikan titik didih didefinisikan sebagai berikut:

    ΔTd = Td - Tdo
    
    Dimana Td adalah titik didih larutan, dan Tdo adalah titik didih pelarut murni.

3.	Penurunan titik beku 

    Penurunan titik beku didefinisikan sebagai berikut:
    
    ΔTb = Tbo – Tb
    
    Pembekuan melibatkan transisi dari keadaan tidak teratur ke keadaan terarur. Agar proses itu terjadi, energi harus diambil dari system karena larutan lebih tidak teratur dibandingkan pelarut, maka lebih banyak energi yang diambil untuk menciptakan keteraturan. Jadi, larutan memiliki titik beku lebih rendah dibandingkan pelarut.

4.	Tekanan Osmotik

    Osmosis adalah Gerakan bersih molekul pelarut melewati membrane semipermeabel dari pelarut murni atau dari larutan encer ke larutan pekat. Telakan osmotik adalah tekanan yang digunakan untuk menghentikan osmosis. 

    Π = MRT

    Keterangan :

    M : Molaritas

    R : Konstanta gas (0,0821 L. atm/K. mol)

    T : Suhu mutlak.

5.	Sifat Koligatif Elektrolit

    Sifat koligatif elektrolit memerlukan pendekatan yang sedikit berbeda daripada yang digunakan untuk sifat koligatif nonelektrolit. Karena elektrolit terurai menjadi ion-ion dalam larutan dan dengan demikian satu satuan senyawa elektrolit terpisah menjadi dua atau lebih partikel bila dilarutkan. Persamaan Sifat Koligatif :

    Π = iMRT

    keterangan :

    M : Molaritas

    R : Konstanta gas (0,0821 L. atm/K. mol)

    T : Suhu mutlak.

    i : faktor van’t hoff 

    i : jumlah partikel sebenarnya dalam larutan setelah penguraian/jumlah satuan rumus yang semua terlarut dalam larutan
              """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/18k2U9tA8Ll8BiGVaDnlz2r8tUvDf7yOA/view?usp=sharing)")
        
    if optionkimdas == "Kinetika Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kinetika Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            A. Laju Reaksi

Laju reaksi,yaitu perubahan konsentrasi reaktan atau produk terhadapa waktu (M/s). Persamaan Umum produk 

Reaktan → Produk

Dari persamaan ini dapat diketahui bahwa,selama berlangsungnya suatu reaksi, molekul reaktan bereaksi sedangkan molekul produk terbentuk.Sebagai hasilnya, kita dapat mengamati jalannya reaksi dengan cara memantau menurunnya konsentrasi reaktan atau 
meningkatnya konsentrasi produk.

A → B

Laju = - Δ[A]/Δt

Laju = - Δ[B]/Δt 

B. Hukum laju

Salah satu cara untuk mengkaji pengaruh konsentrasi reaktan terhadap laju reaksi ialah dengan menentukan bagaimana laju awal bergantung pada konsentrasi awal. Konsentrasi reaktan menurun dan akan menjadi sulit untuk mengukur perubahan nya secara akurat. Selain itu, mungkin saja terjadi reksi balik seperti

Produk → Reaktan

Hukum laju : Laju = k[A]X[Y]Y

Untuk reaksi umum : aA + bB → cC + dD

C. Hubungan Antara Konsentrasi Reaktan dan Waktu
1.	Reaksi Orde Pertama : Reaksi yang lajunya bergantung pada konsentrasi reaktan dipangkatkan dengan satu.
2.	Reaksi Orde Kedua : Reaksi yang lajunya bergantung pada konsentrasi reaktan dipangkatkan dengan dua.

D. Energi Aktivasi dan Ketergantungan Konstanta Laju Terhadap suhu
1. Teori Tumbukan pada Kinetika Kimia

    Dari segi teori tumbukan pada kinetika kimia, maka dapat diperkirakan laju reaksi akan berbanding lurus dengan banyaknya tumbukan molekul per detik atau berbanding lurus dengan frekuensi tumbukan molekul.

    Laju = banyaknya tumbukan/waktu(sekon)
    
2. Persamaan Arrhenius

    Ketergantungan konstanta laju reaksi terhadap suhu dapat dinyatakan dengan persamaan yang dikenal dengan persamaan Arrhenius :

    k = Ae-EaIRT

E. Mekanisme Reaksi dan Hukum Laju

Dalam banyak kasus, persamaan ini sekedar menyatakan jumlah dari sederet reaksi sederhana yang sering dinamakan sebagai tahap elementer karena reaksi reaksi sederhana tersebut merepresentasikan jalannya reaksi keseluruhan pada tingkat molekul. Urutan-urutan elementer yang mengarah pada pembentukan produk dinamakan mekanisme reaksi. Sebagai contoh ;

2NO(g) → N2O2(g)

N2O2(g) + O2(g) → 2NO2(g)

Maka :

Tahap 1 : NO(g)   + NO(g) →  N2O2(g)

Tahap 2 : N2O2(g) + O2(g) →  2NO2(g)

Reaksi Keseluruhan : 2NO(g) + N2O2(g) + O2(g) → N2O2(g) + 2NO2(g)

Tahap Elementer harus memenuhi dua syarat:
1.	Jumlah elementer harus menghasilkan persamaan setara keseluruhan untuk reaksi tersebut.
2.	Tahap penentu laju, yaitu tahap paling lambat dari seluruh rangkaian tahap menuju pembentukan produk. Harus memprediksi hukum laju yang sama.

F. Katalisis

Katalis adalah zat yang meningkatkan laju reaksi kimia tanpa ikut terpakai. Katalis dapat bereaksi membentuk produk antara, tetapi akan diperoleh kembali dalam tahap berikutnya. Mari kita anggap bahwa reaksi berikut memiliki konstanta laju k tertentu dan energi aktivasi Ea.

A + B → C + D

Namun demikian, dengan kehadiran katalis, konstanta laju disebut konstanta laju katalitik. Maka berdasarkan definisi katalitik :

Laju berkatalis > laju tak berkatalis
           """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1yCUxo1nupeJQ4O6G9a00jCIXYmD-O_OP/view?usp=sharing)")
        
    if optionkimdas == "Kesetimbangan Kimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kesetimbangan Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
A. Konsep Kesetimbangan

Bila laju reaksi maju dan reaksi balik sama besar dan konsentrasi reaktan dan produk tidak lagi berubah seiring berjalannya waktu, maka tercapailah kesetimbangan kimia. Kesetimbangan kimia merupakan proses dinamik. Kesetimbangan antara dua fasa dari zat yang sama dinamakan kesetimbangan fisis karena perubahan yang terjadi hanyalah proses fisis. Dalam kasus ini,molekul H2O meninggalkan dan yang Kembali ke fasa cair sama banyaknya.

H20(l) ⇆ H20(g)

B. Konstanta Kesetimbangan

Kita dapat menggeneralisasi pembahasan ini dengan memperhatikan reaksi reversibel berikut.
aA + bB ⇆ cC + dD

Dimana a,b,c, dan d adalah koefisien stoikiometri untuk spesi spesi yang bereaksi dengan A,B,C,dan D. konstanta kesetimbangan untuk reaksi pada suhu tertentu ialah.

k = [C]c[D]d/[A]a[B]b

C. Beberapa Cara Untuk Menyatakan Konstanta Kesetimbangan
1.	Kesetimbangan Homogen : berlaku untuk reaksi yang semua spesi bereaksinya berada pada fasa yang sama.
2.	Kesetimbangan Heterogen : untuk reaksi yang melibatkan fasa yang berbeda.

D. Aturan-Aturan Penulisan Persamaan Konstanta Kesetimbangan
1.	Konsentrasi dari spesi spesi yang konsentrasi-reaksi di dalam fasa terkondensasi. Dinyatakan dalam mol per liter.
2.	Konsentrasi dari padatan murni, cairan murni dan pelarut tidak dituliskan dalam persamaan konstanta kesetimbangan.
3.	konstanta kesetimbangan tidak berdimensi.

E. Apa yang Dapat Diketahui Dari Konstanta Kesetimbangan
1.	Memprediksi arah reaksi.
2.	Menghitung konsentrasi kesetimbangan.

F. Faktor yang mempengaruhi Kesetimbangan Kimia.
1.	Asas Le Chatelier

    Ada satu aturan umum yang membantu kita memprediksi kearah mana reaksi kesetimbangan akan bergeser bila terjadi perubahan konsentrasi, tekanan. Volume, atau suhu. Asas le chatalier menyatakan bahwa “ jika suatu tekanan eksternal diberikan kepada suatu sistem kesetimbangan, sistem ini akan menyesuaikan diri sedemikian rupa untuk mengimbangi sebagian tekanan ini pada saat sistem mencoba setimbang Kembali.”

2.	Perubahan Konsentrasi
3.	Perubahan Tekanan dan Volume
4.	Perubahan suhu 
5.	Pengaruh katalis
        """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1fmK3R44BinpR9AvTBAwP2Gn8rBYCZ41o/view?usp=sharing)")
        
    if optionkimdas == "Asam Basa":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Asam Basa</h2>", unsafe_allow_html=True)
        st.write(
            """
A. Asam dan Basa Brønsted 
1.	Pasangan Asam Basa Konjugat

    Basa konjugat dari suatu asam Brønsted ialah spesi yang tersisa ketika satu proton pindah asam tersebut. Sebaliknya, suatu asam konjugat dihasilkan dari penambahan sebuah proton pada basa Brønsted. Setiap asam Brønsted memiliki satu basa konjugat dan setiap basa Brønsted memiliki satu asam konjugat.

B. Sifat Asam Basa dari Air

Salah satu sifat khas air ialah kemampuannya untuk bertindak baik sebagai asam maupun sebagai basa.Air berfungsi sebagai basa dalam reaksi dengan asam,dan pelarut ini berfungsi sebagai asam dalam reaksi basa. Air merupakan elektrolit yang sangat lemah sehingga air merupakan penghantar listrik yang buruk, meskipun hanya terionisasi sedikit.

   H2O(l)  ⇆ H+(aq) + OH-(aq)

Reaksi ini adakalanya disebut autoionisasi air. Untuk menjelaskan sifat asam basa dari air dari sudut pandang Brønsted sebagai berikut : 

   H2O + H2O ⇆ H3O+ +  OH-
   
   asam1 basa2  asam2   basa1

C. pH Suatu Ukuran Keasaman

Karena konsentrasi ion H+ dan OH-  dalam larutan air serinh kali sangat kecil dan kerena itu sulit diukur. Maka, seorang biokimiawan Denmark Soren Sorensen pada tahu 1909 mengajukan cara pengukuran yang lebih praktis yang disebut pH. pH suatu larutan didefinisikan sebagai logaritma negative dari konsentrasi ion Hidrogen(dalam mol per liter).

   pH = - log [H+]

Karena pH pada dasarnya hanyalah suatu cara untuk menyatakan suatu konsentrasi ion Hidrogen. Larutan asam dan basa pada suhu 25oC dapat di definisikan berdasarkan nilai pH nya. Seperti :

Larutan asam : pH < 7,00

Larutan basa  : pH > 7,00

Larutan netral : pH = 7,00

Rumus mencari pH asam = pH : -log[H+]

Rumus mencari pH basa = pOH : -log[OH-] lalu pH : 14,00-pOH

D. Kekuatan Asam dan Basa

Asam kuat ialah elektrolit kuat, yang kebanyakan digunakan untuk kebutuhan praktis karena dianggap terionisasi sempurna dalam air. Kebanyakan asam kuat adalah asam anorganik. Kebanyakan asam terionisasi hanya sedikit dalam air,asam seperti ini disebut asam lemah. Kekuatan asam lemah sangat beragam karena beragamnya derajat ionisasi. Terbatasnya ionisasi asam lemah berkaitan dengan konstanta kesetimbangan ionisasi.
Basa kuat ialah semua elektrolit kuat yang terionisasi sempurna dalam air. Sedangkan basa lemah adalah elekrolit lemah. Hal yang perlu diingat yaitu

1.	jika asamnya kuat, basa konjugat sangat lemah.
2.	H3O+ ialah asam terkuat yang dapat berada dalam laturan berair.
3.	Ion OH- ialah basa terkuat yang dapat berada dalam larutan berair. 

E. Asam Lemah dan Konstanta Ionisasi Asam

Mari kita asumsikan suatu asam monoprotik lemah HA, ionisasinya dalam air adalah :

    HA(aq) ⇆  H+(aq) + A-(aq)

Maka konstanta kesetimbangan untuk asam ini dinamakan konstanta kesetimbanga asam. Dinyatakan sebagai berikut :

     ka = [H+][A-] / [HA]

Dalam hal ini, tiga dasar tahapnya ialah:
1.	Nyatakan konsentrasi kesetimbangan dari semua spesi dalam konsentrasi awalnya dan satu bilangan tak diketahui x, yang menyatakan perubahan konsentrasi.
2.	Tuliskan konstanta ionisasi asam dalam konsentrasi-konsentrasi k setimbangnya. Dengan mengetahui nilai k maka kita dapat mengetahui nila x.
3.	Setelah menentukan x, hitunglah konsentrasi kesetimbangan dari semua spesi atau pH larutan.

1. Persen ionisasi

Cara lain untuk mengetahui kekuatan asam ialah mengukur persen ionisasi,

Persen ionisasi = (konsentrasi asam ionisasi/konsentrasi awal asam)x100%

Semakin kuat asam maka semakin besar nilai persen ionisasinya.

F. Basa Lemah dan Konstanta Ionisasi Basa

Sama seperti halnya pada asam lemah, Dimana nila kb konstanta kesetimbangan basa dinamakan konstanta ionisasi basa. 

G. Hubungan Antara Konstanta-Konstanta Ionisasi Asam-Basa Konjugat

Ketika dua reaksi ditambahkan untuk menghasilkan reaksi ketiga, konstanta kesetimbangan untuk reaksi ketiga adalah hasilkali antara konstanta-konstanta kesetimbangan dari kedua reaksi yang ditambahkan. Jadi, untuk pasangan asam konjugat-basa konjugat akan selalu berlaku.

H. Sifat Asam Basa dari Garam
1.	Garam yang menghasilkan larutan netral.
2.	Garam yang menghasilkan larutan basa.
3.	Garam yang menghasilkan larutan asam.
4.	Hidrolis ion logam
5.	Garam yang kation dan anion nya terhidrolisis.
        """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1xzEM_sGSkXiZ7E8GhEnm-FFQxeXp3lmL/view?usp=sharing)")
         

            
            
  

                
#Materi Analisis Jenis            
with tab_2:
    optionanjen = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Reaksi Kimia dan Persamaan Reaksi", "Satuan Konsentrasi", "Pemisahan Kation Golongan I-V", "Identifikasi Zat Dengan Cara Kering", "Pemisahan Anion Golongan I-V", "Pembuatan Larutan",))
    if optionanjen == "Reaksi Kimia dan Persamaan Reaksi":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Reaksi Kimia dan Persamaan Reaksi</h2>", unsafe_allow_html=True)
        st.write(
            """
                 Reaksi kimia adalah proses dimana zat baru, yang disebut produk terbentuk dari sejumlah zat 
asal, yang disebut sebagai reaktan, gambaran zat-zat yang terlibat dalam suatu proses reaksi kimia dapat dinyatakan sebagai persamaan reaksi kimia

 A + B   →  C + D
 
Reaktan     Produk

Persamaan ini mengandung rumus dari zat-zat yang bereaksi pada sisi sebelah kiri (reaktan), dan rumus dari hasil reaksinya pada sisi sebelah kanan (produk). Penulisan reaksi Kimia memiliki  tiga  tahapan  prosedur  yang  sistematis  yang  perlu  diperhatikan  untuk memudahkan penulisan  persamaan  reaksi  kimia, ketiga tahap tersebut adalah sebagai berikut:
1.	Tuliskan nama dari reaktan dan produk

    kalsium hidroksida + asam fosfat → kalsium fosfat 

2.	Ubahlah Nama dari reaktan dan produk menjadi rumus kimia

    Ca(OH)2 + H3PO4 → Ca3(PO4)2 + H2O

3.	Setimbangkan rumus  kimia  untuk  memperoleh persamaan  reaksi  kimia, dengan mengatur koefisien reaksi

    3Ca(OH)2 + 2H3PO4 → Ca3(PO4)2 + 6H2O

Syarat-syarat berlangsungnya suatu reaksi kimia yaitu terjadi perubahan bentuk wujud zat (mengendap, melarut, atau terurai menjadi gas),warna, suhu, daya hantar atau terbentuk elektrolit lemah.
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Reaksi Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
1.	Reaksi penetralan / reaksi penggaraman

    Reaksi penetralan disebut juga reaksi asam basa. reaksi penetralan adalah reaksi yang membentuk unsur bersifat netral yaitu air (H2O) yang berasal dari zat asam yang melepaskan ion (H +) dengan zat basa yang melepaskan ion (OH-)

    a.	     Oksida asam + oksida basa → garam
           
    CO2 + 2NaOH → Na2CO3 + H2O
           
    b.	     Oksida basa + asam → garam + air
           
    K2O + HCl → KCl + H2O
           
    c.	     Oksida logam (oksida basa)
     
    Na2O + H2O → 2NaOH
     
    d.	     Oksida non logam (oksida asam)
     
    CO2 + H2O → H2CO3

2.	Reaksi metatesis

    Reaksi Metatesis adalah reaksi pertukaran pasangan ion dari dua elektrolit. Pada reaksi ini, setidaknya satu produk reaksi akan membentuk endapan, gas atau elektrolit lemah.
Garam 1 + garam 2 → garam 3 + garam 4

    Contoh: 
    
    AgNO3 (aq) + NaCl (aq) → AgCl(s) + NaNO3 (aq)

3.	Reaksi redoks

    Reaksi reduksi-oksidasi (ada perubahan biloks/ bilangan oksidasi). Dalam reaksi redoks atom yang menyumbangkan electron dioksidasi dan atom yang menerima electron direduksi.

    H2 + F2 → 2HF
    
    Untuk membentuk senyawa hidrogen fluorida, molekul H2 melepaskan 2 elektron menjadi 2H+ : H2 → 2H+ + 2e-, sedangkan molekul F2 menangkap/mengikat 2 elektron, menjadi 2F- : F2 + 2e- → 2F-.

4.	Reaksi pengendapan

    Endapan adalah zat yang memisahkan diri sebagai suatu fase padat keluar dari larutan, endapan terbentuk jika larutan menjadi terlalu jenuh dengan zat yang bersangkutan, kelarutan (s) suatu endapan, menurut definisi adalah sama dengan konsentrasi si molar dari larutan jenuhnya. Kelarutan bergantung pada berbagai kondisi, seperti suhu, tekanan, konsentrasi bahan-bahan lain dalam larutan itu, dan pada komposisi pelarutnya.

    Contoh: 
    
    Pb(NO3)2 (aq) + 2 NaI(aq) → PbI2(s) + 2NaNO3(aq)

5.	Reaksi kompleks

    Suatu ion (atau molekul) Kompleks terdiri dari satu Atom (ion) pusat dan sejumlah ligan dan terikat erat dengan atom (ion) pusat itu.

    Contoh: 
    
    [Co(NH3)6]3+ + 6H3O+ → [Co(H2O)6]3+ + 6NH4+
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kelarutan Elektrolit Dalam Air</h2>", unsafe_allow_html=True)
        st.write(
            """
Semua asam larut, Sebagian besar basa tidak larut kecuali ; NaOH, KOH,NH4OH, Ba(OH)2 , Ca(OH)2, Sr(OH)2 larut.
            
Garam sulfat (SO42-) umumnya larut, kecuali: BaSO4, PbSO4, Ag2SO4 tidak larut.
            
Garam klorida (Cl-), bromida (Br-), iodida(I-) umumnya larut kecuali : AgCl, PbCl2, Hg2Cl2, AgBr, PbBr2, Hg2Br2, AgI, PbI2, Hg2I2, tidak larut. 
            
Garam fluorida (F-) umumnya larut kecuali: MgF2, CaF2, dan BaF2 tidak larut.

Garam kalium (K+), natrium (Na+), ammonium (NH4+), Nitrat (NO3-), asetat(CH3COO-), hipoklorit (ClO-), klorit (ClO2-),klorat ( ClO3-), perklorat (ClO4-), Bromat(BrO3-), dan Iodat (IO3-) semuanya larut. 

Garam sulfida (S2-) umumnya tidak larut kecuali : Na2S, K2S , (NH4)2S, MgS, CaS, BaS larut. 

Garam- garam (CO32-, CrO42-, PO43-) umumnya tidak larut kecuali garam K+, Na+ dan NH4+.

Asam yang berupa gas : H2S, asam yang terurai menjadi gas:H2CO3 H2O + CO2 (g) H2SO3 H2O + SO2 (g) 
Basa yang terurai menjadi gas : NH4OH H2O + NH3 (g).
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Tata Nama Senyawa Kimia</h2>", unsafe_allow_html=True)
        st.write(
            """
Syarat_syarat dalam penamaan senyawa kimia adalaha sebagai berikut:
1.	Senyawa yang terdiri dari unsur logam dan non logam: nama kation diikuti nama anion dengan akhiran-ida

    NaCl = Natrium klorida

    MgCl2 = Magnesium klorida

2.	Senyawa yang terdiri dari unsur non logam dan non logam : nama unsur diikuti dengan awalan mono(1), di(2), tri(3), tetra(4), penta (5), heksa (6), penta (7), okta (8),
nona(9), deka(10), dst....

    Contoh:

    SO2 = sulfur dioksida

    N2O5 = dinitrogen pentaoksida

3.	Senyawa yang mengandung logam atau kation yang memiliki 2 bilangan oksidasi maka : nama kation dengan akhiran – i, untuk biloks yang tinggi dan akhiran –o, untuk biloks rendah, atau nama kation, dengan nama umum (dalam bahasa indonesia) diikuti muatan kation dengan angka romawi.

    Contoh:

    FeCl2 = Ferro klorida atau besi (II) klorida

    FeCl3 = Ferri klorida atau besi (III) klorida
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1nNtSU-ZxXD4xd_w0tBYA09KwL6vMIht3/view?usp=sharing)")
        
    if optionanjen == "Satuan Konsentrasi":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Satuan Konsentrasi</h2>", unsafe_allow_html=True)
        imageAnjen1 = Image.open('Resource/image/Anjen/images.jpeg')
        st.image(imageAnjen1, caption = "Gambar 1. Konsep Mol (Sumber : temukanpengertian.com )")
        st.write(
            """ 
Mol = g/BM = g/Mr = g/Ar    
            
g = massa (gram)

BM = berat molekul (g/mol atau mg/mmol)

Contoh:

Hitung berapakah mol molekul yang terdapat dalam 10 gram glukosa (C6H12O6), diketahui Ar C = 12, O = 16, serta H = 1.

Jawaban:
Mr glukosa = (6 x 12) + (12 x 1) + (6 x 16) = 180

Mol = 10/180  = 0,05
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Hukum proust</h2>", unsafe_allow_html=True)
        st.write("Bunyi hukum Proust  “perbandingan massa unsur-unsur penyusun suatu senyawa selalu tetap”")
        imageAnjen2 = Image.open('Resource/image/Anjen/images1.jpg')
        st.image(imageAnjen2)
        st.write(
            """
Contoh :
   
Berapa % kadar Fe dalam Fe2O3  
   
Jawab :
   
% = ((2 × 56 g/mol) )/(160 g/mol × 100) = 70 %
            """)

        st.markdown("<h2 style='text-align: center; color: raisin black;'>Konsep ekuivalen & Berat Ekuivalen (BE)</h2>", unsafe_allow_html=True)
        st.write(
            """
**Rumus ekuivalen dan berat ekuivalen**
        
    grek = g/BE
         
    BE = BM/a
    
dengan:
         
BE = berat ekuivalen (g/grek atau mg/mgrek)
  
a = valensi yang nilainya tergantung reaksi
  
**Berat Ekuivalen (BE) Reaksi asam basa**

    BE asam = (BM asam)/(jumlah H+)          

    BE Basa = (BM asam)/(jumlah OH-)
        
**Berat Ekuivalen (BE) Reaksi redoks**
  
    BE zat = (BM zat)/(Jumlah elektron yang terlibat)
        
**Berat Ekuivalen (BE) Reaksi penggaraman**
  
    BE garam = (BM garam)/(Muatan anion × jumlah anion )
  
    BE garam = (BM garam)/(Muatan kation × jumlah kation )
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Molaritas (M)</h2>", unsafe_allow_html=True)
        st.write(
            """
Molaritas menyatakan banyaknya mol solute yang terdapat dalam 1 liter atau 1000 mL larutan
Rumus Molaritas : 

       M = mol/L = G/Mr × 1000/volume = g/(BM ×L)
       
Contoh : 

Berapa Normalitas H2SO4 dengan Molaritas = 0,25 M?

Jawaban :

N = 0,25 × 2 = 0,5 N
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Normalitas (N)</h2>", unsafe_allow_html=True)
        st.write(
            """
Normalitas adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan

      N =  greak/L = g/(BE ×L)
      
Contoh : 

Berapa Normalitas H2SO4 dengan Molaritas = 0,25 M?

Jawaban :

N = 0,25 × 2 = 0,5 N
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kadar Larutan Dalam Persen(%)</h2>", unsafe_allow_html=True)
        st.write(
            """
**Persen berat/berat (% b/b)**
      
      % b/b = (g solut)/(100 g larutan)
      
Contoh : 

Larutan NaOH 50% b/b = (50 g NaOH)/(100 g larutan)

**Persen volume (% v/v)**

      %v/v = (mL solut)/(100 mL solut)
      
Contoh : 

Alkohol 70 % (v/v) = (70 mL)/(100 mL larutan)

**Persen berat / volume (% b/v)**

      %b/v = (g solut)/(100 mL larutn) 
      
Contoh : 

NaCl 60 % (b/v) = (60 g)/(100 mL)
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Bagian per sejuta (ppm : parts per million) & Bagian Permiliar (ppb:parts per billion)</h2>", unsafe_allow_html=True)
        st.write(
            """
Bagian tiap juta (ppm) menyatakan berapa jumlah bagian satu komponen dalam 1 juta bagian campuran

      ppm = mg/L = mg/kg
      
ppb = parts per billion dalam bahasa Indonesia bpm = bagian per milliar, berarti kandungan atau Konsentrasi dalam ppb jauh lebih encer dibandingkan dengan Konsentrasi dalam ppm. 
        
      ppb=1 µg/kg = 1 µL/L
      
contoh:

Hitunglah besar ppm 10 liter air apabila dilarutkan Natrium Hidroksida atau NaOH sebanyak 1500 mg.

jawab

ppm= mg/L = 1500 mg/10 L
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pengenceran</h2>", unsafe_allow_html=True)
        st.write(
            """
Rumus pengenceran :

(C1 x V1) sebelum diencerkan = (C2 x V2) setelah diencerkan

C adalah konsentrasi larutan (M, N, ppm, dan %), V adalahvolume larutan (L atau mL)
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Hubungan antar satuan</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Hubungan mol dengan grek = grek = mol x a

•	Hubungan molaritas dengan normalitas = N = M x a

•	Hubungan % (b/b) dengan % b/v = % (b/v) = % b/b x bj bj = berat jenis atau density

•	Hubungan % dengan ppm = 1% = 104 ppm
      
            
Daftar Pustaka:
            
Da lopez, Yos F. 2017. Konsentrasi Larutan dalam Satuan Kimia. Nusa Tenggara Timur (NTT): Politeknik Pertanian Negeri Kupang

Wardaya, Anton. 2014. Modul, Rumus, & Soal Hukum Proust (Hukum Perbandingan Tetap). Jakarta Barat: wardayacollege
""")
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1YEEzMSlhS6j2v2EYRyXd5JQHVOsrZ_zD/view?usp=sharing)")

    if optionanjen == "Pemisahan Kation Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Kation Golongan I-V</h2>", unsafe_allow_html=True)
        st.write(
            """
            Kation-kation diklasifikasikan dalam 5 golongan berdasarkan sifat-sifat kation itu terhadap beberapa reagensia, penggolongan ini didasarkan pada terbentuk atau tidaknya endapan jika suatu kation bereaksi dengan reagensia tertentu, reagensia golongan yang dipakai untuk klasifikasi kation yang paling umum, adalah asam klorida, hidrogen sulfida, amonium sulfida dan amonium karbonat.

     Proses analisis kation dan anion dilakukan dengan dua cara yaitu pemisahan dan identifikasi. Pemisahan dilakukan dengan mengendapkan kation dari larutannya. Endapan yang dihasilkan dipisahkan dengan mencuci larutannya dan dibuat larutan dengan jalan mengaduk menggunakan alat sentrifuge lalu membagi dua hasil penyaringan. Larutan yang masih mengandung kation lain lalu diendapkan juga sehingga terbentuk grup kation baru. Apabila di dalam grup tersebut masih terdapat kation lain, proses pengendapan dilakukan lagi sehingga tertinggal hanya satu kation saja.

     Jadi boleh dikatakan bahwa klasifikasi kation yang paling umum didasarkan atas perbedaan kelarutan dari klorida, sulfida, dan karbonat dari kation tersebut. Kelima golongan Kation dan ciri khas golongan-golongan ini adalah sebagai berikut:
            """)
        imageAnjen1 = Image.open('Resource/image/Anjen/bagan.jpg')
        st.image(imageAnjen1, caption = "Gambar 1. Bagan Pemisahan Kation (Sumber: Penuntun Praktik Analisis Jenis)")
        st.write(
            """
1.	Golongan I : Kation grup ini membentuk endapan dengan asam klorida encer. Kation Golongan I yaitu: Ag+, Hg2 2+, Pb2+
2.	Golongan II : Kation grup ini adalah kation-kation yang tidak bereaksi dengan asam klorida, namun membentuk endapan dengan asam sulfida dalam suasana asam mineral encer.
    
    Gol II A : Cu2+, Cd2+, Bi3+,
    
    Gol II B : As3+, As5+, Sb3+, Sb5+, Sn2+, Sn4+
    
    Sulfida dari kation dalam golongan IIA tak dapat larut dalam amonium polisufida, sulfida dari kation dalam golongan IIB justru dapat larut.
    
3.	Golongan III : Kation grup ini tidak bereaksi dengan asam klorida encer maupun dengan asam sulfida dalam suasana asam mineral encer. Namun, kation ini membentuk endapan dengan amonium sulfida dalam suasana netral atau amoniakal.
    
    Gol III A : Fe2+, Fe3+, Al3+, Cr (III), Cr (VI)
    
    Gol III B : Zn2+, Co2+, Ni2+, Mn (II), Mn (IV)
    
4.	Golongan IV : Kation yang termasuk dalam grup ini adalah kation yang tidak bereaksi dengan pereaksi-pereaksi Golongan I, II dan III. Kation-kation ini membentuk endapan dengan amonium karbonat dengan adanya amonium klorida, dalam suasana netral atau sedikit asam.
    
    Gol IV : Ba2+, Ca2+, Sr2+
    
    Beberapa sistem klasifikasi golongan meniadakan pemakaian amonium klorida disamping amonium karbonat sebagai reagensia golongan; dalam hal ini, magnesium harus juga dimasukkan ke dalam golongan ini. Tetapi, karena dalam pengerjaan analisis yang sistematis, amonium klorida akan terdapat banyak sekali ketika kation-kation golongan keempat hendak diendapkan, adalah lebih logis untuk tidak memasukkan magnesium ke dalam Golongan IV.

5.	Golongan V : Kation-kation yang umum, yang tidak bereaksi dengan pereaksi pereaksi golongan I, II, III dan IV merupakan golongan kation yang terakhir, yang meliputi ion-ion magnesium, natrium, kalium, amoium, lilitium dan hidrogen.
   """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan I</h2>", unsafe_allow_html=True)
        st.write("""
     Kation golongan I yaitu Pb2+, Hg2 2+, dan Ag+ . Kation ini membentuk endapan putih ketika bereaksi dengan HCl encer. Endapan yaang terbentuk antara lain; PbCl2, Hg2Cl2, dan AgCl. Berikut reaksi pengendapan kation golongan I oleh asam klorida encer.
   
• Ag+ (aq) + Cl(aq) → AgCl(s) (endapan putih)
      
• Pb2+ (aq) + 2 Cl(aq) → PbCl2(s) (endapan putih)
    
• Hg2 2+ (aq) + 2Cl(aq) → Hg2Cl2(s) (endapan putih)
    """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan II</h2>", unsafe_allow_html=True)
        st.write ("Setelah ditambahkan hidrogen sulfida, kemudian saring menghasilkan filtrat dan residu (Golongan III). Filtrat ini mungkin terdiri dari sulfida-sulfida logam logam IIA (HgS, PbS, Bi2S3, CuS) dan sulfida-sulfda logam golongan IIB (As2S3, Sb2S3, Sb2S5, SnS2). Pemisahan golongan IIA dan IIB dilakukan dengan mencuci dengan sulfida yang diendapkan dengan sedikit larutan NH4Cl yang telah dijenuhi H2S.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan III</h2>", unsafe_allow_html=True)
        st.write("Pemisahan kation-kation golongan III dan golongan-golongan lain yaitu dengan menambahkan H2O dan Panaskan, kemudian saring menghasilkan residu dan filtrat (Golongan IV). Endapan yang dihasilkan tersebut ditambahkan sedikit air, NH4Cl serta larutan NH3 dan panaskan hingga mendidih, kemudian saring menghasilkan residu dan filtrat. Residu mungkin mengandung golongan III.A yaitu MnO- , Fe(OH)3, Cr(OH)3, dan Al(OH)3, dan filtrat mungkin mengandung CoS, NiS, MnS, dan ZnS.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan kation golongan IV</h2>", unsafe_allow_html=True)
        st. write("Hasil filtrat yang diperoleh dari pemisahan kation golongan III, mungkin mengandung golongan IV dan V. Cara pemisahannya dilakukan dengan penambahan reagen natrium heksanitritokobaltat(III) sebanyak 5 mL, kemudian saring menghasilkan residu dan filtrat (mungkin golongan V). Pemisahan Kation Golongan IV dengan Metode Sulfat yaitu residu yang dihasilkan mungkin mengandung BaCO3, SrCO3 dan CaCO3")
        st.markdown(
            """
            Daftar Pustaka:
            
            Svehla,G.1990._Buku Teks Analisis Anorganik Kualitatif Makro dan Semimikro_.Jakarta: PT. Kalman Media Pustaka 
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1IdfRtJEGT5yQwW5ezAqdxIRJvzFvoRx7/view?usp=sharing)")
        
 
    if optionanjen == "Identifikasi Zat Dengan Cara Kering":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Identifikasi Zat Dengan Cara Kering</h2>", unsafe_allow_html=True)
        st.write(
            """
            Analisis kualitatif secara konvensional dapat dilakukan secara visual melalui 2 uji yaitu uji reaksi kering dan uji reaksi basah.Uji reaksi kering adalah pengujian yang diterapkan dalam keadaan kering dan tanpa proses pelarutan sampel, cara uji reaksi kering antara lain: Sifat fisik, Reaksi nyala, Pipa tiup, Mutiara boraks
Pengamatan dalam uji kering meliputi
•	Bentuk
•	Warna
•	Bau
•	Warna nyala 

**Teknik uji dalam uji reaksi kering yaitu:**

1.	Sifat fisik

    Dalam sifat fisik yang perlu diperhatikan:
    
    -	Pengamatan bentuk
    
        bentuk harus diperhatikan secara seksama,apakah berupa padatan atau cairan
        
    -	Pengamatan warna
    
        beberapa senyawa berwarna yang secara umum dijumpai 

2.	Reaksi Nyala
""")
        imageAnjen1 = Image.open('Resource/image/Anjen/Uji_nyala.jpg')
        st.image(imageAnjen1, caption = "Gambar 1. Uji nyala (Sumber: yuninainggolan.wordpress)")
        st.write(
            """    
    Uji nyala api adalah suatu prosedur analisis yang digunakan dalam ilmukimia untuk mendeteksi keberadaan unsur tertentu, terutama ion logam, berdasarkan karakteristik spektrum emisi masing-masing unsur, ide pengujian ini adalah bahwa atom-atom sampel menguap dan karena panas, mereka mengemisikan sinar ketika berada dalam nyala api.

    Prosedur Kerja:
    1.	Disiapkan kristal NaCl dalam kaca arloji.
    2.	Diisi 2 tabung reaksi masing-masing dengan 1 mL HCl pekat.
    3.	Dicelupkan ujung kawat nikrom dalam tabung reaksi 1 dan dimasukkan dalam nyala api bunsen. Dilakukan hal ini sampai kawat tidak memberikan warna lain.
    4.	Dicelupkan ujung   kawat  nikrom   tersebut   dalam  tabung  reaksi  2 kemudian dalam kristal NaCl.
    5.	Diamati   warna  nyala   yang  terjadi  dan   dicatat   hasil   pengamatan kalian.
    6.	Diulangi kegiatan yang sama untuk kristal yang lain. Disiapkan kristal NaCl dalam kaca arloji.
""")
        imageAnjen2 = Image.open('Resource/image/Anjen/Warna.jpg')
        st.image(imageAnjen2)
        st.write(
            """
3.	Uji Pipa Tiup

    Uji pipa tiup bertujuan untuk membebaskan logam tertentu dari sampel tertentu yang memiliki warna yang khas
            """)
        imageAnjen3 = Image.open('Resource/image/Anjen/Pipa_tiup.jpeg')
        st.image(imageAnjen3) 
        st.write(
            """
    Prosedur kerja
    1.  Campurkan di dalam mortar garam yang akan di periksa dengan Na2CO3(perbandingan 1:2) gerus sampai halus.Buat gerukan pada permukaan arang kayu.
    2.  Nyalakan bunsen perlahan sampai di dapat nyala api TB. Kemudian panaskan campuran yang ada
    3.  Siapkan sebongkah arang, lubangi arang kurang lebih 1,5cm. Sampel yang sebelumnya dilarutkan  dengan pereaksi dalam plat tetes dimasukan kedalam arang.
    4.  Arang yang telah diisi sampel simpan diatas kassa asbes dan nyalakan api.
    5.  Tiupkan dengan pipa tiup, arahkan pada zat sampai semuanya bereaksi. Ambil sampel yg ada dalam arang dan masukan ke dalam tabung reaksi lalu tambahkan pereaksi tertentu.
""")
        imageAnjen4 = Image.open('Resource/image/Anjen/Nyala_api.jpg')
        st.image(imageAnjen4)
        st.write("4.	Uji Mutiara Boraks")
        imageAnjen5 = Image.open('Resource/image/Anjen/boraks.jpeg')
        st.image(imageAnjen5, caption = "Gambar 3. Uji Mutiara Boraks (Sumber: davin tiska abriani)")
        st.write(
            """
pengamatan warna nyala sampel pada manik boraks yang dipanasi diatas nyala api oksidasi dan reduksi baik dalam dingin ataupun panas dapat diperoleh warna yang menunjukkan apakah zat itu mengandungkation atau anion. Jika sampel mengandung anion logam maka saat dipanaskan pada nyala api akanmengeluarkan warna nyala mutiara boraks yang spesifik.
     
Prosedur Kerja
1.  Kawat platina dipijarkan (sampai merah)
2.  Kawat dimasukkan ke dalam boraks (bubuk halus)
3.  Kawat dipanaskan lagi sampai terbentuk butiran tak berwarna dan transpara (tembus cahaya),
4.  Mutiara panas disentuhkan ke zat uji
5.  Dipanaskan dalam api pengoksidasi dan api pereduksi
""")
        imageAnjen6 = Image.open('Resource/image/Anjen/Warna_boraks.png')
        st.image(imageAnjen6)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1ScSsWu9PxEWEXU6g3RbpDOOg7V_5-fhF/view?usp=sharing)")
        
    if optionanjen == "Pemisahan Anion Golongan I-V":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pemisahan Anion Golongan I-V</h2>", unsafe_allow_html=True)
        st.write("Klasifikasi anion ini adalah salah satu contoh pengelompokan anion yang dibagi berdasarkan reaksinya dengan asam klorida encer (HCl(aq) ) dan perbedaan kelarutannya sebagai garam barium dan perak. Empat golongan anion dan karakteristiknya adalah sebagai berikut:")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan I</h2>", unsafe_allow_html=True)  
        st.write(
            """
            Anion golongan ini bereaksi dengan HCl(aq) menghasilkan gas atau endapan, yaitu karbonat, silikat, sulfida, sulfit, dan tiosulfat
  
Reaksi Karbonat:
            
            CO3 2- + 2H+ → CO2(g) + H2O
            
Reaksi Silikat:

           SiO3 2- + 2H+ → H2SiO3(s)
           
Reaksi Sulfida:

           S2- + 2H+ → H2S(g)
           
Reaksi Sulfit:

           SO3 2- + 2H+ → SO2(g) + H2O
           
Reaksi Tiosulfat:

           S2O3 2- + 2H+ → S(s) + SO2(g) + H2O
           """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan II</h2>", unsafe_allow_html=True)
        st.write( 
             """
             Anion golongan ini tidak bereaksi dengan HCl(aq) namun membentuk endapan dengan ion barium pada kondisi netral. Anion golongan ini adalah sulfat, fosfat, fluorida, dan borat

Reaksi sulfat: 

    SO4 2- + Ba2+ → BaSO4(s)

Reaksi Fosfat:

    2F - + Ba2+ → BaF2(s)

Reaksi Borat:

    B4O7 2- + 2Ba2+ + H2O → 2Ba(BO2 )2(s) + 2H
""")

        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan III</h2>", unsafe_allow_html=True)
        st.write(
            """
            Anion golongan ini tidak bereraksi dengan HCl(aq) maupun ion barium, namun membentuk endapan dengan ion perak dalam media asam nitrat encer. Anion golongan ini adalah klorida, bromida, iodida, dan tiosianat.
            
Reaksi Klorida: 

          Cl- + Ag+ → AgCl(s)
          
Reaksi Bromida:

         Br- + Ag+ → AgBr(s)
         
Reaksi Iodida: 

         I - + Ag+ → AgI(s)
         
Reaksi Tiosianat:

         SCN- + Ag+ → AgSCN(s) 
         """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Anion Golongan IV</h2>", unsafe_allow_html=True)
        st.write("Anion-anion yang tidak bereaksi dengan pereaksi-pereaksi di atas dikelompokkan pada golongan ini, yaitu ion nitrit, nitrat, dan klorat")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Identifikasi Produk yang mudah menguap</h2>", unsafe_allow_html=True)
        st.write(
            """
Gas yang dilepaskan dengan HCl atau H2SO4 encer : (karbonat, bikarbonat, sulfit, tiosulfat, sulfida, nitrit, hipoklorit, sianida, dan sianat) Gas atau uap asam yang dilepaskan dengan H2SO4 pekat : (fluorida, heksafluorosilikat, klorida, bromida, iodida, klorat, perklorat, permanganat, bromat, borat, heksasianoferat (II), heksasianoferat (III), tiosianat, format, asetat, oksalat, tartrat dan sitrat)

Contoh Reaksi anion karbonat (CO32-) dari larutan garam natrium karbonat penta hidrat (Na2CO3.10H2O) dengan HCl encer:

         CO32-(aq) +2H+(aq)=CO2+ H2O(l)
         
 Identifikasi dilihat dari :
- Berbuih
- Mengeruhkan air kapur :

    CO2(s)+ Ca2+(aq) + 2OH-(aq)=CaCO3(s)putih + H2O(l)

    CO2(s)+ Ba2+(aq) + 2OH-(aq)=BaCO3(s)putih + H2O(l)

Contoh Reaksi anion sulfit (SO32-) dari larutan garam natrium sulfit hepta hidrat (Na2SO3.7H2O) dengan HCl encer:

    SO32-(aq) + 2H+(aq)=SO2(aq) + H2O(l)

Identifikasi dilihat dari :
- Bau belerang terbakar yang menyesakkan nafas
- Warna hijau (terbentuk dari ion Cr3+ yang dihasilkan jika sehelai kertas saring yang telah dibasahi larutan K2Cr2O7 yang telah diasamkan,dipegang diatas mulut tabung reaksi.
            """)
        st.markdown(
            """
Daftar Pustaka:
            
Svehla,G.1990._Buku Teks Analisis Anorganik Kualitatif Makro dan Semimikro_. Jakarta: PT. Kalman Media Pustaka
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1HJm0txtr--xvcj2rKRQ9bOhwIgSabtu0/view?usp=sharing)")
        
        
    if optionanjen == "Pembuatan Larutan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pembuatan Larutan</h2>", unsafe_allow_html=True)
        st.write("Cara membuat larutan perlu diperhatikan,yaitu cara membuat larutan  dari bahan  cair atau padat dengan menggunakan  konsentrasi tertentu. Larutan adalah campuran homogen dari dua atau lebih zat  yang berbeda komposisinya. Suatu larutan dalam volume kecil disebut zat  terlarut. Pelarut didefinisikan sebagai zat yang jumlahnya melebihi zat lain.")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Cara Pembuatan Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Menimbang kristal senyawa atau memipet dari larutan pekat

•	Hasil penimbangan dan pemipetan dilarutkan dalam volume tertentu

•	Larutan yang dibuat harus dengan konsentrasi tertentu

•	Larutan disimpan dalam botol/ wadah yang sesuai

•	Botol atau wadah penyimpanan harus diberi label
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Informasi Yang Ada Pada Label</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Nama senyawa kimia/ Rumus kimia senyawa dari larutan yang dibuat

•	Konsentrasi larutan

•	Tanggal pembuatan

•	Tanggal kadaluarsa

•	Sifat bahan bahan kimia

•	Inisial pembuat larutan
""")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alat Yang Digunakan Untuk Pembuatan Larutan</h2>", unsafe_allow_html=True)
        st.write(
            """
•	Labu takar

•	Beaker glass

•	Kaca arloji

•	Pipet

•	Batang pengaduk

•	Labu semprot

•	Corong

•	Bulp
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/12ZVIMB3NRyBopmbTfveV_GPcmlg4wltK/view?usp=sharing)")
        

        


      
#Materi Titrimetri
with tab_3:
    optiontitri = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pengenalan Analisis Titrimetri","Asidimetri-Alkalimetri","Asidimetri","Alkalimetri","Permanganometri","Iodometri"))
    
    if optiontitri == "Pengenalan Analisis Titrimetri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pengenalan Analisis Titrimetri</h2>", unsafe_allow_html=True)
        st.write(
            """
            **Definisi**

Analisis volumetri /analisis titrimetri adalah teknis analisis yang berdasarkan pada volume suatu larutan yang sudah diketahui konsentrasinya yang diperlukan untuk bereaksi sempurna dengan sejumlah tertentu komponen cuplikan (sampel).
             """)
        imageT1 = Image.open('Resource/image/Titri/Titri_1.png')
        st.image(imageT1)
        st.write(
            """
        Istilah dalam analisis volumetri/titrimetri:
            
•	Titrasi adalah proses penambahan larutan standar dari buret sedikit demi sedikit sampai jumlah zat yang direaksikan tepat ekuivalen satu sama lain.

•	Titran adalah zat yang diketahui konsentrasinya yang digunakan untuk menitar zat lain

•	Titrat adalah zat yang dititrasi

•	Titik ekuivalen (setara) adalah titik pada saat titran yang ditambahkan tepat ekuivalen dengan titrat maka penambahan titran harus dihentikan

•	Titik akhir titrasi adalah titik pada saat titrasi dihentikan yang ditandai oleh perubahan warna dari indikator

•	Indikator : Zat yang ditambahkan ke dalam titrat sebagai penunjuk titik akhir titrasi

•	Larutan standar (larutan baku) adalah larutan yang konsentrasinya diketahui secara pasti


**Prinsip /reaksi titrimetri**

•	aA + tT → produk 

A = Analit

T = zat penitar (titran)

a dan t = jumlah molekul / koefisien reaksi

•	Prinsip reaksi titrasi volumetri :

mgrek titran = mgrek titrat


Syarat-syarat reaksi dapat digunakan sebagai reaksi titrasi:
1.	Berlangsung sempurna, tunggal dan menurut persamaan yang jelas.
2.	Reaksi berlangsung cepat
3.	Ada penunjuk titik akhir ( indikator)
4.	Larutan baku yang direaksikan dengan analit harus mudah didapat dan sederhana menggunakannya, harus stabil sehingga konsentrasinya tidak berubah sewaktu disimpan.

**Problema dalam titrasi:**

a.	
1.	Cara menentukan titik akhir harus tepat
2.	Cara menghitung jumlah analit
3.	Cara menentukan konsentrasi larutan baku dengan teliti
4.	Titrasi yang baik,perubahan: warna/kekeruhan harus terjadi tepat pada saat titran telah ekuivalen dengan titrat, titik ekuivalen tepat sama dengan titik akhir
    
b.	Umumnya titik ekuivalen tidak sama dengan titik akhir sehingga terjadi kesalahan titrasi. Kesalahan yang terjadi tidak boleh lebih dari 0,1 %

c.	Kesalahan positif : Jumlah yang dipakai lebih dari yang sesungguhnya diperlukan untuk ekuivalen

**Penggolongan titrasi berdasarkan reaksinya**
1.	Titrasi Asam-Basa (Asidimetri-alkalimetri)
2.	Titrasi Redoks (Permanganometri dan Iodometri)
3.	Titrasi Pengendapan (Argentometri)
4.	Titrasi Kompleksometri

**Berdasarkan cara titrasi**
1.	Titrasi langsung, 
cara ini dilakukan dengan melakukan titrasi langsung terhadap zat yang akan ditetapkan. Cara ini mudah, cepat, dan sederhana
2.	Titrasi tidak langsung, 
analit direaksikan dengan suatu pereaksi ,kemudian hasil reaksi di titrasi (analit tidak langsung terlibat dalam titrasi)
3.	Titrasi balik /titrasi kembali ( _back titration_ ), 
analit direaksikan dengan pereaksi berlebih. Dan kelebihan pereaksi di titrasi
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1vNo_GQjerR3Bm_57VGHPAJMYzWoPf7Ud/view?usp=sharing)")          
        
    if optiontitri == "Iodometri":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Iodometri</h2>", unsafe_allow_html=True)
        st.write(
          """
**Iodometri (titrasi tidak langsung)**
       
Analit → Oksidator (KIO3, K2Cr2O7)
       
       Oks(analit) + KI ⇋ I2 + Red(analit)
       
       I2 + 2S2O3^2- ⇋ 2I^- + S4O6^2-
       
       IO3^- + 5I^- + 6H^+ ⇋ 3I2 + 3H2O (pH rendah)
       
       Cr2O7^2- + 6I^- + 14H+ ⇋ 2Cr3^+ + 3I2 + 7H2O (pH rendah)
       
Reaksi I2 dengan S2O3^2- berlangsung sempurna dan cepat 
       
Reaksi unik karena oksidator lain tidak mengubah S2O3^2- menjadi S4O6^2- melainkan menjadi SO32^- dan SO42^-
       
**Titrasi tanpa Indikator :**
       
• Lenyapnya warna I2 (coklat tua - kuning - bening)
       
**Titrasi dengan Indikator Amilum/kanji :**
       
• Lenyapnya warna I2 (coklat tua - kuning - biru tua - bening)
       
Amilum + I2 membentuk kompleks berwarna biru tua, sangat jelas walaupun I2 sedikit sekali
       
Titik akhir : iod yang terikat dengan amilum itu pun hilang bereaksi dengan titran (S2O3^2-) sehingga warna biru hilang
       
Titran Na2S2O3 yang digunakan dari garam pentahidrat (Na2S2O3.5H2O)
       
Larutan stabil pada pH 9 dan 10 untuk meminimalkan bakteri yang dapat menguraikan S2O3^2- menjadi SO3^2- , SO4^2-, dan S↓
        
Titik akhir : iod yang terikat dengan amilum itu pun hilang bereaksi dengan titran (S2O3^2-) sehingga warna biru hilang

**Kesalahan titrasi**
1.	Kesalahan Oksigen

   O2 diudara dapat menyebabkan hasil titrasi terlalu tinggi karena dapat mengoksidasi
   
   reaksi:

              4I^- + O2 + 4H^+ → 2I2 + 2H2O

   Reaksi ini dikatalisis oleh cahaya dan panas

2.	Penambahan Amilum terlalu awal

   I2 menguap karena terlalu lama menunggu titrasi pH tinggi, S2O3^2- teroksidasi secara parsial menjadi SO4^2-
   
   reaksi:
   
             4I2 + S2O3^2- + 5H2O → 8I^- + 2SO4^2- + 10H^+
    
**Bobot Ekivalen**

Dalam titrasi iodometri, BE suatu zat dihitung dari banyaknya jumlah atom I, bukan jumlah ion I-

              BE= BM/n atom I
          """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1Na45lGPHtPrXJv_eBD_YdtgKTLBOG9SG/view?usp=sharing)")

        
    if optiontitri == "Permanganometri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Permanganometri</h2>", unsafe_allow_html=True)
       st.write(
           """
          **Pengertian titrasi redoks**
          
Titrasi yang melibatkan reaksi reduksi dan oksidasi antara titran dan titrat hingga tepat ekuivalen

**Jenis Titrasi Redoks**
1.	Oksidator kuat sebagai Titran

    KMnO4 (Permanganometri)
   
    K2Cr2O7
   
    Ce (IV)

2.	Reduktor kuat sebagai Titran
    Ti (III)
   
    Fe (II)
   
    Na2S2O3
   
3.	Na2S2O3 sebagai Titran

    Iodometri (Tak langsung)
   
4.	I2 sebagai Titran

    Iodometri (langsung)

**Oksidator kuat sebagai Titran**
1. KMnO4 (Permanganometri)
   
   Kalium permanganat adalah oksidator kuat yang dapat bereaksi dengan cara yang berbeda tergantung kondisi pH
   
   a. Dalam larutan asam [H+] 0,1 N
   
         MnO4- + 8H+ + 5e ⇋  Mn2+ + 4H2O
   
   b. Larutan netral/sedikit basa pH 4-10
   
         MnO4- + 4H+ + 3e ⇋  MnO2 + 2H2O
          
         MnO4- + 2H2O + 3e ⇋ MnO2 + 4OH-
      
   c. Larutan sangat basa [OH-] 0,1 N 
   
         MnO4- + e ⇋ MnO4

2. Titrasi langsung                         

   Fe2+

   Sn2+

   Fe(CN)6 4-

   HNO2
   
   reaksi:
   
           5Fe2+ + MnO4- + 8H+ ⇋ 5Fe3+ + Mn2+ + 4H2O

3. Titrasi tidak langsung

   Ba2+

   Ca2+

   Pb2+

   Zn2+

   Hg2+

   Standardisasi Titrasi tidak langsung:
   1.	Sampel diendapkan sebagai oksalat
   2.	Disaring, dicuci 
   3.	Dilarutkan dalam H2SO4 berlebih sehingga terbentuk asam oksalat
   4.	Dititrasi asam oksalat dengan KMNO4
   
   Reaksi:

           Ca2+ + C2O42- ⇋ CaC2O4 ↓

           CaC2O4↓ + 2H+ ⇋ Ca2+ + H2C2O4

           5H2C2O4 + 2MnO4- + 6H+ ⇋ 10CO2 + 2Mn2+ + 8H2O

      KMnO4 bertindak sebagai auto indikator

      Warna titik akhir titrasi berasal dari KMnO4

 **Pembuatan dan Penyimpanan KMnO4**
""")
       imageT1 = Image.open('Resource/image/Titri/KMnO4.png')
       st.image(imageT1)       
       st.write(
           """
    **Kesalahan titrasi**
1.	Kesalahan Positif

   Penambahan KMnO4 terlalu cepat,menyebabkan terjadinya reaksi MnO4- dengan Mn2+ 

2.	Kesalahan Negatif 

   Penambahan KMnO4 terlalu lama, menyebabkan hilangnya oksalat karena membentuk peroksida yang terurai menjadi air

   reaksi:
   
           H2C2O4 + O2 ⇋ H2O2 + 2CO2↑
           
           H2O2 ⇋ H2O + O2 ↑

**K2Cr2O7 (Kalium Dikromat)**

Kalium dikromat adalah oksidator yang lebih lemah daripada KMnO4 dan Ce(IV), namun sangat stabil dan inert terhadap Cl- 

Dalam suasana asam, K2Cr2O7 mengalami reduksi menjadi:

            Cr3+Cr2O7 2- + 14H+ + 6e ⇋ 2Cr3+ + 7H2O
 
Memerlukan indikator redoks, yaitu zat yang dapat dioksidasi/ reduksi dan berubah warna akibat reaksi tersebut

Penentuan Fe2+ digunakan indikator asam difenilamin sulfonate

**Ce(IV) (Serium Tetravalen)**

1. Serium tetravalen yang digunakan dalam bentuk garam

   • Ce(NO3)4.2NH4NO3

   • Ce(SO4)2.2(NH4)2SO4.2H2O

   • Ce(HSO4)4  

2. Ce4+ mengalami reduksi menjadi Ce3+ Ce4+ + e ⇋ Ce3+

   Kelebihan

   • Larutan stabil dalam H2SO4

   • Hasil reaksi tunggal

   • Tidak mengoksidasi Cl-

   Kekurangan

   • Larutan stabil dalam H2SO4

   • Hasil reaksi tunggal

   • Tidak mengoksidasi Cl-

   • Hanya larut dalam asam

   • Membentuk endapan dalam basa

   • Harga tinggi

   • Memerlukan indicator redoks : Fe(II)- ortofenantrolin (ferroin)

**Reduktor kuat sebagai Titran**

Ti (III), Fe(II), Na2S2O3

1. Ti (III) mudah teroksidasi oleh udara, sehingga perlu penanganan khusus

   Proses titrasi dilakukan dalam atmosfer inert (mengalirkan N2atau CO2)

2. Fe (II) mudah teroksidasi oleh udara dalam larutan netral, sehingga larutan harus dalam suasana asam 

3. Na2S2O3 iodometri (titrasi tidak langsung)
           """)
       st.write("---")
       st.caption("Download Materi")
       st.write("Google Drive: [link](https://drive.google.com/file/d/1dXmGHm_zCBy7CtaNNObd2rK2vm4wOjYx/view?usp=sharing)")
      
        
    if optiontitri == "Asidimetri-Alkalimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Asidimetri-Alkalimetri</h2>", unsafe_allow_html=True)
       st.write(
           """
**Asidimetri-alkalimetri**
       
Asidimetri adalah Bila ditentukan berapa mL larutan asam yang konsentrasinya diketahui untuk menetralkan suatu larutan basa yang kadarnya dicari.

Alkalimetri adalah bila penitar dengan memakai basa yang konsentrasinya diketahui untuk menetapkan suatu asam
           """)
       imageT1 = Image.open('Resource/image/Titri/p1.png')
       st.image(imageT1)
       st.write(
           """   
       **Pemilihan Indikator**
           
• Indikator asam – basa adalah zat yang dapat berubah warna apabila pH lingkungannya berubah

• Warna dalam keadaan asam dinamakan warna asam

• Warna yang ditunjukkan dalam keadaan basa dinamakan warna basa
""")
       st.write("**Jenis indikator asam-basa**")
       imageT2 = Image.open('Resource/image/Titri/p2.png')
       st.image(imageT2)
       st.write(
          """
       **Indikator asam-basa berubah warna bila pH lingkungannya berubah**
            
• Indikator asam-basa ialah asam organik lemah, jadi dalam larutan mengalami kesetimbangan pengionan.

• Molekul-molekul indikator tersebut mempunyai warna yang berbeda dengan ion-ionnya

• Letak trayek pH pada pH tinggi, atau rendah atau ditengah, tergantung dari nilai ka, kb indicator

  reaksi: 
  
                  HIn     ⇌     H+ + In-
               
**Suatu indicator pH digunakan untuk menunjukkan titik akhir**
1.	Indicator harus berubah warna tepat pada saat titran menjadi ekivalen dengan titrat agar tidak terjadi kesalahan titrasi. Untuk mengatasinya trayek indicator harus mencakup pH larutan pada titik ekivalen
2.	Perubahan warna itu harus terjadi dengan mendadak(jelas). Untuk mengatasinya trayekindicator harus memotong bagian yang curam dari kurva

**Titik ekuivalen**

• Titrasi asam kuat oleh basa kuat , pH titik ekuivalen = 7

• Titrasi asam lemah oleh basa kuat, pH titik ekuivalen ± 9

• Titrasi basa kuat oleh asam kuat, pH titik ekuivalen = 7

• Titrasi basa lemah oleh asam kuat, pH titik ekuivalen ± 5

• Makin besar daerah curam kurva ( makin panjang daerah yang curam), makin leluasa pemilihan indicator. Bentuk kurva dan panjang bagian yang curam tergantung pada:           

      • Kesempurnaan reaksi 
  
      • Konsentrasi titran dan titrat
  
**pH larutan**

pH = -log [H+]

pOH = -log [OH-]

pH + pOH = 14
""")
       imageT3 = Image.open('Resource/image/Titri/p3.jpg')
       st.image(imageT3)
       st.write("---")   
       st.caption("Download Materi")
       st.write("Google Drive: [link](https://drive.google.com/file/d/1oWHdhSU_rpCO_-XOCrIEZ84tSreacxH-/view?usp=sharing)")
    
    if optiontitri == "Asidimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Asidimetri</h2>", unsafe_allow_html=True)
       st.write(
          """
       **Bahan baku primer standarisasi asam (HCl)**
              
Boraks atau natrium tetraborat dekahidrat

1.	Na2B4O7.10 H2O ( BM =381,4 BE = BM/2)

     Na2B4O7 + 5H2O   →   2NaH2BO3 + 2H3BO3

     2NaH2BO3 + 2HCl   →  2NaCl + 2H3BO3

     Na2B4O7 + 5H2O + 2HCl   →   2NaCl + 4H3BO3

2.	Natrium karbonat ( Na2CO3) ( BM = 105,96)

     Na2CO3 + HCl   →    NaHCO3 + NaCl
          
     NaHCO3 + HCl   →   NaCl + H2O + CO2

**Standardisasi HCl 0,1 N dengan Bahan Baku Primer Boraks**

Ditimbang teliti  ± 1500 mg boraks dengan kaca arloji, larutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalam Erlenmeyer, tambahkan 2 tetes indikator MM kemudian dititar dengan larutan HCl 0,1 N sampai larutan berubah warna menjadi merah
""")
       imageT1 = Image.open('Resource/image/Titri/As1.png')
       st.image(imageT1)      
       st.write(
           """
       **Penetapan Kadar NaOH dan Na2CO3 dalam Campuran Secara (WARDER)**
           
Na2CO3 dan NaOH dalam sampel campuran dapat ditentukan kadar

masing-masing dengan titrasi asam-basa menggunakan larutan standar

**HCl dengan 2 indikator (pp dan SM).**

Tahap 1: Digunakan indikator pp, HCl akan bereaksi terlebih dahulu dengan natrium hidroksida, dilanjutkan dengan reaksi ion karbonat menjadi hidrogen karbonat (bikarbonat).

Tahap 2: Ditambahkan indikator SM, HCl bereaksi dengan ion hidrogen karbonat (bikarbonat)

**Prosedur**

Dipipet 25 mL contoh ke dalam Erlenmeyer ditambahkan dengan sedikit air suling, dibubuhi 2-3 tetes PP, lalu dititar dengan HCl 0,1 N sehingga tercapai titik akhir hilangnya warna merah muda. Banyaknya HCl yang dipakai dicatat, misalnya a mL. Larutan dibubuhi 2-3 tetes indikator SM, titar dengan HCl sampai titik akhir dari buret tadi tanpa buret dinolkan lagi. Panaskan hingga hampir mendidih (jika warna larutan berubah warna maka dititar lagi dengan HCl). Catat mL HCl yang dipakai, misalnya b mL.
Reaksi  
               
1). NaOH + HCl  →  NaCl + H2O      
                
2). Na2CO3 + HCl →  NaHCO3 + NaCl
                
    NaHCO3 + HCl →  NaCl + CO2 + H2O 
    """)
       imageT2 = Image.open('Resource/image/Titri/As2.png')
       st.image(imageT2)       
       imageT3 = Image.open('Resource/image/Titri/As3.png')
       st.image(imageT3)
       imageT4 = Image.open('Resource/image/Titri/As4.png')
       st.image(imageT4)
       st.write("---")
       st.caption("Download Materi")
       st.write("Google Drive: [link](https://drive.google.com/file/d/1pyJ7HgQ854Ar92zpA7U02gs10UypZyFh/view?usp=sharing)")    
    
    
    if optiontitri == "Alkalimetri":
       st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkalimetri</h2>", unsafe_allow_html=True)
       st.write(
         """
       **Larutan standar (larutan baku)**

Larutan standar adalah larutan yang digunakan sebagai titran yang konsentrasinya di ketahui secara pasti
           
**Larutan standar terdiri dari**

Larutan standar primer adalah larutan yang konsentrasinya harus diketahui dengan teliti dengan cara penimbangan zat yang dilarutkan dalam volume tertentu.

**Syarat-syarat larutan standar primer**

1.	Zat harus mudah diperoleh, murni, mudah dikeringkan
2.	Zat tak berubah selama penimbangan, stabil, tidak higroskopis
3.	Mudah diperiksa kemurniannya
4.	Mudah larut
5.	Reaksi dengan larutan standar harus stoikiometri dan cepat

**Larutan standar sekunder**

larutan yang dapat digunakan untuk standarisasi atau menentukan kadar zat lain dan konsentrasinya sudah distandarisasi dengan suatu standar primer.

Standardisasi ialah suatu usaha menentukan konsentrasi yang tepat dari larutan baku yang akan digunakan untuk titrasi.

**Standarisasi NaOH**

Ditimbang teliti  ± 630 mg asam oksalat dengan kaca arloji, larutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalam Erlenmeyer, tambahkan 2 tetes indikator PP kemudian dititar dengan larutan NaOH 0,1 N sampai larutan berubah warna menjadi merah muda
""")
       imageT1 = Image.open('Resource/image/Titri/naoh.png')
       st.image(imageT1)
       st.write(
           """
       **Standarisasi NaOH secara langsung tanpa pelarutan secara kuantitatif**
           
Ditimbang teliti  ± 157,5 mg asam oksalat dan dimasukkan ke dalam Erlenmeyer kemudian ditambahkan air suling kira-kira 25 mL. Ke dalam larutan ditambahkan 2 tetes indikator PP kemudian dititar dengan larutan NaOH 0,1 N sampai larutan berubah warna menjadi merah muda
""")
       imageT2 = Image.open('Resource/image/Titri/naoh1.png')
       st.image(imageT2)       
       st.write(
           """
       
       **Penetapan kadar asam asetat dalam cuka makan**
           
Dipipet 5 mL contoh cuka makan ke dalam labu takar 250 mL kemudian ditepatkan dengan air suling sampai tanda tera. Dipipet 25 mL larutan tersebut ke dalam Erlenmeyer. Tambahkan 2 sampai 3 tetes indikator PP lalu dititar dengan NaOH 0,1 N (yang sudah distandarisasi).

Menghitung kadar analit:
""")
       imageT3 = Image.open('Resource/image/Titri/analit.png')
       st.image(imageT3)
       imageT4 = Image.open('Resource/image/Titri/analit1.png')
       st.image(imageT4)
       st.write("---")
       st.caption("Download Materi")
       st.write("Google Drive: [link](https://drive.google.com/file/d/14SEvQRrbUxfo1-gzSeEAESPDNSpAVAOd/view?usp=sharing)")

   


   
                                    
#Materi Kimia Organik
with tab_4:
    optionKO = st.selectbox(
            "Pilih materi yang kamu mau",
            ("--- Pilih Materi ---", "Pendahuluan", "Alkana dan Sikloalkana", "Alkena dan Alkuna", "Stereokimia", "Senyawa Aromatik", "Alkohol dan Fenol"))
    if optionKO == "Pendahuluan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pendahuluan</h2>", unsafe_allow_html=True)
        st.write(
            """
            Kimia organik adalah cabang ilmu pengetahuan mengenai kimia senyawa yang mengandung unsur karbon. Jika suatu senyawa tidak mengandung unsur karbon, maka dikatakan anorganik. Ada beberapa alasan mengapa karbon menjadi hal utama dalam kimia organik:
1.	Atom karbon dapat membentuk ikatan yang kuat dengan atom karbon lain untuk membentuk cincin dan rantai atom karbon
2.	Atom karbon juga bisa membentuk ikatan yang kuat dengan unsur-unsur seperti hidrogen, nitrogen, oksigen, dan belerang.

Karena dari sifat-sifat pembentuk ikatan ini, karbon dapat menjadi dasar keragaman senyawa yang sangat besar dan diperlukan untuk munculnya organisme hidup.


Kimia organik awalnya dikotakkan hanya mencakup senyawa-senyawa yang berasal dari makhluk hidup, tapi pandangan ini berubah karena banyaknya penelitian yang membuktikan bahwa senyawa-senyawa organik dapat terbentuk dari senyawa anorganik, contohnya adalah Friedrich Wohler yang berhasil membuat urea dari senyawa anorganik pada tahun 1828.

Selain itu, Alexander Oparin pada tahun 1924 juga menyatakan bahwa kehidupan di Bumi mungkin berkembang melalui evolusi bertahap dari molekul-molekul berbasis karbon dari senyawa -senyawa yang dianggap ada di Bumi prebiotik (masa sebelum ada makhluk hidup): metana, hidrogen, air, dan amonia. Ide ini diuji dengan percobaan yang dilakukan di University of Chicago pada tahun 1952 oleh Stanley Miller dan Harold Urey. Dalam publikasi mereka di tahun 1953, mereka menunjukkan ada lima asam amino (konstituen penting protein) terbentuk ketika percikan listrik melewati labu yang berisi campuran keempat senyawa ini. 
            """)
        st.markdown(
            """
            Daftar Pustaka: 
            
            SOLOMONS, T. W. G., C. B. FRYHLE, & S. A. SNYDER. 2008. _Organic Chemistry_. Edisi ke-12. John Wiley & Sons, Inc. Hoboken.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1HkxDojpo7XzYukO5ALVDAE9_5FtR4nGB/view?usp=sharing)")
        
    if optionKO == "Alkana dan Sikloalkana":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkana</h2>", unsafe_allow_html=True)
        st.write(
            """
            Sebelum memasuki materi alkana, kita perlu mengetahui apa aitu hidrokarbon. Hidrokarbon adalah senyawa yang hanya mengandung atom karbon dan hidrogen. Alkana adalah hidrokarbon yang tidak memiliki ikatan rangkap pada atom karbonnya. Alkana tergolong hidrokarbon jenuh/tersaturasi dan merupakan hidrokarbon paling sederhana.
            Rumus umum: CnH2n+2

Aturan-aturan pemberian nama alkana bercabang menurut sistem IUPAC:
1.	Rantai atom karbon yang terpanjang dianggap sebagai nama senyawa induknya (rantai utama).
2.	Gugus-gugus yang terikat pada rantai utama disebut substituen dan setiap subtituen memiliki satu nama dan satu nomor (menunjukkan  nomor atom C yang mengikat substituen).
3.	Jika terdapat substituen, penomoran rantai utama dimulai dari ujung yang memberikan nomor cabang yang lebih rendah.
4.	Jika terdapat lebih dari satu subtituen yang sama, maka nomor masing-masing substituen harus dituliskan. Jumlah substituent ditunjukkan dengan awalan di-, tri-, tetra-, dan seterusnya.
5.	Penulisan cabang diurutkan berdasarkan abjad
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Penamaan_alkana.png')
        st.image(imageKO1)
        st.write(
            """
            Dalam hidrokarbon, berdasarkan jumlah atom C yang terikat pada suatu atom C dibedakan menjadi 4:
1.	Atom C primer (1°)
2.	Atom C sekunder (2°)
3.	Atom C tersier (3°)
4.	Atom C kuartener (4°)
            """)
        imageKO2 = Image.open('Resource/image/Kimor/Atom_C.png')
        st.image(imageKO2)
        st.write(
            """
            Sifat Fisika Alkana:
1.	Merupakan senyawa nonpolar dan 
2.	gaya antarmolekulnya (van der Waals) adalah gaya London (gaya dipol sesaat-dipol induksian)
3.	Isomer alkana yang bercabang memiliki titik didih lebih rendah daripada isomer yang memiliki rantai lurus (tak bercabang).

Pembuatan Alkana:
1.	Reaksi aluminium karbida dengan air

        Al4C3 + 12H2O → 3CH4 + 4Al(OH)3

2.	Mereaksikan gas alkena dengan gas hidrogen (Adisi)

        C2H4 + H2 → C2H6
            """)
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Sikloalkana</h2>", unsafe_allow_html=True)
        st.write(
            """
            Sikloalkana adalah tipe alkana yang mempunyai satu atau lebih cincin atom karbon pada struktur kimia molekulnya.
            Rumus umum: CnH2n

Aturan-aturan pemberian nama sikloalkana bercabang menurut sistem IUPAC:
1.	Jika terdapat substituen, maka nama cabang disebutkan terlebih dahulu diikuti dengan nama sikloalkananya
2.	Jika terdapat lebih dari dua substituen, nomor pada cincin dimulai dari substituen yang memiliki urutan abjad pertama, dan arah penomorannya memberikan nomor terendah untuk substituen selanjutnya

            """)
        imageKO3 = Image.open('Resource/image/Kimor/Penamaan_sikloalkana.png')
        st.image(imageKO3)
        st.write("Pembuatan: Hidrogenasi Benzena")
        imageKO4 = Image.open('Resource/image/Kimor/Hidrogenasi_benzena.png')
        st.image(imageKO4, caption = "sumber: ruangguru.com")
        st.write(
            """
            Reaksi penting:
            1.	Oksidasi
            """)
        imageKO5 = Image.open('Resource/image/Kimor/Oksidasi_sikloalkana.png')
        st.image(imageKO5)
        st.write("2.	Halogenasi")
        imageKO6 = Image.open('Resource/image/Kimor/Halogenasi_sikloalkana.png')
        st.image(imageKO6)
        st.markdown(
            """
            Daftar Pustaka: 
            
            SOLOMONS, T. W. G., C. B. FRYHLE, & S. A. SNYDER. 2008. _Organic Chemistry_. Edisi ke-12. John Wiley & Sons, Inc. Hoboken.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1eyxBoTTdDbhp84Ae_aRKHMt57B-5iyc1/view?usp=sharing)")
        
    if optionKO == "Alkena dan Alkuna":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkena</h2>", unsafe_allow_html=True)
        st.write(
            """
Alkena adalah hidrokarbon tak jenuh dengan sebuah ikatan rangkap dua selang atom karbon. Rumus umum: CnH2n

Penamaan Alkena:

Mengikuti tatanama IUPAC, nama alkena diambil dari nama alkana dengan menggantikan imbuhan belakang -ana dengan -ena. sistem penomorannya mengikuti system penomoran alkana dengan catatan penomoran rantai karbon terpanjang dinamakan dari ujung yang terdekat dengan ikatan rangkap, sehingga atom karbon pada ikatan rangkap tersebut mempunyai nomor sekecil mungkin.

Sifat Fisik:

Sifat alkena tidak jauh berbeda dengan alkana. Namun, alkena mempunyai tingkat keasaman yang jauh lebih tinggi dibandingkan alkana dan wujud zatnya tergantung dari massa molekulnya.

Reaksi penting:
1.	Hidrasi

        CH2=CH2 + H2O + H+(katalis) → CH3–CH2OH

2.	Halogenasi

        CH2=CH2 + Cl2 → ClCH2–CH2Cl

Pembuatan:
1.	Dehidrogenasi alkohol
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Dehidrogenasi_alkohol.png')
        st.image(imageKO1)
        st.write("2.	Hidrogenasi alkuna")
        imageKO2 = Image.open('Resource/image/Kimor/Hidrogenasi_alkuna.png')
        st.image(imageKO2)
        st.write(
            """
Notasi Cis-Trans:
            
Jika 2 atom karbon alkena mempunyai 2 gugus yang sejenis, maka notasi cis-trans mampu dipakai. Jika gugus sejenis terletak pada tempat yang sama dari ikatan rangkap, maka dinamakan sebagai (cis-). Jika gugus sejenis terletak berseberangan, maka dinamakan sebagai (trans-).
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Cis_trans.png')
        st.image(imageKO3,caption = "Sumber: roboguru.ruangguru.com")
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkuna</h2>", unsafe_allow_html=True)
        st.write(
            """
            Alkuna adalah molekul hidrokarbon tak jenuh yang memiliki ikatan rangkap tiga. Rumus umum: CnH2n-2
            
-Penamaan Alkuna:
1.	Tatanama IUPAC

    Nama sistematis alkuna menurut sistem IUPAC diperoleh dengan mengganti akhiran –ana pada alkana dengan akhiran –una.

2.	Tatanama umum (trivial)

    Dalam tatanama umum, alkuna diberi nama sebagai asetilena tersubtitusi.
            """)
        imageKO4 = Image.open('Resource/image/Kimor/Penamaan_alkuna.png')
        st.image(imageKO4)
        st.write(
            """
            Sifat Fisika:           
1.	Semua alkuna tidak larut dalam air (larut dalam pelarut nonpolar)
2.	Titik didih semakin meningkat dengan bertambahnya berat molekul.
3.	Kenaikan titik didih pada alkuna juga dipengaruhi percabangantom C

Reaksi penting:
1.	Adisi Hidrogen (Hidrogenasi)
            """)
        imageKO5 = Image.open('Resource/image/Kimor/Hidrogen_alkuna.png')
        st.image(imageKO5)
        st.write("2.	Adisi Hidrogen (Hidrogenasi) parsial")
        st.image(imageKO2)
        st.write("3.	Oksidasi dengan KMnO4")
        imageKO6 = Image.open('Resource/image/Kimor/Kmno4_alkuna.png')
        st.image(imageKO6)
        st.write("Pembuatan: Dehidrohalogenasi Alkil Dihalida")
        imageKO7 = Image.open('Resource/image/Kimor/Pembuatan_alkuna.png')
        st.image(imageKO7)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1eAMRVME-3UA3idZkBo7D82KzdFy1mBwz/view?usp=sharing)")


    if optionKO == "Stereokimia":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Streokimia</h2>", unsafe_allow_html=True)
        st.write(
            """
            Studi mengenai molekul-molekul dalam ruang tiga dimensi, yaitu bagaimana atom-atom dalam sebuah molekul ditata dalam ruangan satu relatif terhadap yang lain.
            
Stereoisomer: senyawa berlainan yang mempunyai struktur sama, berbeda hanya dalam hal
penataan atom-atom dalam ruangan

a. Isomer Struktural

Isomer struktur adalah senyawa karbon yang mempunyai rumus molekul sama, tetapi susunan ikatannya berbeda.
1.	Isomer Kerangka (Isomer Rantai)

    Isomer kerangka (isomer rantai) terjadi pada senyawa yang memiliki rumus molekul dan gugus fungsi sama, tetapi struktur kerangka atom karbonnya berbeda.

2.	Isomer Posisi

    Isomer posisi terjadi pada senyawa yang memiliki rumus molekul sama, gugus fungsi sama, tetapi posisi gugus fungsi atau ikatan rangkapnya berbeda.

3.	Isomer Fungsional (Isomer Gugus Fungsi)

    Isomer fungsional atau dikenal juga sebagai isomer gugus fungsi terjadi pada senyawa yang mempunyai rumus molekul yang sama, tetapi gugus fungsinya berbeda.

b. Stereoisomer
1.	Isomer geometrik atau isomer cis-trans : stereoisomer yang berbeda karena gugus-gugus berada pada satu sisi atau pada sisi-sisi yang berlawanan terhadap letak ketegaran molekul
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Cis_trans.png')
        st.image(imageKO1,caption = "Sumber: roboguru.ruangguru.com")
        st.write(
            """
            Kiralitas
1.	Objek yang tidak bisa diimpitkan pada bayangan cerminnya dikatakan kiral, sebaliknya obyek yang dapat diimpitkan pada bayangan cerminnya disebut akiral. 
2.	Sebuah molekul kiral yang tidak dapat diimpitkan pada bayangannya cerminnya, merupakan dua senyawa berlainan yang disebut enantiomer.
3.	Atom karbon kiral/ asimetrik : atom karbon yang mengikat empat gugus yang berlainan.
            """)
        imageKO2 = Image.open('Resource/image/Kimor/Kiral1.jpg')
        st.image(imageKO2,caption = "Sumber: http://sheirafirdarumanda.blogspot.com/")
        st.write(
            """
            Penetapan Konfigurasi : Sistem (R) dan (S)
            
Sepasang enantiomer mempunyai konfigurasi yang berlawanan. R = rectus = kanan, S = sinister = kiri. Cara menentukan konfigurasi R atau S:
1.	Urutkan ke empat gugus atau atom yang terikat pada atom C kiral, sesuai urutan prioritas aturan deret Chan-Ingold-Prelog
2.	Proyeksikan molekul hingga gugus yang berprioritas rendah berarah ke belakang
3.	Pilih gugus dengan prioritas tertinggi dan buat panah ke gugus dengan prioritas tertinggi berikutnya
4.	Jika panah searah jarum jam, maka konfigurasinya adalah R, sedangkan jika berlawanan arah konfigurasinya adalah S.
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Kiral2.jpg')
        st.image(imageKO3,caption = "Sumber: http://sheirafirdarumanda.blogspot.com/")
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1DHyKfG6cJtlf0dWUCjw7rdpX8TVVWEXr/view?usp=sharing)")
        
    if optionKO == "Senyawa Aromatik":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Senyawa Aromatik</h2>", unsafe_allow_html=True)
        st.write(
            """
            Senyawa aromatik merupakan senyawa hidrokarbon yang memiliki ikatan tunggal dan ikatan rangkap di antara atom-atom karbonnya. Dengan syarat:            
1.	Memiliki rantai tertutup (siklik). 
2.	Memiliki bentuk planar atau datar.
3.	Memiliki ikatan rangkap terkonjugasi (berselang-seling) dengan ikatan tunggal.
4.	Memiliki jumlah elektron phi sesuai rumus 4n+2, dimana n merupakan bilangan bulat positif (0, 1, 2, 3, dst.)

Sifat Fisika:
1.	Berwujud cair dengan titik didih 80oC
2.	Tidak berwarna, tak larut dalam air, larut dalam kebanyakan pelarut organik
3.	Mudah terbakar dengan nyala bergelaga dan berwarna (karena kadar karbonya  tinggi).

Tata nama:
1.	Benzena Monosubstitusi

Sistem IUPAC tetap memakai nama umum untuk beberapa benzena monosubstitusi, misalnya toluena, kumena, stirena. Cincin benzena diberi nama sebagai substituent yang terikat pada rantai utama
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Benzena.png')
        st.image(imageKO1)
        st.write(
            """
            2.	Benzena Disubstitusi

Jika ada 2 gugus substituen, penamaan diberikan dengan nomor atau awalan orto (o), meta (m) atau para (p).
            """)
        imageKO2 = Image.open('Resource/image/Kimor/Benzena_disubstitusi.png')
        st.image(imageKO2, caption = "Sumber: roboguru.ruangguru.com")
        st.write(
            """
            3.	Benzena Polisubstitusi
                1.	Jika ada lebih dari 2 substituen penamaan ditunjukkan dengan nomor, sehingga penomoran diberikan sekecil mungkin.
                2.	Jika ada lebih dari 2 substituent yang berbeda, penomoran diurutkan sesuai abjad.
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Benzena_polisubstitusi.png')
        st.image(imageKO3, caption = "Sumber: fathchemical.blogspot.com")
        st.write(
            """
            Reaksi penting:
1.	Hidrogenasi
            """)
        imageKO4 = Image.open('Resource/image/Kimor/Hidrogenasi_benzena.png')
        st.image(imageKO4)
        st.write("2.	Sulfonasi")
        imageKO5 = Image.open('Resource/image/Kimor/Sulfonasi_benzena.png')
        st.image(imageKO5)
        st.markdown(
            """
            Pembuatan:
            
Distilasi tar batu bara (_coal-tar_): distilasi fraksi _light oil_ yang mengandung benzena dan toluena 
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1ZdXOtY3lRtCsXLTEcNpiVvuiyGmea_Ct/view?usp=sharing)")
        
    if optionKO == "Alkohol dan Fenol":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Alkohol</h2>", unsafe_allow_html=True)
        st.write(
            """
            Alkohol (atau alkanol) adalah istilah umum untuk senyawa organik yang memiliki gugus hidroksil (-OH) terikat pada atom karbon.
            
Sifat Fisika:
1.	Alkohol merupakan cairan tidak berwarna (jernih) dan berbau khas.
2.	Hanya alkohol dengan struktur yang kecil/berat molekul ringan larut dalam air.
3.	Tidak larut dalam n-heksana. 
4.	Keasaman alkohol lebih rendah dibandingkan fenol
5.	Titik cair dan titik didihnya meningkat sesuai dengan bertambahnya Mr alkanol

-Tata nama IUPAC
1.	Nama alkohol diambil dari nama alkana dengan akhiran ˗a diganti dengan ˗ol. Alkohol dengan dua, tiga, dan empat gugus ˗OH di antara alkana dan ˗ol diberi sisipan di, tri, tetra sehingga namanya menjadi diol, triol, dan tetrol.
2.	Jika rantai pokok mengikat gugus alkil, penamaan dimulai dari ujung rantai yang mengandung gugus fungsi ˗OH yang paling dekat dengan gugus substitusinya

-Tata nama Trivial
1.	Pemberian namanya diawali dengan nama alkil diikuti kata alcohol
2.	Senyawa dengan lebih dari satu gugus ˗OH disebut glikol.

Reaksi penting:
1.	Dehidrogenasi alkohol
            """)
        imageKO1 = Image.open('Resource/image/Kimor/Dehidrogenasi_alkohol.png')
        st.image(imageKO1)
        
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Fenol</h2>", unsafe_allow_html=True)
        st.write(
            """
            Fenol adalah suatu rangkaian senyawa yang mengandung gugus hidroksil terikat langsung pada cincin aromatik.
            
Sifat Fisika:
1.	Kelarutan fenol dalam air akan berkurang jika gugus nonpolar terikat pada cincin aromatik.
2.	Tidak larut dalam n-heksana.
3.	Fenol bereaksi dengan FeCl3 dan memberikan warna merah-ungu.
4.	Keasaman fenol lebih tinggi dari alkohol.

Penamaan Fenol
1.	Apabila gugus OH merupakan substituen yang memiliki prioritas paling tinggi yang terikat pada benzena maka nama pokok senyawa tersebut adalah fenol dan gugus OH diberi nomor-1 
2.	Jika ada gugus yag prioritasnya lebih tinggi dari OH, misalnya –COOH, CHO, -CO- maka gugus OH berstatus sebagai gugus cabang dan diberi nama “hidroksil”
                 """)
        imageKO2 = Image.open('Resource/image/Kimor/Fenol1.png')
        st.image(imageKO2)
        st.write(
            """
            Pembuatan
1.	Reaksi Hidrolisis Klorobenzena
            """)
        imageKO3 = Image.open('Resource/image/Kimor/Fenol2.jpeg')
        st.image(imageKO3)
        st.write("2.	Reaksi Asam Benzena Sulfonat dengan NaOH")
        imageKO4 = Image.open('Resource/image/Kimor/Fenol3.png')
        st.image(imageKO4)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1mK9VBN1iuqjvNX6haqzDzf1z1wcbC5kg/view?usp=sharing)")
        
        
        
#Materi Fisika Dasar
with tab_5:
    optionfisdas = st.selectbox(
                "Pilih materi yang kamu mau",
                ("--- Pilih Materi ---", "Pendahuluan", "Kinematika", "Usaha dan Energi", "Arus Listrik", "Kalor dan Termodinamika"))
    if optionfisdas == "Pendahuluan":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Pendahuluan</h2>", unsafe_allow_html=True)
        st.write(
           """
           Fisika adalah sains atau ilmu alam yang mempelajari materi beserta gerak dan perilakunya dalam lingkup ruang dan waktu, bersamaan dengan konsep yang berkaitan
seperti energi dan gaya. Sebagai salah satu ilmu sains paling dasar, tujuan utama fisika adalah memahami bagaimana alam semesta berkerja. Ilmu fisika memiliki peran yang sangat penting dalam kimia analitik karena banyak
teknik dan metode analitik didasarkan pada prinsip-prinsip fisika. Beberapa contoh peran ilmu fisika dalam kimia analitik adalah:

1.	Spektroskopi: Teknik spektroskopi memanfaatkan prinsip-prinsip fisika seperti spektroskopi atom, spektroskopi molekul, dan spektroskopi sinar-X. Teknik ini digunakan untuk mengidentifikasi dan memisahkan zat kimia berdasarkan karakteristik spektrum yang dihasilkan oleh zat tersebut.

2.	Kromatografi: Teknik kromatografi memanfaatkan prinsip fisika seperti diferensial affinitas, partisi, dan adsorpsi untuk memisahkan campuran zat kimia menjadi
komponen-komponen yang lebih murni. Teknik ini termasuk kromatografi gas, kromatografi cair, dan kromatografi kolom.

3.	Elektrokimia: Elektrokimia memanfaatkan prinsip fisika elektrokimia untuk menganalisis dan memisahkan zat kimia dalam larutan. Teknik ini melibatkan elektrolisis, elektrogravimetri, potensiometri, dan voltametri.

4.	Termal: Teknik termal memanfaatkan prinsip fisika termal untuk menganalisis dan memisahkan zat kimia berdasarkan karakteristik termal mereka. Contohnya, teknik
difraksi sinar-X dapat digunakan untuk menganalisis struktur kristal dari zat kimia, dan teknik analisis termal dapat digunakan untuk menentukan perubahan termal yang terjadi dalam suatu sampel.

5.	Mikroskopi: Teknik mikroskopi memanfaatkan prinsip-prinsip fisika seperti pembiasan cahaya, interferensi, difraksi, dan polarisasi untuk mengamati dan menganalisis struktur zat kimia pada skala mikroskopik. Contohnya, mikroskop elektron dapat digunakan untuk mempelajari struktur atom dan molekul, sementara
mikroskop fluoresensi dapat digunakan untuk melihat reaksi kimia dalam sel hidup
Dengan demikian, ilmu fisika sangat penting dalam kimia analitik karena memberikan dasar teoritis dan teknis bagi banyak teknik dan metode analitik.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/17XoRu0y5Y6ZHuz2M8eB7ZVdY-pgw0dCu/view?usp=sharing)")
    
    if optionfisdas == "Kinematika":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kinematika</h2>", unsafe_allow_html=True)
        st.write(
            """
    Kinematika merupakan cabang Ilmu fisika yang membahas mengenai bagaimana benda bergerak. Kinematika membahas gerak benda tanpa mempelajari penyebab gerak tersebut. Kinematika merupakan dasar bagi banyak cabang fisika lainnya, seperti fluida, kalor, gelombang, cahaya, dsb.
Dalam Analisis Kimia, Kinematika dapat diaplikasikan secara tidak langsung melalui cabang Fisika lainnya. Misalnya, gerak gelombang cahaya merupakan dasar dari spektrofotometri.
Gerak adalah perubahan kedudukan atau tempat suatu benda terhadap titik acuan tertentu.

Besaran‐besaran yang terkait dengan kinematika :

- Perpindahan

Perpindahan didefinisikan sebagai perubahan posisi benda terhadap titik acuan. Perpindahan merupakan besaran vector, berbeda dengan jarak yang merupakanbesaran skalar.

- Waktu

Waktu dalam kinematika adalah salah satu variabel yang digunakan untuk mengukur pergerakan benda. Dalam kinematika, waktu dianggap sebagai variabel independen yang mengukur durasi dari suatu peristiwa atau gerakan. Waktu dalam kinematika diukur dalam satuan detik (s), dan sering digunakan bersamaan dengan variabel lain seperti posisi, kecepatan, dan percepatan untuk menggambarkan gerakan benda. Dalam persamaan kinematika, waktu biasanya dinyatakan sebagai t.

Beberapa konsep penting yang berkaitan dengan waktu dalam kinematika antara lain:
1.	Waktu awal (t₀): Waktu ketika gerakan dimulai.
2.	Waktu akhir (t): Waktu ketika gerakan berakhir.
3.	Waktu tempuh (Δt): Selisih waktu antara waktu akhir dan waktu awal. Waktu tempuh dapat digunakan untuk menghitung kecepatan rata-rata suatu benda.
4.	Waktu paruh (t₁/₂): Waktu yang diperlukan untuk setengah dari suatu populasi radioaktif terurai.

Dalam analisis kinematika, waktu digunakan untuk mengukur perubahan posisi, kecepatan, dan percepatan suatu benda seiring berjalannya waktu. Sebagai contoh, jika diketahui posisi awal dan posisi akhir suatu benda, serta waktu yang diperlukan untuk benda tersebut bergerak dari posisi awal ke posisi akhir, maka kecepatan rata-rata dan percepatan rata-rata benda tersebut dapat dihitung menggunakan waktu sebagai salah satu variabelnya.

- Kecepatan

Kecepatan dalam kinematika adalah ukuran seberapa cepat suatu benda bergerak dan arah gerakannya. Kecepatan didefinisikan sebagai perubahan jarak yang ditempuh oleh suatu benda dalam satu satuan waktu, atau dapat juga
didefinisikan sebagai turunan dari perpindahan benda terhadap waktu. Kecepatan dapat diukur dalam satuan meter per detik (m/s) atau kilometer per jam (km/jam).
Rumus umum untuk kecepatan (v) adalah:

v = Δs/Δt

di mana Δs adalah perpindahan atau jarak yang ditempuh oleh benda selama interval waktu tertentu Δt. Dalam kasus pergerakan benda dengan kecepatan yang konstan, rumus ini dapat disederhanakan menjadi:

v = s/t

di mana s adalah jarak yang ditempuh oleh benda dalam waktu t.

Selain kecepatan rata-rata, ada juga kecepatan instan atau kecepatan pada suatu saat tertentu. Kecepatan instan didefinisikan sebagai limit dari perubahan jarak terhadap waktu ketika interval waktu mendekati nol. Kecepatan instan adalah kecepatan benda pada suatu titik dalam gerakan, dan dapat dihitung dengan mengambil turunan dari persamaan perpindahan benda terhadap waktu.
Rumus untuk kecepatan instan dapat dinyatakan sebagai berikut:

v = ds/dt

di mana ds adalah perpindahan yang sangat kecil dan dt adalah waktu yang sangat kecil yang dibutuhkan oleh benda untuk melakukan perpindahan tersebut.
- Percepatan

Percepatan dalam kinematika adalah ukuran seberapa cepat kecepatan suatu benda berubah seiring waktu. Secara matematis, percepatan didefinisikan sebagai perubahan kecepatan suatu benda selama interval waktu tertentu. Percepatan dapat berupa percepatan rata-rata atau percepatan instan.
Percepatan rata-rata (a) diukur dalam satuan meter per detik kuadrat (m/s²) dan didefinisikan sebagai perubahan kecepatan (Δv) dibagi dengan interval waktu (Δt):

a = Δv/Δt

Percepatan instan adalah percepatan pada suatu titik dalam gerakan dan didefinisikan sebagai limit dari perubahan kecepatan terhadap waktu ketika interval waktu mendekati nol. Dalam notasi turunan, percepatan instan dinyatakan sebagai turunan dari kecepatan terhadap waktu:

a = dv/dt

Rumus kinematika yang melibatkan percepatan adalah:

v = v₀ + at

di mana v adalah kecepatan akhir benda, v₀ adalah kecepatan awal benda, a adalah percepatan benda, dan t adalah waktu yang diperlukan untuk mencapai kecepatan akhir. Rumus ini digunakan untuk menghitung kecepatan benda pada titik tertentu dalam gerakan jika diketahui percepatan, kecepatan awal, dan waktu yang dibutuhkan untuk mencapai kecepatan tersebut. Dalam kinematika, percepatan sering dihubungkan dengan gaya melalui hukum
Newton kedua, yaitu F = ma, di mana F adalah gaya yang bekerja pada benda, m adalah massa benda, dan a adalah percepatan benda yang dihasilkan oleh gaya tersebut.

Gerak lurus beraturan (GLB) adalah gerakan suatu benda dalam lintasan lurus dengan kecepatan konstan. Dalam GLB, kecepatan benda selalu sama pada setiap titik dalam lintasan. Gerak lurus beraturan dapat terjadi dalam keadaan di mana gaya-gaya yang bekerja pada benda seimbang, sehingga tidak ada percepatan pada benda tersebut.
Contoh GLB yang umum adalah gerakan roda mobil di jalan raya dengan kecepatan konstan. Pada saat roda mobil bergerak, kecepatan roda tetap sama pada setiap titik pada lintasan jalan raya, karena gaya-gaya yang bekerja pada roda mobil, seperti gaya gesekan dan gaya gravitasi, seimbang.

Rumus: v = s/t

Gerak lurus berubah beraturan (GLBB) adalah gerakan suatu benda dalam lintasan lurus dengan percepatan konstan. Dalam GLBB, kecepatan benda bertambah atau berkurang dengan laju yang sama pada setiap titik dalam lintasan. Dalam GLBB, percepatan benda diukur dalam satuan meter per detik kuadrat (m/s²) dan dinyatakan sebagai perubahan kecepatan (Δv) dibagi dengan interval waktu (Δt):

a = Δv/Δt

Kecepatan benda pada titik tertentu dalam GLBB dapat dihitung menggunakan rumus kinematika:

v = v₀ + at

di mana v adalah kecepatan benda pada titik tertentu, v₀ adalah kecepatan awal benda, a adalah percepatan benda, dan t adalah waktu yang diperlukan untuk mencapai kecepatan tersebut.

Selain itu, persamaan gerak yang digunakan dalam GLBB adalah:

s = v₀t + (1/2)at²

di mana s adalah jarak yang ditempuh oleh benda, v₀ adalah kecepatan awal benda, a adalah percepatan benda, dan t adalah waktu yang diperlukan untuk menempuh jarak tersebut.
Contoh GLBB yang umum adalah gerakan benda yang dilempar ke atas dan kemudian jatuh kembali ke bumi. Pada awal gerakan, kecepatan benda adalah nol. Namun, setelah dilempar, benda mengalami percepatan gravitasi yang konstan sehingga kecepatannya
bertambah secara bertahap. Pada titik tertinggi, kecepatan benda kembali menjadi nol, kemudian benda jatuh kembali ke bumi dengan percepatan gravitasi yang sama.
            """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/11tbMk4wxWioI_p1aF2ij5TtV32Mph1tp/view?usp=sharing)")  
        
    if optionfisdas == "Usaha dan Energi":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Usaha dan Energi</h2>", unsafe_allow_html=True)
        st.write(
           """
           Usaha dan energi adalah konsep penting dalam fisika yang berkaitan dengan perubahan keadaan benda dan perpindahan energi dalam sistem fisika.

**Usaha**

Usaha didefinisikan sebagai jumlah energi yang diperlukan untuk memindahkan benda dari satu titik ke titik lain dengan gaya konstan. Secara matematis, usaha dapat dihitung dengan
rumus:

W = F × d × cos(θ)

di mana:

W = usaha (dalam satuan Joule)

F = gaya yang bekerja pada benda (dalam satuan Newton)

d = jarak perpindahan benda (dalam satuan meter)

θ = sudut antara arah gaya dan arah perpindahan benda (dalam satuan derajat)

**Energi Potensial**

Energi potensial adalah energi yang dimiliki oleh benda sebagai akibat dari posisi atau ketinggiannya dalam suatu medan gravitasi atau medan gaya lainnya. Energi potensial dapat
dihitung dengan rumus:

Ep = m × g × h

di mana:

Ep = energi potensial (dalam satuan Joule)

m = massa benda (dalam satuan kilogram)

g = percepatan gravitasi bumi (sekitar 9,8 m/s^2)

h = ketinggian benda dalam medan gravitasi (dalam satuan meter)

**Energi Kinetik**

Energi kinetik adalah energi yang dimiliki oleh benda sebagai akibat dari gerakannya. Energi kinetik dapat dihitung dengan rumus:

Ek = 1/2 × m × v^2

di mana:

Ek = energi kinetik (dalam satuan Joule)

m = massa benda (dalam satuan kilogram)

v = kecepatan benda (dalam satuan meter per detik)

**Prinsip Konservasi Energi Mekanik**

Prinsip konservasi energi mekanik menyatakan bahwa total energi mekanik dalam suatu sistem terjaga atau konstan, walaupun terdapat perubahan bentuk energi dari potensial ke kinetik dan
sebaliknya. Dengan menggunakan prinsip ini, dapat dihitung energi mekanik awal (Em1) dan akhir (Em2) suatu benda dalam suatu sistem yang mengalami perubahan energi. Persamaan
prinsip konservasi energi mekanik adalah sebagai berikut:

Em1 = Em2

Ep1 + Ek1 = Ep2 + Ek2

di mana:

Em1 = energi mekanik awal (dalam satuan Joule)

Em2 = energi mekanik akhir (dalam satuan Joule)

Ep1 = energi potensial awal (dalam satuan Joule)

Ep2 = energi potensial akhir (dalam satuan Joule)

Ek1 = energi kinetik awal (dalam satuan Joule)

Ek2 = energi kinetik akhir (dalam satuan Joule)
           """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/19TwtmnRsHhn8bifjGkxOjqw5Zh7z784z/view?usp=sharing)") 
        
    if optionfisdas == "Arus Listrik":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Arus Listrik</h2>", unsafe_allow_html=True)
        st.write(
           """
1.	Arus Listrik

    Arus listrik adalah gerakan muatan listrik melalui suatu penghantar. Arus listrik dapat dihasilkan oleh baterai, generator listrik, atau sumber energi listrik lainnya. Arus listrik diukur
dalam satuan ampere (A). Ada dua jenis arus listrik, yaitu arus searah (DC) dan arus bolak-balik (AC).
Arus searah (DC) adalah arus listrik yang mengalir dalam satu arah atau polaritas tertentu. Arus searah biasanya dihasilkan oleh baterai dan digunakan dalam aplikasi seperti
lampu kilat, sirkuit elektronik, dan kendaraan listrik.
Arus bolak-balik (AC) adalah arus listrik yang mengalir bolak-balik antara dua arah atau polaritas. Arus bolak-balik dihasilkan oleh generator listrik dan digunakan dalam sistem
listrik rumah tangga dan industri.

2.	Tegangan Listrik

    Tegangan listrik (atau beda potensial listrik) adalah perbedaan potensial listrik antara dua
titik dalam rangkaian listrik yang dapat mendorong arus listrik mengalir. Satuan tegangan
listrik adalah volt (V) dan dapat diukur menggunakan alat yang disebut voltmeter.

3. Hambatan Listrik

    Hambatan listrik adalah besarnya penghalang yang dihadapi oleh arus listrik dalam mengalir melalui penghantar. Hambatan listrik diukur dalam satuan ohm (Ω) dan dapat dihitung menggunakan hukum Ohm.

4.	Hukum Ohm

    Hukum Ohm menyatakan bahwa beda potensial listrik pada suatu penghantar sebanding dengan arus listrik yang mengalir melaluinya dan invers sebanding dengan hambatan penghantar. Persamaannya adalah:

    V = I * R

    dengan:

    V = beda potensial listrik (dalam satuan volt)

    I = arus listrik (dalam satuan ampere)

    R = hambatan listrik (dalam satuan ohm)

5.	Hukum Kirchoff

    Hukum Kirchoff terdiri dari dua hukum, yaitu:
    
    - Hukum Kirchoff Pertama (KPL) menyatakan bahwa jumlah arus listrik yang masuk ke sebuah simpul sama dengan jumlah arus listrik yang keluar dari simpul tersebut. Persamaannya adalah: ΣI_masuk = ΣI_keluar

    - Hukum Kirchoff Kedua (KPL) menyatakan bahwa jumlah beda potensial listrik dalam suatu loop tertutup sama dengan nol. Persamaannya adalah: ΣV_loop = 0

6.	Daya Listrik

    Daya listrik adalah besarnya energi yang dikonsumsi atau dihasilkan oleh suatu rangkaian listrik dalam satu satuan waktu. Daya listrik diukur dalam satuan watt (W) dan dapat dihitung
menggunakan persamaan:

    P = V * I

    dengan:

    P = daya listrik (dalam satuan watt)

    V = beda potensial listrik (dalam satuan volt)

    I = arus listrik (dalam satuan ampere)
       """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1r3e1OAf1KwQy-4gt__HA8BmamnZ4DUZQ/view?usp=sharing)")
               
if optionfisdas == "Kalor dan Termodinamika":
        st.markdown("<h2 style='text-align: center; color: raisin black;'>Kalor dan Termodinamika</h2>", unsafe_allow_html=True)
        st.write(
           """
           Kalor dan termodinamika adalah konsep-konsep fisika yang berkaitan dengan transfer energi dalam bentuk panas dan hubungan antara energi, suhu, dan kerja.
Kalor adalah energi yang berpindah dari suatu sistem ke sistem lain akibat adanya perbedaan suhu. Sistem yang menerima kalor akan mengalami kenaikan suhu dan sebaliknya,
sistem yang melepaskan kalor akan mengalami penurunan suhu. Termodinamika adalah studi tentang energi dan perubahan energi dalam suatu sistem.

Termodinamika mencakup dua hukum termodinamika yang mendasar, yaitu:
1.	Hukum Pertama Termodinamika: energi tidak dapat diciptakan atau dihancurkan, tetapi dapat berubah bentuk dari satu bentuk ke bentuk yang lain.
2.	Hukum Kedua Termodinamika: entropi alam semakin meningkat, yaitu keadaan alam semakin acak dan tidak teratur.


   Dalam termodinamika, suatu sistem dapat berupa sistem terbuka, sistem tertutup, atau sistem terisolasi. Sistem terbuka dapat bertukar energi dan materi dengan lingkungannya,
sistem tertutup dapat bertukar energi tetapi tidak materi dengan lingkungannya, sedangkan sistem terisolasi tidak bertukar energi atau materi dengan lingkungannya.
Beberapa konsep penting dalam termodinamika adalah panas jenis, kapasitas kalor, kerja, entropi, dan efisiensi termodinamika. Panas jenis adalah jumlah kalor yang diperlukan
untuk meningkatkan suhu satu kilogram bahan satu derajat Celsius. Kapasitas kalor adalah jumlah kalor yang diperlukan untuk meningkatkan suhu suatu benda. Kerja adalah energi yang
dibutuhkan untuk melakukan perpindahan, misalnya perpindahan benda atau gas. Entropi adalah ukuran dari ketidakteraturan dan keteraturan dari suatu sistem, sedangkan efisiensi
termodinamika adalah rasio antara energi yang dihasilkan dengan energi yang digunakan. Pada umumnya jika suatu zat diberi kalor, maka zat tersebut akan mengalami pemuaian.
Pemuaian yang terjadi pada zat padat dapat berupa pemuaian panjang, luas, dan volume.

Berikut ini adalah rumus untuk tiga jenis pemuaian yang umum terjadi:

1. Pemuaian linier:

     ΔL = αL₀ΔT
 
     ΔL = perubahan panjang (dalam satuan meter)
 
     α = koefisien muai panjang
 
    L₀ = panjang awal (dalam satuan meter)
 
    ΔT = perubahan suhu (dalam satuan derajat Celsius)
 
2. Pemuaian luas:

    ΔA = βA₀ΔT
 
    ΔA = perubahan luas (dalam satuan meter persegi)
 
    β = koefisien muai luas
    
    A₀ = luas awal (dalam satuan meter persegi)
 
    ΔT = perubahan suhu (dalam satuan derajat Celsius)
 
3. Pemuaian volume:

    ΔV = γV₀ΔT
 
    ΔV = perubahan volume (dalam satuan meter kubik)
 
    γ = koefisien muai volume
 
    V₀ = volume awal (dalam satuan meter kubik)
 
    ΔT = perubahan suhu (dalam satuan derajat Celsius)
 
   Koefisien muai panjang, muai luas, dan muai volume merupakan konstanta yang tergantung pada jenis material dan suhu.

   Jika membicarakan kalor dan termodinamika, maka kita juga berbicara tentang ‘transfer’nya. Metode transfer panas ada tiga yaitu konduksi, konveksi, dan radiasi. Konduksi,
konveksi, dan radiasi adalah tiga mode transfer panas yang berbeda. Ketiganya berperan penting dalam mengatur suhu benda dan lingkungan sekitarnya. Berikut adalah penjelasan
singkat tentang ketiga mode transfer panas tersebut:

1. Konduksi:

    Konduksi adalah mode transfer panas melalui perpindahan energi panas dari molekul ke molekul dalam suatu benda atau antara dua benda yang saling bersentuhan. Panas ditransfer
dari daerah yang lebih panas ke daerah yang lebih dingin, sampai tercapai kesetimbangan termal. Konduksi terjadi karena perbedaan suhu antara dua objek atau antara bagian-bagian
objek yang berbeda. Konduksi terutama terjadi pada benda padat.

2. Konveksi:

    Konveksi adalah mode transfer panas melalui pergerakan massa dari satu tempat ke tempat lain yang mengalirkan energi panas bersama-sama. Konveksi terjadi karena adanya
perbedaan suhu dan densitas dari benda yang mengalir. Udara, air, dan gas lainnya biasanya terlibat dalam proses konveksi. Konveksi dapat terjadi baik pada benda padat maupun fluida.

3. Radiasi:

    Radiasi adalah mode transfer panas melalui pancaran gelombang elektromagnetik yang membawa energi panas dari sumber panas ke benda lainnya. Radiasi terjadi karena semua
benda yang memiliki suhu di atas nol mutlak akan memancarkan energi dalam bentuk gelombang elektromagnetik. Radiasi dapat terjadi dalam hampa udara, sehingga dapat terjadi pada benda padat, cair, atau gas.

   Ketiga mode transfer panas ini sering kali terjadi bersamaan dalam suatu sistem dan saling mempengaruhi. Penting untuk memahami prinsip-prinsip dasar ketiga mode transfer panas ini untuk dapat menerapkan teknik-teknik pengaturan suhu yang efektif pada berbagai aplikasi teknik dan industri.
           """)
        st.write("---")
        st.caption("Download Materi")
        st.write("Google Drive: [link](https://drive.google.com/file/d/1Rkn5h8GRh9y2uD93MNEURd3rTxDxl3EU/view?usp=sharing)")
