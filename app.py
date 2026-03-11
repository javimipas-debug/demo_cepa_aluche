import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aprendiendo Prompts con IA", page_icon="🧠")

# --- CONFIGURACIÓN DE LA IA ---
# NOTA: Cuidado al subir esto a GitHub público, ¡podrían desactivarte la clave!
api_key = 'AIzaSyAwGpfkLZeZXK22QHYDPJ3Bd8rH0Jaqqfc'

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash') # He puesto 1.5 que es la versión estable actual

st.title("🧠 Laboratorio de Prompts")
st.write("Aquí aprenderemos que **no es lo que pides, sino cómo lo pides**.")

# --- 1. SELECCIÓN DEL ROL (Contexto del Prompt) ---
st.subheader("1. Elige el 'Rol' de la IA")
opcion = st.selectbox(
    "¿Qué personalidad debe tener la IA?", 
    ["Traductor", "Experto Científico", "Explicación con Poema"]
)

# Definimos el contexto según la opción
if opcion == "Traductor":
    contexto = "Actúa como un traductor profesional bilingüe. Traduce el siguiente texto de forma natural al inglés y al español, explicando si hay alguna palabra difícil:"
elif opcion == "Experto Científico":
    contexto = "Eres un científico experto y divulgador. Explica el siguiente concepto de forma rigurosa pero que un alumno de secundaria pueda entenderlo perfectamente:"
else: # Poema
    contexto = "Eres un profesor poeta. Explica el siguiente tema del temario escolar usando un poema que rime, para que sea más fácil de memorizar:"

# --- 2. ENTRADA DEL ALUMNO ---
st.subheader("2. ¿Sobre qué quieres hablar?")
texto_usuario = st.text_input("Escribe el tema o frase:", "La fotosíntesis")

# --- 3. CONSTRUCCIÓN DEL PROMPT ---
# Juntamos el contexto con la entrada para que los alumnos vean la frase completa
prompt_final = f"{contexto} {texto_usuario}"

with st.expander("🔍 Ver el Prompt completo que recibirá la IA"):
    st.info(f"**Instrucción total:** {prompt_final}")

# --- EJECUCIÓN ---
if st.button("✨ Generar Respuesta"):
    if not api_key:
        st.error("Falta la API Key.")
    else:
        with st.spinner("Construyendo respuesta..."):
            response = model.generate_content(prompt_final)
            
            st.success("### Respuesta de la IA:")
            st.write(response.text)

            # --- EXPLICACIÓN DIDÁCTICA ---
            st.divider()
            st.subheader("💡 ¿Qué acaba de pasar?")
            st.write(f"La IA no solo ha leído '{texto_usuario}'. Ha recibido una instrucción detallada:")
            
            st.code(f"""
# Así se construye un Prompt profesional:
contexto = "{contexto}"
usuario = "{texto_usuario}"

prompt_completo = contexto + " " + usuario
response = model.generate_content(prompt_completo)
            """, language="python")
