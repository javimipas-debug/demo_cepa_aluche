import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mi App con IA", page_icon="🤖")

# --- CONFIGURACIÓN DE LA IA ---
# En un entorno real usaríamos st.secrets, pero para clase pediremos la clave:
api_key = 'AIzaSyAwGpfkLZeZXK22QHYDPJ3Bd8rH0Jaqqfc'

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash') # El modelo más rápido y gratuito

st.title("🤖 Transformador con Inteligencia Artificial")

# --- ENTRADA ---
texto_usuario = st.text_input("Escribe una frase para la IA:", "Inventa un chiste sobre programadores")

opcion = st.selectbox("¿Qué debe hacer la IA?", 
                     ["Resumir", "Traducir a Inglés", "Convertir en Poema", "Explicar como a un niño"])

if st.button("✨ ¡Ejecutar Magia!"):
    if not api_key:
        st.error("¡Necesitas pegar la API Key en la barra lateral!")
    else:
        with st.spinner("La IA está pensando..."):
            # Creamos el "Prompt" (la instrucción)
            prompt = f"{opcion}: {texto_usuario}"
            
            # Llamada a la IA
            response = model.generate_content(prompt)
            resultado = response.text
            
            st.success("### Resultado de la IA:")
            st.write(resultado)

            # --- EXPLICACIÓN DEL CÓDIGO ---
            st.divider()
            st.subheader("💡 El código detrás de la IA")
            st.code(f"""
# 1. Configuramos la IA
genai.configure(api_key="TU_CLAVE")

# 2. Elegimos el modelo
model = genai.GenerativeModel('gemini-2.5-flash')

# 3. Enviamos tu instrucción (Prompt)
prompt = "{opcion}: {texto_usuario}"
response = model.generate_content(prompt)

print(response.text)
            """, language="python")
else:
    st.info("Escribe algo y pulsa el botón para ver la magia.")
