import streamlit as st
from streamlit_elements import elements, mui, html

with elements("stack_buttons"):
  with st.container():
    with mui.Stack(direction="column", justifyContent="space-around",spacing={5}):
        mui.Typography("Registrarse",variant="h3",color="#DD0000",fontFamily="'Inter', sans-serif;",fontWeight="bold") 
        with mui.Stack(direction="column", justifyContent="space-around",spacing={1}):
            mui.Typography("Nombre de usuario",variant="h5",color="black",fontFamily="'Inter', sans-serif;",fontWeight="bold") 
            mui.TextField(
            id="outlined-required",
            label="Nombre de usuario",
            type="user"
            ) 
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
        with mui.Stack(direction="column", justifyContent="space-around",spacing={1}):
            mui.Typography("Confirmar contraseña",variant="h5",color="black",fontFamily="'Inter', sans-serif;",fontWeight="bold") 
            mui.TextField(
            label="Confirmar contraseña",
            type="password",
            autoComplete="current-password"
            )
        with mui.Button(variant="contained"):
            mui.Typography("Registrarse")
        