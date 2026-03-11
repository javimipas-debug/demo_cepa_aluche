import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Editor Mágico para Clase", page_icon="📝")

st.title("📝 Transformador de Texto Interactivo")
st.write("Cualquier cosa que escribas aquí pasará por un filtro de Python.")

# --- ENTRADA DE USUARIO ---
st.subheader("1. Escribe tu mensaje")
texto_usuario = st.text_input("Mensaje original:", "Hola Mundo")

# --- MENÚ DE OPCIONES ---
opcion = st.selectbox(
    "¿Qué transformación quieres aplicar?", 
    ["Convertir a MAYÚSCULAS", "Invertir el texto", "Contar letras"]
)

# --- LÓGICA DE TRANSFORMACIÓN ---
# Aquí guardaremos el resultado y el fragmento de código que vamos a explicar
if opcion == "Convertir a MAYÚSCULAS":
    resultado = texto_usuario.upper()
    explicacion_codigo = f'resultado = "{texto_usuario}".upper()'
    
elif opcion == "Invertir el texto":
    resultado = texto_usuario[::-1]
    explicacion_codigo = f'resultado = "{texto_usuario}"[::-1]'
    
else: # Contar letras
    resultado = len(texto_usuario)
    explicacion_codigo = f'resultado = len("{texto_usuario}")'

# --- RESULTADO VISUAL ---
st.subheader("2. Resultado")
st.success(f"El resultado final es: **{resultado}**")

# --- EXPLICACIÓN DEL CÓDIGO (Dinámica) ---
st.divider()
st.subheader("💡 ¿Cómo lo hace Python?")
st.write(f"Como has seleccionado **{opcion}**, la línea de código que se está ejecutando internamente es:")

# Mostramos el bloque de código específico según la opción
st.code(f"""
# Código de Python:
{explicacion_codigo}
""", language="python")

st.info("💡 Fíjate cómo cambian las comillas y los métodos según lo que eliges arriba.")
