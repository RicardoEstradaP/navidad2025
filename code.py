import streamlit as st

# ---------------------- DECORACIÓN NAVIDEÑA ----------------------
st.set_page_config(page_title="Quiz Navideño de Bondad", page_icon="🎄")

navidad_css = """
<style>
body {
    background: #f0f6ff;
}
.navidad-box {
    padding: 20px;
    border-radius: 12px;
    background: #ffffffaa;
    border: 2px dashed #d62828;
    box-shadow: 0 0 12px rgba(0,0,0,0.15);
}
h1 {
    color: #136f63;
    text-shadow: 1px 1px 2px #fff;
}
.role-box {
    background: #ffe8d6;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddbea9;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(navidad_css, unsafe_allow_html=True)

st.markdown("<h1>🎄 Quiz Navideño de Bondad 🎁</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;'>Descubre si este año te toca regalo, muchos regalos… o carbón. 👀</p>", unsafe_allow_html=True)

st.markdown("<div class='navidad-box'>", unsafe_allow_html=True)


# ---------------------- FILTRO DE ROL ----------------------
st.markdown("### 🎅 ¿Eres docente o estudiante de psicología?")
rol = st.radio("", ["Docente", "Estudiante"])


# ---------------------- PREGUNTAS ----------------------

preguntas_docente = {
    "¿Has devuelto tareas con retroalimentación navideña, cálida y sin juzgar?": 1,
    "¿Has dado extensiones sin hacerlo ver como ‘un milagro’ de tu generosidad?": 1,
    "¿Has evitado regañar grupos completos por culpa de uno?": 1,
    "¿Has promovido el autocuidado emocional en tus estudiantes?": 1,
    "¿Has revisado trabajos antes del límite sin que te lo pidan 15 veces?": 1,
}

preguntas_estudiante = {
    "¿Has entregado tus actividades sin llorar en el último minuto?": 1,
    "¿Has sido amable con tus docentes incluso en semanas de parciales?": 1,
    "¿Has evitado hacer trabajos con IA sin criterio (y sin citar)?": 1,
    "¿Has apoyado emocionalmente a tus compañerxs cuando están saturados?": 1,
    "¿Has leído las instrucciones antes de preguntar?": 1,
}

# según rol seleccionamos preguntas
preguntas = preguntas_docente if rol == "Docente" else preguntas_estudiante


# ---------------------- RESPUESTAS ----------------------
st.markdown("### 🎄 Responde con sinceridad navideña:")

respuestas = []
for pregunta in preguntas:
    opcion = st.radio(pregunta, ["Sí", "No"], key=pregunta)
    respuestas.append(opcion)


# ---------------------- RESULTADOS ----------------------
if st.button("🎁 Ver mi resultado navideño"):
    puntaje = sum(1 for r in respuestas if r == "Sí")

    st.markdown("## 🎄 Resultado Final 🎅")

    if puntaje == 0:
        st.error("😈 ¡Uy! Este año te toca carbón… del bueno, del que mancha. 🧱")
        regalos = 0
    elif puntaje <= 2:
        st.warning("🎁 Te toca **un regalito**… chiquito, como tu fuerza de voluntad para no procrastinar.")
        regalos = 1
    elif puntaje <= 4:
        st.success("🎁🎁 ¡Te corresponden **dos regalos**! Claramente tienes espíritu navideño moderado.")
        regalos = 2
    else:
        st.balloons()
        st.success("🎁🎁🎁 ¡Eres la estrella del arbolito! Te corresponden **tres regalos y un abrazo psicológico**.")
        regalos = 3

    st.markdown(f"### 🎄 Total de regalos asignados: **{regalos}** 🎁")

    # DISCLAIMER
    st.markdown("""
    ---
    ### 📬 *Disclaimer Navideño Importante*
    Pasa tu reporte, adjunto a tu carta para Santa Claus.  
    **Mayu y Ricky no se hacen responsables si recibes puro carbón**  
    ¡Feliz Navidad! 🎄
    """)
    
st.markdown("</div>", unsafe_allow_html=True)
