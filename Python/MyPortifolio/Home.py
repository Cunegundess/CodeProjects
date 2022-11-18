import streamlit as st
from PIL import Image


st.set_page_config(
    layout = 'wide', 
    page_icon = 'random', 
    initial_sidebar_state = 'collapsed', 
    page_title = 'Portifólio')

fotoPerfil = Image.open('images/FotoPerfil.jpg')
imgBook = Image.open('images/book.png')
imgMap = Image.open('images/map.png')
imgList = Image.open('images/list.png')
imgProduct = Image.open('images/product.png')
imgDocs = Image.open('images/docs.png')

col1, col2 = st.columns(2)

with col1: 
    col1.image(fotoPerfil, width = 500)

with col2:
    col2.title("Hello I'm Lucas")
    col2.header('_Sobre mim:_')
    col2.write('''
    - Estudando Análise e Desenvolvimento de Sistemas no Centro Universitário ETEP.\n
    - Explorando novas tecnologias e testando novas ideias.\n
    - Aprendendo mais sobre Python.\n
    ''')
    col2.code('''
    def Lucas():
        name = "LUCAS CUNEGUNDES DE SANTANA"
        acknowledgements = "PROGRAMAÇÃO & DESENVOLVIMENTO"
        primarySkillset = "ALGUMAS HABILIDADES"
        languages = ["HTML", "CSS", "Python"]
    ''')

st.subheader('')
st.title("Alguns dos Projetos que já trabalhei em Python:")

col3, col4 = st.columns(2)

with col3: 
    col3.subheader("BookStore App")
    col3.write('''
    Who doesn't like to read sometimes?\n 
    This app was made to better organize your favorites, 
    add new books, delete old ones, or maybe even update an existing one. Pretty cool right?
    ''')
    col3.image(imgBook, width = 250)

with col4: 
    col4.subheader("GeoMap App")
    col4.write('''
    Who knows when the next big eruption of a volcano could be?\n 
    With this App you can keep up to date on the nearest location of these big boys, 
    you can even get an idea of ​​their height, as well as being able to add your own markers. 
    I think it will be very useful in your adventure.
    ''')
    col4.image(imgMap, width = 250)

st.subheader('')
st.title("Alguns dos Projetos Web que já trabalhei:")

col5, col6, col7 = st.columns(3)

with col5:
    col5.subheader('Todo App')
    col5.write('''
    Nobody likes to work in the middle of the mess, including me.\n
    That's why I had the idea to create this application, it's been very useful to me. 
    I believe it will be very useful for you too. 
    It doesn't cost anything to try
    ''')
    col5.image(imgList, width = 250)
    
with col6: 
    col6.subheader('Documentation Page')
    col6.write('''
    JavaScript can give you serious headaches, and your best friend will be documentation.\n 
    This saved me in some projects, maybe it will save in yours too. Give it a try ;)
    ''')
    col6.image(imgDocs, width = 250)

with col7:
    col7.subheader('E-commerce Product Page')
    col7.write('''
    Going to a store in person to shop can be quite tiring, and at these times, 
    shopping online is the best option.\n 
    I mean, everthing is online now, and who knows if you'll want to 
    play some music, and where you'll find a instrument, that's why i think shopping online is the better
    ''')
    col7.image(imgProduct, width = 250)

st.subheader('')
st.title('Social Media:')

col8, col9, col10 = st.columns(3)

with col8:
    col8.subheader('GitHub:')
    col8.write('https://www.github.com/Cunegundess')


with col9:
    col9.subheader('LinkedIn:')
    col9.write('https://www.linkedin.com/in/lucas-cunegundes/')
