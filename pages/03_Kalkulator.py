import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Calchemio</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Kalkulator buat kamu yang suka kimia</h2>", unsafe_allow_html=True)
st.caption("Apa yang mau kamu hitung hari ini?")
tab_1, tab_2, tab_3, tab_4, tab_5, tab_6 = st.tabs(["Molalitas","Molaritas", "% Kadar", "Normalitas", "PPM", "PPB"])
with tab_1:
     option = st.selectbox(
        "Pilih salah satu",
        ("Diketahui Mol zat terlarut & massa zat pelarut","Diketahui massa zat terlarut, molekul relatif zat terlarut, & massa pelarut"))
     if option == "Diketahui Mol zat terlarut & massa zat pelarut":
        Mol_zatterlarut = st.number_input("Masukkan mol zat terlarut(mol)")
        massa_zatpelarut = st.number_input("Masukkan massa zat pelarut(kg)")
        tombol_1 = st.button("Hitung molalitas")       
        if tombol_1:
            nilai_molalitas1 = Mol_zatterlarut/massa_zatpelarut
            st.success(f"nilai molalitas adalah {nilai_molalitas1}")
     if option == "Diketahui massa zat terlarut, molekul relatif zat terlarut, & massa pelarut":
        Massa_zatterlarut = st.number_input("Masukkan nilai massa(g)")
        Molekulrelatif = st.number_input("Masukkan nilai Mr")
        massa_zatpelarut1= st.number_input("Masukkan nilai massa pelarut (g)")
        tombol_2 = st.button("Hitung molalitas")
        if tombol_2:
            nilai_molalitas2 = Massa_zatterlarut*1000/(Molekulrelatif*massa_zatpelarut1)
            st.success(f"nilai normalitas adalah {nilai_molalita_2}")
   
with tab_2:
    option = st.selectbox(
        "Pilih salah satu",
        ("Diketahui Mol zat terlarut & Volume","Diketahui massa, Mr, & volume"))
    if option == "Diketahui Mol zat terlarut & Volume":
        Mol = st.number_input("Masukkan nilai mol terlarut")
        Volume = st.number_input("Masukkan jumlah volume larutan (mL)")
        tombol_1 = st.button("Hitung molaritas")
        if tombol_1:
            nilai_molaritas1 = Mol/Volume
            st.success(f"nilai molaritas adalah {nilai_molaritas1}")
    if option == "Diketahui massa, Mr, & volume":
        Massa = st.number_input("Masukkan nilai massa terlarut (gram)")
        Mr = st.number_input("Masukkan nilai Mr terlarut (gram/mol)")
        volume = st.number_input("Masukkan jumlah volume larutan (mL)")
        tombol_2 = st.button("Hitung molaritas")
        if tombol_2:
            nilai_molaritas2 = Massa*1000/(Mr*volume)
            st.success(f"nilai molaritas adalah {nilai_molaritas2}")
        
with tab_3:
    option = st.selectbox(
        "Pilih salah satu",
        ("% Kadar (v/v)","% Kadar (b/v)","% Kadar (b/b)"))
    if option == "% Kadar (v/v)":
        volume_zat1= st.number_input("Masukkan nilai volume zat")
        volume_total1 = st.number_input("Masukkan nilai volume total")
        tombol_1 = st.button("Hitung % Kadar (v/v)")
        if tombol_1:
            nilai_kadar1 =volume_zat1/volume_total1
            st.success(f"nilai % Kadar (v/v) adalah {nilai_kadar1}")
    if option == "% Kadar (b/v)":
        massa_zat1= st.number_input("Masukkan nilai massa zat")
        volume_total2 = st.number_input("Masukkan nilai volume total")
        tombol_2 = st.button("Hitung % Kadar (b/v)")
        if tombol_2: 
            nilai_kadar2 = massa_zat1/volume_total2
            st.success(f"nilai % Kadar (b/v) adalah {nilai_kadar2}")
    if option == "% Kadar (b/b)":
        massa_zat2= st.number_input("Masukkan nilai massa zat")
        massa_total1 = st.number_input("Masukkan nilai massa total")
        tombol_3 = st.button("Hitung % Kadar (b/b)")
        if tombol_3:
            nilai_kadar3 = massa_zat2/massa_total1
            st.success(f"nilai % Kadar (b/b) adalah {nilai_kadar3}")
    
    
