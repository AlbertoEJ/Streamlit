import streamlit as st
from Crypto.Cipher import AES
from PIL import Image


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



st.title('Cifrado de un mensaje con AES-256 bits')
st.text('Código realizado en Python por Elena :D')

opcion = st.radio(
    "¿Sabes cómo funciona el cifrado AES-256?",
    ('Selecciona una opción','Sí', 'No, enseñame'))

if opcion == 'Sí':
    texto = st.text_input('Ingresa un texto a cifrar:',type="password")
    mensaje=bytes(texto, 'utf-8')

    key = st.text_input('Ingresa la llave para cifrar. Esta llave se convertirá automáticamente a bytes. IMPORTANTE: DEBE SER DE 32 BYTES (32 CARÁCTERES)',)
    keybytes=bytes(key, 'utf-8')

    if len(key)==32:
        cifrado=encrypt(keybytes,mensaje)
        if st.button('Cifrar'):
            st.write('El texto cifrado es: ', cifrado)
        else:
            st.write('Presiona cifrar para mostrar el mensaje cifrado')
        
        if st.button('Decifrar'):
            desencriptado=decrypt(keybytes,cifrado)
            st.write('El texto descifrado es: ', desencriptado)
        else:
            st.write('Presiona cifrar para mostrar el mensaje descifrado')
    else:
        st.text('La llave que ingresaste no es de 32 bytes. Ingresa otra de nuevo.')

if opcion == 'No, enseñame':
    st.markdown('Actualmente, hay tres tipos de cifrado AES: 128 bits, 192 bits y 256 bits, donde este último por su longitud en el número de bits es el más seguro. Esto se diseñó basándose en la Ley de Moore, ya que las primeras pruebas demostraron que, en un tiempo relativamente corto, la potencia de los procesadores podría romper el cifrado más débil y, por tanto, con menor número de bits en periodos de tiempo cada vez más bajo.')
    st.markdown("Para entender el funcionamiento del cifrado AES hemos de entender que la información original sufre una transformación, donde los significantes binarios son modificados de tal manera que sin el decodificador pertinente no se pueden entender. Entiéndase significante como el código binario que codifica lo que son datos e instrucciones que el procesador ha de ejecutar. Así pues, de la misma manera que un conjunto de letras y números ilegibles para nosotros no tiene sentido alguno, para un procesador tampoco.")

    image = Image.open('/AES-Design.jpg')
    st.image(image, caption='Funcionamiento de AES')





    



    
