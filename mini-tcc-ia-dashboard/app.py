import streamlit as st

with st.form("formulario_perfil"):

    area = st.selectbox(
        "Área de interesse:",
        [
            "Data Science",
            "Inteligência Artificial",
            "Cybersecurity",
            "Cloud Computing",
            "UX/UI Design",
        ]
    )

    nivel = st.selectbox(
        "Nível de programação:",
        [
            "Iniciante",
            "Intermediário",
            "Avançado"
        ]
    )

    experiencia = st.selectbox(
        "Experiência em programação:",
        [
            "Nenhuma",
            "Pouca",
            "Moderada",
            "Muita"
        ]
    )

    horas = st.slider(
        "Horas de estudo por semana:",
        1,
        40,
        10
    )

    objetivo = st.selectbox(
        "Objetivo:",
        [
            "Primeiro emprego",
            "Transição de carreira",
            "Aprimoramento profissional",
            "Empreendedorismo",
            "Curiosidade",
        ]
    )

    enviar = st.form_submit_button("Analisar perfil")


if enviar:

    nivel_numerico = {
        "Iniciante": 1,
        "Intermediário": 2,
        "Avançado": 3
    }

    nivel_codigo = nivel_numerico[nivel]

    curso = recomendar_curso(
        nivel_codigo,
        experiencia,
        horas
    )

    dados = (
        nome,
        idade,
        cidade,
        estado,
        latitude,
        longitude,
        nivel,
        area,
        experiencia,
        horas,
        objetivo,
        curso,
    )

    inserir_interessado(dados)

    st.success("Perfil analisado com sucesso!")

    st.info(
        f"🎯 Curso recomendado pela IA: **{curso}**"
    )