with tab_4:
    option = st.selectbox(
        "Pilih salah satu",
        ("Diketahui molaritas & valensi","Diketahui massa, BE, & volume larutan", "Diketahui massa,Mr, & volume larutan"))
    if option == "Diketahui molaritas & valensi":
        Molaritas = st.number_input("Masukkan nilai molaritas")
        Valensi = st.number_input("Masukkan nilai valensi")
        tombol_1 = st.button("Hitung normalitas")
        if tombol_1:
            nilai_normalitas1 = Molaritas*Valensi
            st.success(f"nilai normalitas adalah {nilai_normalitas1}")
    if option == "Diketahui massa, BE, & volume larutan":
        Massa1 = st.number_input("Masukkan nilai massa (gram)")
        BE = st.number_input("Masukkan nilai BE")
        volume1 = st.number_input("Masukkan nilai volume larutan (liter)")
        tombol_2 = st.button("Hitung normalitas")
        if tombol_2:
            nilai_normalitas2 = Massa1/(BE*volume1)
            st.success(f"nilai normalitas adalah {nilai_normalitas2}")
    if option == "Diketahui massa,Mr, & volume larutan":
        Massa2 = st.number_input("Masukkan nilai massa (mg)")
        Mr = st.number_input("Masukkan nilai Mr")
        volume2 = st.number_input("Masukkan nilai volume larutan (mL)")
        tombol_3 = st.button("Hitung normalitas")
        if tombol_3:
            nilai_normalitas3 = Massa2*1000/(Mr*volume2)
            st.success(f"nilai normalitas adalah {nilai_normalitas3}")
            
with tab_5:
    option = st.selectbox(
        "Pilih salah satu",
        ("mg/L","mg/kg"))
    if option == "mg/L":
        Massa1 = st.number_input("Masukkan nilai massa zat terlarut (mg)")
        Volume = st.number_input("Masukkan nilai volume larutan (L)")
        tombol_1 = st.button("Hitung PPM")
        if tombol_1:
            nilai_ppm1 = Massa1/Volume
            st.success(f"nilai PPM adalah {nilai_ppm1}")
    if option == "mg/kg":
        Massa2 = st.number_input("Masukkan nilai massa zat terlarut (mg)")
        Berat = st.number_input("Masukkan nilai berat larutan (kg)")
        tombol_2 = st.button("Hitung PPM")
        if tombol_2:
            nilai_ppm2 = Massa2/Berat
            st.success(f"nilai PPM adalah {nilai_ppm2}")
    
with tab_6:
    option = st.selectbox(
        "Pilih salah satu",
        ("μg/L","μg/kg"))
    if option == "μg/L":
        Massa1 = st.number_input("Masukkan nilai massa zat terlarut (μg)")
        Volume = st.number_input("Masukkan nilai volume larutan (L) ")
        tombol_1 = st.button("Hitung PPB")
        if tombol_1:
            nilai_ppb1 = Massa1/Volume
            st.success(f"nilai PPB adalah {nilai_ppb1}")
    if option == "μg/kg":
        Massa2 = st.number_input("Masukkan nilai massa zat terlarut (μg)")
        Berat = st.number_input("Masukkan nilai berat larutan (kg) ")
        tombol_2 = st.button("Hitung PPB")
        if tombol_2:
            nilai_ppb2 = Massa2/Berat
            st.success(f"nilai PPB adalah {nilai_ppb2}")  
