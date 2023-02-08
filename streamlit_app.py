import streamlit as st


title = st.text_input('Movie title', 'Life of Brian')

suma=str(title+1)
st.write('La suma es:', suma)