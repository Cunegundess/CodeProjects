import streamlit as st
from sendEmail import sendEmail


st.header('Contact Me')

with st.form(key = 'email_forms'):

    userEmail = st.text_input('Insira seu Email:')
    rawMessage = st.text_area('Escreva o seu recado:')
    message = f'''\
    New Email from {userEmail}
    
    {userEmail}\n
    {rawMessage}
    '''
    submitButton = st.form_submit_button('Enviar')

    if submitButton:
        sendEmail(message)
        st.info('Seu email foi enviado com sucesso')