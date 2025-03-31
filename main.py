import streamlit as st
import requests

#url api fastapi
API_URL ="http://localhost:8000"

#funcion para interactuar con el chatbot
def chatWithBot(user_input):
    response = requests.post(f"{API_URL}/chat/", json={"message": user_input})
    return response.json()['response']

#funcion para generar musica
def generateMusic(style, bpm, rhythm, music_type):
    data = {
        "style": style,
        "bpm": bpm,
        "rhythm": rhythm,
        "type": music_type
    }
    response = requests.post(f"{API_URL}/generateMusic/", json=data)
    return response.json()['music']


#interfaz de usuario
st.title("generador de musica con IA: MGIA")

#seccion de chat
st.header('chat con el bot')
user_message = st.text.input('escribe tu mensaje:')
if user_message:
    bot_response = chatWithBot(user_input)
    st.write(f"Bot: {bot_response}")


#seccion generador de musica
st.header('Generador de Musica: MgIA')
style = st.text_input('Estilo de musica:')
bpm = st.number_input('BPM', min_value=60, max_value=200)
rythm = st.text_input('Ritmo:')
music_type = st.selectbox('Tipo de musica', ['instrumental', 'acapella', 'cancion completa'])

if st.button('Generar música'):
    music = generateMusic(style, bpm, rhythm, music_type)
    st.audio(music, format='audio/mp3')
