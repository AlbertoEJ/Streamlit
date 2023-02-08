import streamlit as st


title = st.text_input('Movie title', 'Life of Brian',key=int)

suma=title+1
st.write('La suma es:', suma)