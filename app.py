import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image
from streamlit_elements import elements, mui, html
from pages import home, register, login




with elements("stack_buttons"):
  with st.container():
    with mui.Stack(direction="row", justifyContent="space-around"):
      with mui.Stack(direction="row",justifyContent="flex-start",):
        mui.Box(
              component="img",
              src="https://firebasestorage.googleapis.com/v0/b/proyectodesarolloweb.appspot.com/o/logo.png?alt=media&token=527802e1-b5ca-4eb7-8b97-d65b821a966d"
          )
      with mui.Stack(direction="row", spacing={2},justifyContent="flex-end",alignItems="center"):
        with mui.Button(variant="contained"):
          mui.Typography("Iniciar Sesión")
        with mui.Button(variant="outlined"):
          mui.Typography("Registrarse")


inventario = Image.open('./img/inventario.png')
st.image(inventario, use_column_width=True)

with elements("stack_slogan"):
  with mui.Stack(direction="column",justifyContent="center",alignItems="center"):
    mui.Typography("Keep Food",variant="h3",color="black",fontFamily="'Inter', sans-serif;",fontWeight="bold")
    mui.Typography("Cómida de hoy, inventario de hoy",variant="h4",fontFamily="'Inter', sans-serif;")
    mui.Typography("Administra, ordena, dispone y coordina tu inventario.",variant="h6",fontFamily="'Inter', sans-serif;")
 
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)







