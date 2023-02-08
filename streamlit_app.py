import streamlit as st
from Crypto.Cipher import AES

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return cipher.nonce + tag + ciphertext

def decrypt(key, data):
    nonce = data[:AES.block_size]
    tag = data[AES.block_size:AES.block_size * 2]
    ciphertext = data[AES.block_size * 2:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    
    return cipher.decrypt_and_verify(ciphertext, tag)

key=b'12345678901234567890123456789012'

cifrado=encrypt(key,'Holaaaa')

desencriptado=decrypt(key,cifrado)

st.title('Tarea de cifrado de Elena Herandez')
st.text('¡Esto es puro Pythoooon!')

texto = st.text_input('Ingresa un texto a cifrar',)

st.write('El texto cifrado es: ', cifrado)
st.write('El texto descifrado es: ', desencriptado)
