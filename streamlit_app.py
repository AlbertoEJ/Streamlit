import streamlit as st
import pycrypto

st.title('Tarea de cifrado de Elena Herandez')
st.text('¡Esto es puro Pythoooon!')

texto = st.text_input('Ingresa un texto a cifrar',)

st.write('El texto que cifrarás es: ', texto)