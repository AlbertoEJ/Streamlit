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



st.title('Cifrado de un mensaje con AES')
st.text('Código realizado en Python por Elena :D')

texto = st.text_input('Ingresa un texto a cifrar:',)
mensaje=bytes(texto, 'utf-8')

key = st.text_input('Ingresa la llave para cifrar. Esta llave se convertirá automáticamente a bytes.',value="12345678901234567890123456789012")
keybytes=bytes(key, 'utf-8')

cifrado=encrypt(keybytes,mensaje)

desencriptado=decrypt(keybytes,cifrado)

if st.button('Cifrar'):
    st.write('El texto cifrado es: ', cifrado)
else:
    st.write('Presiona cifrar para mostrar el mensaje cifrado')
    
if st.button('Decifrar'):
    st.write('El texto descifrado es: ', desencriptado)
else:
    st.write('Presiona cifrar para mostrar el mensaje descifrado')


    
