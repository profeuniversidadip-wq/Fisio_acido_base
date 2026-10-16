
import streamlit as st

st.set_page_config(
    page_title="FisioÁcidoBase IA",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.block-container {padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1150px;}
html, body, [class*="css"] {font-size: 17px;}
.main-title {font-size: 2rem; font-weight: 800; margin-bottom: .25rem;}
.subtitle {font-size: 1.02rem; opacity:.82; margin-bottom: 1rem;}
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
    border-radius:16px;
    padding:16px 18px;
    margin:.65rem 0;
    border:1px solid rgba(80,110,140,.22);
}
.status-normal {background:#E8F5E9; border-left:7px solid #2E7D32;}
.status-acid {background:#FFEBEE; border-left:7px solid #C62828;}
.status-alk {background:#E3F2FD; border-left:7px solid #1565C0;}
.status-warn {background:#FFF8E1; border-left:7px solid #F9A825;}
.big-state {font-size:1.25rem; font-weight:800; margin-bottom:.25rem;}
.flow-box {
    text-align:center;
    font-size:1.05rem;
    font-weight:700;
    padding:12px 10px;
    border-radius:12px;
    background:rgba(255,255,255,.72);
    border:1px solid rgba(80,110,140,.20);
    margin-top:.55rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Equilibrio ácido-base: comprender antes de memorizar</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aplicación interactiva para Fisiología y Fisiopatología · Kinesiología</div>', unsafe_allow_html=True)

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
    st.caption("Mueve los faders y observa cómo cambia la tendencia ácido-base. Los rangos son educativos y se interpretan con los valores de referencia del material.")

    st.markdown("### Variables principales")

    c1, c2 = st.columns(2)

    with c1:
        ventilacion = st.slider(
            "Ventilación alveolar relativa (%)",
            min_value=25,
            max_value=200,
            value=100,
            step=5,
            help="100% representa una ventilación de referencia. No equivale a un valor clínico medido."
        )
        pco2 = st.slider(
            "PCO₂ (mmHg)",
            min_value=20,
            max_value=70,
            value=40,
            step=1
        )

    with c2:
        hco3 = st.slider(
            "HCO₃⁻ (mEq/L)",
            min_value=10,
            max_value=40,
            value=24,
            step=1
        )
        excrecion_h = st.slider(
            "Excreción renal relativa de H⁺ (%)",
            min_value=25,
            max_value=200,
            value=100,
            step=5,
            help="100% representa una condición de referencia. Es un control conceptual, no una medición clínica directa."
        )

    # Interpretación independiente de cada variable.
    if pco2 > 45:
        resp = "Tendencia respiratoria acidificante"
        resp_cls = "status-acid"
        resp_chain = "↑ PCO₂ → ↑ H₂CO₃ → ↑ H⁺ → ↓ pH"
    elif pco2 < 35:
        resp = "Tendencia respiratoria alcalinizante"
        resp_cls = "status-alk"
        resp_chain = "↓ PCO₂ → ↓ H⁺ → ↑ pH"
    else:
        resp = "Componente respiratorio en rango"
        resp_cls = "status-normal"
        resp_chain = "PCO₂ entre 35–45 mmHg"

    if hco3 < 22:
        met = "Tendencia metabólica acidificante"
        met_cls = "status-acid"
        met_chain = "↓ HCO₃⁻ → menor capacidad amortiguadora → tendencia a ↓ pH"
    elif hco3 > 26:
        met = "Tendencia metabólica alcalinizante"
        met_cls = "status-alk"
        met_chain = "↑ HCO₃⁻ → mayor componente básico → tendencia a ↑ pH"
    else:
        met = "Componente metabólico en rango"
        met_cls = "status-normal"
        met_chain = "HCO₃⁻ entre 22–26 mEq/L"

    if ventilacion < 80:
        vent_txt = "Hipoventilación relativa"
        vent_cls = "status-acid"
        vent_chain = "↓ ventilación → ↓ eliminación de CO₂ → tendencia a ↑ PCO₂ → ↓ pH"
    elif ventilacion > 120:
        vent_txt = "Hiperventilación relativa"
        vent_cls = "status-alk"
        vent_chain = "↑ ventilación → ↑ eliminación de CO₂ → tendencia a ↓ PCO₂ → ↑ pH"
    else:
        vent_txt = "Ventilación cercana a referencia"
        vent_cls = "status-normal"
        vent_chain = "La ventilación no sugiere un desplazamiento importante por sí sola"

    if excrecion_h < 80:
        renal_txt = "Menor eliminación renal de H⁺"
        renal_cls = "status-acid"
        renal_chain = "↓ excreción de H⁺ → retención relativa de ácido → tendencia a ↓ pH"
    elif excrecion_h > 120:
        renal_txt = "Mayor eliminación renal de H⁺"
        renal_cls = "status-alk"
        renal_chain = "↑ excreción de H⁺ → menor carga ácida → apoyo a ↑ pH"
    else:
        renal_txt = "Excreción renal cercana a referencia"
        renal_cls = "status-normal"
        renal_chain = "Sin desplazamiento renal marcado en el simulador"

    st.markdown("### Lectura inmediata")
    r1, r2 = st.columns(2)
    with r1:
        st.markdown(
            f'<div class="status-card {resp_cls}"><div class="big-state">{resp}</div>'
            f'<div>{resp_chain}</div></div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="status-card {vent_cls}"><div class="big-state">{vent_txt}</div>'
            f'<div>{vent_chain}</div></div>',
            unsafe_allow_html=True
        )
    with r2:
        st.markdown(
            f'<div class="status-card {met_cls}"><div class="big-state">{met}</div>'
            f'<div>{met_chain}</div></div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="status-card {renal_cls}"><div class="big-state">{renal_txt}</div>'
            f'<div>{renal_chain}</div></div>',
            unsafe_allow_html=True
        )

    # Resumen global cualitativo.
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

    st.markdown("### Estado integrado del simulador")

    if acid_score == 0 and alk_score == 0:
        global_txt = "Equilibrio cercano a condición de referencia"
        global_cls = "status-normal"
        global_msg = "Las variables principales se mantienen en rangos de referencia del simulador."
    elif acid_score > alk_score:
        global_txt = "Predominio de fuerzas acidificantes"
        global_cls = "status-acid"
        global_msg = "Las variables seleccionadas favorecen un aumento relativo de H⁺ y una tendencia a disminuir el pH."
    elif alk_score > acid_score:
        global_txt = "Predominio de fuerzas alcalinizantes"
        global_cls = "status-alk"
        global_msg = "Las variables seleccionadas favorecen una disminución relativa de H⁺ y una tendencia a elevar el pH."
    else:
        global_txt = "Fuerzas opuestas: posible compensación o trastorno mixto"
        global_cls = "status-warn"
        global_msg = "Hay variables acidificantes y alcalinizantes simultáneamente. Se debe interpretar el pH, la PCO₂ y el HCO₃⁻ en conjunto."

    st.markdown(
        f'<div class="status-card {global_cls}"><div class="big-state">{global_txt}</div>'
        f'<div>{global_msg}</div>'
        f'<div class="flow-box">CO₂ + H₂O ⇄ H₂CO₃ ⇄ H⁺ + HCO₃⁻</div></div>',
        unsafe_allow_html=True
    )

    st.caption("Nota: el simulador muestra relaciones fisiológicas cualitativas. No calcula compensaciones esperadas ni reemplaza la interpretación clínica completa.")

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
    st.subheader("Práctica razonada")
    casos = [
        {
            "caso":"Paciente con hipoventilación retiene CO₂. ¿Qué cambio inicial esperas?",
            "opciones":["Aumento de H⁺ y descenso del pH","Descenso de H⁺ y aumento del pH","Aumento de HCO₃⁻ por compensación respiratoria inmediata","Sin cambio en el pH"],
            "correcta":"Aumento de H⁺ y descenso del pH",
            "exp":"Retener CO₂ desplaza la reacción hacia la formación de H⁺."
        },
        {
            "caso":"Un paciente hiperventila y elimina más CO₂. ¿Qué ocurre con el pH?",
            "opciones":["Aumenta","Disminuye","Permanece necesariamente en 7,40","Depende solo del riñón"],
            "correcta":"Aumenta",
            "exp":"Al eliminar más CO₂ disminuye H⁺ y el pH se eleva."
        },
        {
            "caso":"pH 7,28; PCO₂ 55 mmHg; HCO₃⁻ 24 mEq/L. ¿Qué componente explica mejor el descenso del pH?",
            "opciones":["Aumento de PCO₂","Disminución de PCO₂","Aumento de HCO₃⁻","HCO₃⁻ bajo"],
            "correcta":"Aumento de PCO₂",
            "exp":"La PCO₂ está elevada y el HCO₃⁻ permanece dentro del intervalo de referencia usado."
        },
        {
            "caso":"pH 7,50; PCO₂ 40 mmHg; HCO₃⁻ 31 mEq/L. ¿Qué componente explica mejor el aumento del pH?",
            "opciones":["Aumento de HCO₃⁻","Aumento de PCO₂","Disminución de HCO₃⁻","PCO₂ baja"],
            "correcta":"Aumento de HCO₃⁻",
            "exp":"El bicarbonato está elevado mientras la PCO₂ se encuentra dentro del intervalo de referencia."
        },
    ]

    for i, c in enumerate(casos,1):
        with st.expander(f"Caso {i}", expanded=(i==1)):
            st.write(c["caso"])
            r = st.radio("Selecciona", c["opciones"], key=f"caso_{i}", index=None)
            if st.button("Revisar", key=f"rev_{i}"):
                if r is None:
                    st.warning("Selecciona una alternativa.")
                elif r == c["correcta"]:
                    st.success("Correcto.")
                    st.write(c["exp"])
                else:
                    st.error("Aún no.")
                    st.write(c["exp"])

st.divider()
st.caption("Creado por Cristian Barahona Videla · Uso educativo · © 2026")
