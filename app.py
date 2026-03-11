import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi App Educativa", page_icon="🚀")

st.title("🚀 Mi Primera App Interactiva")
st.write("¡Hola! Esta app demuestra cómo Python puede transformar datos en segundos.")

# --- ENTRADA DE USUARIO ---
st.subheader("1. Escribe algo")
texto_usuario = st.text_input("Introduce un mensaje:", "Streamlit es genial")

# --- LÓGICA SENCILLA ---
opcion = st.selectbox("¿Qué quieres hacer?", ["Convertir a MAYÚSCULAS", "Invertir el texto", "Contar letras"])

if opcion == "Convertir a MAYÚSCULAS":
    resultado = texto_usuario.upper()
elif opcion == "Invertir el texto":
    resultado = texto_usuario[::-1]
else:
    resultado = len(texto_usuario)

# --- RESULTADO ---
st.subheader("2. Resultado")
st.success(f"El resultado es: **{resultado}**")

# --- EXPLICACIÓN DEL CÓDIGO ---
st.divider()
st.subheader("💡 ¿Cómo funciona?")
st.write("Aquí abajo tienes el código que está ejecutando esta página:")
st.code(f"""
# Así de fácil se programa esto:
if opcion == "Invertir el texto":
    resultado = "{texto_usuario}"[::-1]
""", language="python")
