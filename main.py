import streamlit as st


st.title("Ini Webku")
st.header("Programmer kalibaru")


nama = st.text_input("Masukkan Nama anda")

if not nama:
    st.stop()
st.markdown(f'selamat datang {nama}', unsafe_allow_html=True)

