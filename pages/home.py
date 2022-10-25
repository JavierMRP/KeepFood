import streamlit as st
from streamlit_elements import elements, mui, html
from PIL import Image


with elements("stack_home"):
    with st.container():
        #mui.Typography("Home",variant="h3",color="#DD0000",fontFamily="'Inter', sans-serif;",fontWeight="bold")
        with mui.Stack(direction="raw", justifyContent="space-evenly"):
            with mui.Stack(direction="column", justifyContent="space-around",spacing={5}):
                mui.Box(
                    component="img",
                    src="https://firebasestorage.googleapis.com/v0/b/proyectodesarolloweb.appspot.com/o/logo.png?alt=media&token=527802e1-b5ca-4eb7-8b97-d65b821a966d"
                )
                with mui.Button(variant="contained"):
                    mui.Typography("Inventario")
                with mui.Button(variant="contained"):
                    mui.Typography("Ingresar Platos")
                with mui.Button(variant="contained"):
                    mui.Typography("Recomendaciones")
                with mui.Button(variant="contained"):
                    mui.Typography("Platos disponibles")
                with mui.Button(variant="contained"):
                    mui.Typography("Dashboard")
                with mui.Button(variant="contained"):
                    mui.Typography("Salir")

