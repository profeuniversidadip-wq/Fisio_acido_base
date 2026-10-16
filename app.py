
import streamlit as st

st.set_page_config(
    page_title="FisioÁcidoBase IA",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.block-container {padding-top: 2.4rem; padding-bottom: 1.2rem; max-width: 1050px;}
html, body, [class*="css"] {font-size: 17px;}
.main-title {font-size: 1.65rem; font-weight: 800; margin-bottom: .15rem;}
.subtitle {font-size: .92rem; opacity:.82; margin-bottom: .55rem;}
.card {
    border:1px solid rgba(80,110,140,.25);
    border-radius:14px;
    padding:16px 18px;
    margin:.5rem 0 1rem 0;
    background:rgba(230,244,255,.45);
}
.eq {
    font-size:1.35rem;
    font-weight:700;
    text-align:center;
    padding:14px;
    border-radius:12px;
    border:1px solid rgba(80,110,140,.25);
    margin:.75rem 0;
}
.small {font-size:.92rem; opacity:.82;}
.status-card {
    border-radius:12px;
    padding:10px 12px;
    margin:.35rem 0;
    border:1px solid rgba(80,110,140,.22);
}
.status-normal {background:#E8F5E9; border-left:7px solid #2E7D32;}
.status-acid {background:#FFEBEE; border-left:7px solid #C62828;}
.status-alk {background:#E3F2FD; border-left:7px solid #1565C0;}
.status-warn {background:#FFF8E1; border-left:7px solid #F9A825;}
.big-state {font-size:1.05rem; font-weight:800; margin-bottom:.15rem;}
.flow-box {
    text-align:center;
    font-size:.92rem;
    font-weight:700;
    padding:12px 10px;
    border-radius:12px;
    background:rgba(255,255,255,.72);
    border:1px solid rgba(80,110,140,.20);
    margin-top:.55rem;
}

@media (max-width: 760px) {
    .block-container {
        padding-top: 2.2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    .main-title {
        font-size: 1.35rem !important;
        line-height: 1.18 !important;
        margin-top: .35rem !important;
        margin-bottom: .45rem !important;
    }
    .subtitle {
        font-size: .95rem !important;
        line-height: 1.3 !important;
    }
    [data-testid="stHorizontalBlock"] {
        flex-direction: column !important;
        gap: .35rem !important;
    }
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }
    div[data-testid="stSlider"] {
        padding-bottom: .5rem !important;
    }
    .status-card {
        padding: 13px 14px !important;
        margin: .45rem 0 !important;
    }
    .big-state {
        font-size: 1.08rem !important;
    }
    .flow-box {
        font-size: .96rem !important;
        padding: 10px 8px !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: .15rem !important;
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
    }
    .stTabs [data-baseweb="tab"] {
        white-space: nowrap !important;
        padding-left: .65rem !important;
        padding-right: .65rem !important;
    }
}


.summary-state {
    border-radius:14px;
    padding:11px 14px;
    margin:.35rem 0 .55rem 0;
    font-weight:700;
    border:1px solid rgba(80,110,140,.22);
}
.summary-normal {background:#E8F5E9; border-left:8px solid #2E7D32;}
.summary-acid {background:#FFEBEE; border-left:8px solid #C62828;}
.summary-alk {background:#E3F2FD; border-left:8px solid #1565C0;}
.summary-warn {background:#FFF8E1; border-left:8px solid #F9A825;}
.summary-title {font-size:1.12rem; font-weight:800;}
.summary-mini {font-size:.88rem; margin-top:.1rem;}

.round-badge {
    display:inline-block;
    padding:5px 10px;
    border-radius:999px;
    font-weight:800;
    font-size:.88rem;
    margin-bottom:.45rem;
}
.round-1 {background:#E3F2FD; border:1px solid #64B5F6;}
.round-2 {background:#E8F5E9; border:1px solid #66BB6A;}
.round-3 {background:#FFF3E0; border:1px solid #FFA726;}
.exercise-card {
    border:1px solid rgba(80,110,140,.22);
    border-radius:12px;
    padding:12px 14px;
    margin:.45rem 0 .75rem 0;
    background:rgba(245,249,252,.72);
}
.dot-blue,.dot-green,.dot-orange {
    display:inline-block;
    width:10px;
    height:10px;
    border-radius:50%;
    margin-right:7px;
}
.dot-blue {background:#1E88E5;}
.dot-green {background:#43A047;}
.dot-orange {background:#FB8C00;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Equilibrio ácido-base</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Comprender antes de memorizar · Fisiología y Fisiopatología · Kinesiología</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["1. Fundamentos", "2. Simulador", "3. Gasometría", "4. Práctica"])

with tab1:
    st.subheader("La idea central")
    st.markdown("""
    <div class="card">
    El equilibrio ácido-base depende del control de la concentración de H⁺ en los líquidos corporales.
    En sangre arterial, el intervalo de pH presentado en el material es <b>7,35–7,45</b>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="eq">CO₂ + H₂O ⇄ H₂CO₃ ⇄ H⁺ + HCO₃⁻</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### Pulmón")
        st.write("Regula el CO₂ mediante la ventilación.")
        st.write("↑ eliminación de CO₂ → ↓ H⁺ → ↑ pH")
        st.write("↓ eliminación de CO₂ → ↑ H⁺ → ↓ pH")
    with c2:
        st.markdown("### Riñón")
        st.write("Secreta H⁺ y reabsorbe HCO₃⁻.")
        st.write("Puede modificar el pH ajustando la excreción de ácido y el manejo de bicarbonato.")
    with c3:
        st.markdown("### Amortiguadores")
        st.write("Proteínas, bicarbonato/ácido carbónico y fosfatos.")
        st.write("Actúan limitando cambios bruscos de H⁺.")

    st.subheader("Cómo reconocer el origen del trastorno")
    st.markdown("""
    - Si el cambio primario está en **PCO₂**, el origen es **respiratorio**.
    - Si el cambio primario está en **HCO₃⁻**, el origen es **metabólico**.
    - La compensación respiratoria actúa sobre trastornos metabólicos.
    - La compensación renal actúa sobre trastornos respiratorios.
    """)

with tab2:
    st.subheader("Simulador dinámico")
    st.caption("Mueve los faders y observa de inmediato la tendencia ácido-base.")

    # Controles compactos
    c1, c2 = st.columns(2)
    with c1:
        pco2 = st.slider("PCO₂ (mmHg)", 20, 70, 40, 1)
        ventilacion = st.slider(
            "Ventilación relativa (%)", 25, 200, 100, 5,
            help="100% representa una condición de referencia conceptual."
        )
    with c2:
        hco3 = st.slider("HCO₃⁻ (mEq/L)", 10, 40, 24, 1)
        excrecion_h = st.slider(
            "Excreción renal H⁺ (%)", 25, 200, 100, 5,
            help="100% representa una condición de referencia conceptual."
        )

    # Puntaje cualitativo para resumen inmediato
    acid_score = 0
    alk_score = 0

    if pco2 > 45: acid_score += 2
    elif pco2 < 35: alk_score += 2

    if hco3 < 22: acid_score += 2
    elif hco3 > 26: alk_score += 2

    if ventilacion < 80: acid_score += 1
    elif ventilacion > 120: alk_score += 1

    if excrecion_h < 80: acid_score += 1
    elif excrecion_h > 120: alk_score += 1

    # Resumen visible inmediatamente
    if acid_score == 0 and alk_score == 0:
        global_txt = "Condición cercana a referencia"
        global_cls = "summary-normal"
        global_msg = "Sin predominio acidificante ni alcalinizante."
    elif acid_score > alk_score:
        global_txt = "Predominio acidificante"
        global_cls = "summary-acid"
        global_msg = "Las variables favorecen ↑ H⁺ y tendencia a ↓ pH."
    elif alk_score > acid_score:
        global_txt = "Predominio alcalinizante"
        global_cls = "summary-alk"
        global_msg = "Las variables favorecen ↓ H⁺ y tendencia a ↑ pH."
    else:
        global_txt = "Fuerzas opuestas"
        global_cls = "summary-warn"
        global_msg = "Puede existir compensación o un patrón mixto. Debe integrarse con pH, PCO₂ y HCO₃⁻."

    st.markdown(
        f'<div class="summary-state {global_cls}">'
        f'<div class="summary-title">{global_txt}</div>'
        f'<div class="summary-mini">{global_msg}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Lectura específica, compacta
    r1, r2 = st.columns(2)

    with r1:
        if pco2 > 45:
            st.markdown('<div class="status-card status-acid"><div class="big-state">PCO₂ alta → tendencia respiratoria acidificante</div><div>↑ CO₂ → ↑ H⁺ → ↓ pH</div></div>', unsafe_allow_html=True)
        elif pco2 < 35:
            st.markdown('<div class="status-card status-alk"><div class="big-state">PCO₂ baja → tendencia respiratoria alcalinizante</div><div>↓ CO₂ → ↓ H⁺ → ↑ pH</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-card status-normal"><div class="big-state">PCO₂ en rango</div><div>35–45 mmHg</div></div>', unsafe_allow_html=True)

        if ventilacion < 80:
            st.markdown('<div class="status-card status-acid"><div class="big-state">Hipoventilación relativa</div><div>↓ ventilación → ↑ CO₂ → ↓ pH</div></div>', unsafe_allow_html=True)
        elif ventilacion > 120:
            st.markdown('<div class="status-card status-alk"><div class="big-state">Hiperventilación relativa</div><div>↑ ventilación → ↓ CO₂ → ↑ pH</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-card status-normal"><div class="big-state">Ventilación cercana a referencia</div></div>', unsafe_allow_html=True)

    with r2:
        if hco3 < 22:
            st.markdown('<div class="status-card status-acid"><div class="big-state">HCO₃⁻ bajo → tendencia metabólica acidificante</div><div>Menor base disponible → tendencia a ↓ pH</div></div>', unsafe_allow_html=True)
        elif hco3 > 26:
            st.markdown('<div class="status-card status-alk"><div class="big-state">HCO₃⁻ alto → tendencia metabólica alcalinizante</div><div>Mayor componente básico → tendencia a ↑ pH</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-card status-normal"><div class="big-state">HCO₃⁻ en rango</div><div>22–26 mEq/L</div></div>', unsafe_allow_html=True)

        if excrecion_h < 80:
            st.markdown('<div class="status-card status-acid"><div class="big-state">Menor excreción renal de H⁺</div><div>Retención relativa de ácido → ↓ pH</div></div>', unsafe_allow_html=True)
        elif excrecion_h > 120:
            st.markdown('<div class="status-card status-alk"><div class="big-state">Mayor excreción renal de H⁺</div><div>Menor carga ácida → ↑ pH</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-card status-normal"><div class="big-state">Excreción renal cercana a referencia</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="flow-box">CO₂ + H₂O ⇄ H₂CO₃ ⇄ H⁺ + HCO₃⁻</div>', unsafe_allow_html=True)
    st.caption("Simulación cualitativa educativa: no calcula compensaciones esperadas ni trastornos mixtos complejos.")

with tab3:
    st.subheader("Interpretación guiada de gasometría")
    st.caption("Secuencia: pH → PCO₂ → HCO₃⁻ → origen probable → compensación.")

    c1,c2,c3 = st.columns(3)
    with c1:
        ph = st.number_input("pH", min_value=6.50, max_value=8.00, value=7.40, step=0.01, format="%.2f")
    with c2:
        pco2 = st.number_input("PCO₂ (mmHg)", min_value=10.0, max_value=100.0, value=40.0, step=1.0)
    with c3:
        hco3 = st.number_input("HCO₃⁻ (mEq/L)", min_value=5.0, max_value=50.0, value=24.0, step=1.0)

    if st.button("Interpretar paso a paso", type="primary", use_container_width=True):
        if ph < 7.35:
            estado_ph = "pH bajo"
            direccion = "acidificante"
        elif ph > 7.45:
            estado_ph = "pH alto"
            direccion = "alcalinizante"
        else:
            estado_ph = "pH dentro de 7,35–7,45"
            direccion = "cercano a normal"

        pco2_estado = "alta" if pco2 > 45 else "baja" if pco2 < 35 else "normal"
        hco3_estado = "alto" if hco3 > 26 else "bajo" if hco3 < 22 else "normal"

        st.markdown(f"**Paso 1. pH:** {estado_ph}.")
        st.markdown(f"**Paso 2. PCO₂:** {pco2:.0f} mmHg → {pco2_estado}.")
        st.markdown(f"**Paso 3. HCO₃⁻:** {hco3:.0f} mEq/L → {hco3_estado}.")

        diagnostico = []
        if ph < 7.35:
            if pco2 > 45: diagnostico.append("componente respiratorio acidificante")
            if hco3 < 22: diagnostico.append("componente metabólico acidificante")
        elif ph > 7.45:
            if pco2 < 35: diagnostico.append("componente respiratorio alcalinizante")
            if hco3 > 26: diagnostico.append("componente metabólico alcalinizante")

        if diagnostico:
            st.markdown("**Paso 4. Alteración compatible:** " + " + ".join(diagnostico) + ".")
        else:
            st.markdown("**Paso 4.** Con estos tres valores no aparece un patrón primario simple fuera de rango.")

        # Reconocimiento pedagógico de posible compensación, sin fórmulas cuantitativas
        comp = []
        if ph < 7.35 and pco2 > 45 and hco3 > 26:
            comp.append("HCO₃⁻ elevado puede representar respuesta renal compensatoria a un trastorno respiratorio.")
        if ph > 7.45 and pco2 < 35 and hco3 < 22:
            comp.append("HCO₃⁻ bajo puede representar respuesta renal compensatoria a un trastorno respiratorio.")
        if ph < 7.35 and hco3 < 22 and pco2 < 35:
            comp.append("PCO₂ baja puede representar respuesta respiratoria compensatoria a un trastorno metabólico.")
        if ph > 7.45 and hco3 > 26 and pco2 > 45:
            comp.append("PCO₂ alta puede representar respuesta respiratoria compensatoria a un trastorno metabólico.")

        if comp:
            st.info("**Paso 5. Compensación posible:** " + " ".join(comp))
        else:
            st.caption("La aplicación no calcula compensación esperada cuantitativa ni trastornos mixtos complejos en esta primera versión.")

with tab4:
    st.subheader("Práctica progresiva")
    st.caption("Tres tandas. La dificultad aumenta desde relaciones básicas hasta integración clínica.")

    tanda1, tanda2, tanda3 = st.tabs(["🔵 Tanda 1 · Fundamentos", "🟢 Tanda 2 · Aplicación", "🟠 Tanda 3 · Clínica"])

    def ejercicio(caso, opciones, correcta, explicacion, key):
        st.markdown(f'<div class="exercise-card"><b>{caso}</b></div>', unsafe_allow_html=True)
        r = st.radio("Selecciona una respuesta", opciones, key=f"r_{key}", index=None)
        if st.button("Responder", key=f"b_{key}", use_container_width=True):
            if r is None:
                st.warning("Selecciona una alternativa.")
            elif r == correcta:
                st.success("Correcto.")
                st.info("¿Por qué? " + explicacion)
            else:
                st.error("Respuesta incorrecta.")
                st.info("¿Por qué? " + explicacion)

    with tanda1:
        st.markdown('<span class="round-badge round-1">Tanda 1 de 3 · Fundamentos</span>', unsafe_allow_html=True)
        st.markdown('<span class="dot-blue"></span><b>Objetivo:</b> reconocer la dirección de los cambios de CO₂, H⁺, HCO₃⁻ y pH.', unsafe_allow_html=True)

        ejercicio(
            "1. Un paciente hipoventila y elimina menos CO₂. ¿Qué cambio se espera inicialmente?",
            ["Aumento de H⁺ y descenso del pH","Disminución de H⁺ y aumento del pH","Aumento aislado de HCO₃⁻ sin cambio de pH","Disminución de PCO₂"],
            "Aumento de H⁺ y descenso del pH",
            "Al retener CO₂, la reacción se desplaza hacia la formación de H₂CO₃ y H⁺. El aumento de H⁺ reduce el pH.",
            "t1_1"
        )
        ejercicio(
            "2. Si aumenta la ventilación alveolar, ¿qué ocurre con el CO₂ y el pH?",
            ["Disminuye CO₂ y aumenta pH","Aumenta CO₂ y disminuye pH","Aumenta CO₂ y aumenta pH","No cambia ninguno"],
            "Disminuye CO₂ y aumenta pH",
            "Al eliminar más CO₂, disminuye la formación de H⁺ y el pH se eleva.",
            "t1_2"
        )
        ejercicio(
            "3. Una disminución primaria de HCO₃⁻ produce principalmente:",
            ["Tendencia a acidosis metabólica","Tendencia a alcalosis metabólica","Tendencia a alcalosis respiratoria","Tendencia a acidosis respiratoria"],
            "Tendencia a acidosis metabólica",
            "El HCO₃⁻ es el componente básico principal del sistema bicarbonato. Al disminuir, se reduce la capacidad amortiguadora y el pH tiende a bajar.",
            "t1_3"
        )
        ejercicio(
            "4. Un aumento primario de PCO₂ corresponde a una alteración de origen:",
            ["Respiratorio","Metabólico","Renal exclusivamente","Electrolítico exclusivamente"],
            "Respiratorio",
            "Los trastornos primarios de PCO₂ son respiratorios porque dependen de la eliminación pulmonar de CO₂.",
            "t1_4"
        )
        ejercicio(
            "5. ¿Qué órgano compensa principalmente una alteración respiratoria sostenida?",
            ["Riñón","Pulmón","Hígado","Bazo"],
            "Riñón",
            "El riñón modifica la excreción de H⁺ y la reabsorción de HCO₃⁻ para compensar alteraciones respiratorias.",
            "t1_5"
        )

    with tanda2:
        st.markdown('<span class="round-badge round-2">Tanda 2 de 3 · Aplicación</span>', unsafe_allow_html=True)
        st.markdown('<span class="dot-green"></span><b>Objetivo:</b> identificar el trastorno primario a partir de pH, PCO₂ y HCO₃⁻.', unsafe_allow_html=True)

        ejercicio(
            "1. pH 7,28 · PCO₂ 55 mmHg · HCO₃⁻ 24 mEq/L. ¿Cuál es la alteración primaria?",
            ["Acidosis respiratoria","Acidosis metabólica","Alcalosis respiratoria","Alcalosis metabólica"],
            "Acidosis respiratoria",
            "El pH está bajo y la PCO₂ está elevada, mientras el HCO₃⁻ permanece en rango. El cambio primario es respiratorio y acidificante.",
            "t2_1"
        )
        ejercicio(
            "2. pH 7,50 · PCO₂ 30 mmHg · HCO₃⁻ 24 mEq/L. ¿Cuál es la alteración primaria?",
            ["Alcalosis respiratoria","Acidosis respiratoria","Alcalosis metabólica","Acidosis metabólica"],
            "Alcalosis respiratoria",
            "El pH está elevado y la PCO₂ está baja. La pérdida excesiva de CO₂ disminuye H⁺ y eleva el pH.",
            "t2_2"
        )
        ejercicio(
            "3. pH 7,30 · PCO₂ 40 mmHg · HCO₃⁻ 18 mEq/L. ¿Cuál es la alteración primaria?",
            ["Acidosis metabólica","Acidosis respiratoria","Alcalosis metabólica","Alcalosis respiratoria"],
            "Acidosis metabólica",
            "El pH está bajo y el HCO₃⁻ está disminuido, mientras la PCO₂ está en rango. El trastorno primario es metabólico.",
            "t2_3"
        )
        ejercicio(
            "4. pH 7,49 · PCO₂ 40 mmHg · HCO₃⁻ 31 mEq/L. ¿Cuál es la alteración primaria?",
            ["Alcalosis metabólica","Alcalosis respiratoria","Acidosis metabólica","Acidosis respiratoria"],
            "Alcalosis metabólica",
            "El pH está elevado y el HCO₃⁻ está aumentado, con PCO₂ en rango. El cambio primario es metabólico y alcalinizante.",
            "t2_4"
        )
        ejercicio(
            "5. En una acidosis metabólica, ¿qué respuesta respiratoria compensatoria se espera?",
            ["Aumento de ventilación para disminuir CO₂","Disminución de ventilación para aumentar CO₂","Aumento de HCO₃⁻ pulmonar","Reducción de excreción de H⁺"],
            "Aumento de ventilación para disminuir CO₂",
            "La hiperventilación elimina CO₂, reduce H⁺ y ayuda a desplazar el pH en dirección normal.",
            "t2_5"
        )

    with tanda3:
        st.markdown('<span class="round-badge round-3">Tanda 3 de 3 · Clínica</span>', unsafe_allow_html=True)
        st.markdown('<span class="dot-orange"></span><b>Objetivo:</b> relacionar el contexto clínico con el mecanismo ácido-base.', unsafe_allow_html=True)

        ejercicio(
            "1. Paciente con depresión del centro respiratorio presenta hipoventilación. ¿Qué alteración ácido-base es más probable?",
            ["Acidosis respiratoria","Alcalosis respiratoria","Acidosis metabólica","Alcalosis metabólica"],
            "Acidosis respiratoria",
            "La hipoventilación reduce la eliminación de CO₂. Este se acumula, aumenta H⁺ y disminuye el pH.",
            "t3_1"
        )
        ejercicio(
            "2. Paciente con hiperventilación marcada por ansiedad elimina CO₂ en exceso. ¿Qué alteración es más probable?",
            ["Alcalosis respiratoria","Acidosis respiratoria","Alcalosis metabólica","Acidosis metabólica"],
            "Alcalosis respiratoria",
            "La hiperventilación disminuye la PCO₂, reduce la concentración de H⁺ y eleva el pH.",
            "t3_2"
        )
        ejercicio(
            "3. Paciente con pérdida importante de bicarbonato presenta pH 7,29 y HCO₃⁻ 17 mEq/L. ¿Qué trastorno predomina?",
            ["Acidosis metabólica","Acidosis respiratoria","Alcalosis respiratoria","Alcalosis metabólica"],
            "Acidosis metabólica",
            "La pérdida de HCO₃⁻ reduce el componente básico del sistema amortiguador y desplaza el equilibrio hacia un pH más bajo.",
            "t3_3"
        )
        ejercicio(
            "4. Paciente con acidosis respiratoria sostenida desarrolla aumento de HCO₃⁻. ¿Cómo se interpreta ese cambio?",
            ["Compensación renal","Empeoramiento metabólico obligatorio","Alcalosis respiratoria asociada","Pérdida renal de base"],
            "Compensación renal",
            "Ante un trastorno respiratorio, el riñón puede aumentar la excreción de H⁺ y conservar/reabsorber HCO₃⁻ para acercar el pH a la normalidad.",
            "t3_4"
        )
        ejercicio(
            "5. Paciente con pH 7,36, PCO₂ 55 mmHg y HCO₃⁻ elevado. ¿Qué interpretación general es más adecuada?",
            ["Trastorno respiratorio con respuesta compensatoria renal","Gasometría completamente normal","Alcalosis respiratoria aislada","Acidosis metabólica sin compensación"],
            "Trastorno respiratorio con respuesta compensatoria renal",
            "La PCO₂ elevada ejerce un efecto acidificante y el HCO₃⁻ elevado actúa en sentido compensatorio. El pH cercano al rango normal sugiere compensación.",
            "t3_5"
        )

st.divider()
st.caption("Creado por Cristian Barahona Videla · Uso educativo · © 2026")
