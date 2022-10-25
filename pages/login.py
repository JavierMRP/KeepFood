import streamlit as st
from streamlit_elements import elements, mui, html
from PIL import Image

with elements("stack_buttons"):
  with st.container():
    with mui.Stack(direction="column", justifyContent="space-around",spacing={5}):
      mui.Typography("Iniciar Sesión",variant="h3",color="#DD0000",fontFamily="'Inter', sans-serif;",fontWeight="bold")
      with mui.Stack(direction="column", justifyContent="space-around",spacing={1}):
        mui.Typography("Correo Electrónico",variant="h5",color="black",fontFamily="'Inter', sans-serif;",fontWeight="bold") 
        mui.TextField(
          id="outlined-required",
          label="Correo electrónico",
          type="email"
        )  
      with mui.Stack(direction="column", justifyContent="space-around",spacing={1}):
        mui.Typography("Contraseña",variant="h5",color="black",fontFamily="'Inter', sans-serif;",fontWeight="bold") 
        mui.TextField(
          label="Contraseña",
          type="password",
          autoComplete="current-password"
        )
      with mui.Button(variant="contained"):
          mui.Typography("Iniciar Sesión")
      mui.Typography("Continuando con el correo o google, tu aceptas los Términos de servicios y Política de privacidad.")