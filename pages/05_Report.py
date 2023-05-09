import streamlit as st

st.markdown("<h1 style='text-align: center; color: raisin black;'>Report</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: raisin black;'>Tuliskan keluhanmu agar kami bisa terus berkembang menjadi lebih baik</h2>", unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/tugaslpk.kelompok4@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Resource/style/style.css")
