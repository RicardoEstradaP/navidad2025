import streamlit as st

# -------------------- CONFIGURACIÓN Y ESTILO --------------------
st.set_page_config(page_title="Quiz Navideño de Bondad", page_icon="🎄")

navidad_css = """
<style>
body {
    background: #f0f6ff;
}
.navidad-box {
    padding: 20px;
    border-radius: 12px;
    background: #ffffffcc;
    border: none; /* CORREGIDO: sin borde punteado */
    box-shadow: 0 0 12px rgba(0,0,0,0.10);
}
h1 {
    color: #136f63;
    text-shadow: 1px 1px 2px #fff;
}
</style>
"""
st.markdown(navidad_css, unsafe_allow_html=True)

st.markdown("<h1>🎄 Quiz Navideño de Bondad 🎁</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Descubre si este año te toca regalo, muchos regalos… o carbón. 👀</p>", unsafe_allow_html=True)


# ---------- PREGUNTAS ---------------------
preguntas_docente = [
    "¿Has devuelto tareas con retroalimentación navideña, cálida y sin juzgar?",
    "¿Has dado extensiones sin hacerlo ver como ‘un milagro’ de tu generosidad?",
    "¿Has evitado regañar grupos completos por culpa de uno?",
    "¿Has promovido el autocuidado emocional en tus estudiantes?",
    "¿Has revisado trabajos antes del límite sin que te lo pidan 15 veces?"
]

preguntas_estudiante = [
    "¿Has entregado tus actividades sin llorar en el último minuto?",
    "¿Has sido amable con tus docentes incluso en semanas de parciales?",
    "¿Has evitado hacer trabajos con IA sin criterio (y sin citar)?",
    "¿Has apoyado emocionalmente a tus compañerxs cuando están saturados?",
    "¿Has leído las instrucciones antes de preguntar?"
]

# -------------------- VARIABLES DE SESIÓN --------------------
if "rol" not in st.session_state:
    st.session_state.rol = None

if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 0

if "respuestas" not in st.session_state:
    st.session_state.respuestas = []


# -------------------- SELECCIÓN DE ROL --------------------
if st.session_state.rol is None:
    st.markdown("### 🎅 ¿Eres docente o estudiante de psicología?")
    rol = st.radio("", ["Docente", "Estudiante"])

    if st.button("Iniciar Quiz 🎁"):
        st.session_state.rol = rol
        st.rerun()

else:
    st.markdown("<div class='navidad-box'>", unsafe_allow_html=True)
    st.markdown(f"### 🎄 Rol seleccionado: **{st.session_state.rol}** 🎅")

    preguntas = preguntas_docente if st.session_state.rol == "Docente" else preguntas_estudiante

    total_preguntas = len(preguntas)
    idx = st.session_state.pregunta_actual

    # -------------------- MOSTRAR PREGUNTA ACTUAL --------------------
    if idx < total_preguntas:
        st.markdown(f"### 🎁 Pregunta {idx+1} de {total_preguntas}")
        st.write(preguntas[idx])

        respuesta = st.radio("Elige una opción", ["Sí", "No"], key=f"preg_{idx}")

        if st.button("Siguiente ❄️"):
            st.session_state.respuestas.append(respuesta)
            st.session_state.pregunta_actual += 1
            st.rerun()

    else:
        # -------------------- RESULTADOS --------------------
        puntaje = st.session_state.respuestas.count("Sí")

        st.markdown("## 🎅 Resultado Final Navideño")

        if puntaje == 0:
            st.error("😈 ¡Uy! Este año te toca carbón… del bueno, del que mancha. 🧱")
            regalos = 0
        elif puntaje <= 2:
            st.warning("🎁 Te toca **un regalito**… chiquito, como tu fuerza para no procrastinar.")
            regalos = 1
        elif puntaje <= 4:
            st.success("🎁🎁 ¡Te corresponden **dos regalos**! Claramente tienes espíritu navideño moderado.")
            regalos = 2
        else:
            st.balloons()
            st.success("🎁🎁🎁 ¡Eres la estrella del arbolito! Te corresponden **tres regalos y un abrazo psicológico**.")
            regalos = 3

        st.markdown(f"### 🎄 Total de regalos asignados: **{regalos}** 🎁")

        # -------------------- DISCLAIMER ACTUALIZADO --------------------
        st.markdown("""
        ---
        ### 📬 *Aviso Navideño*
        Pasa tu reporte, adjunto a tu carta para Santa Claus.  
        **Mayu y Ricky no se hacen responsables si recibes puro carbón**  
        ¡Feliz Navidad! 🎄
        """)

        if st.button("Reiniciar 🎄"):
            st.session_state.rol = None
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas = []
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
