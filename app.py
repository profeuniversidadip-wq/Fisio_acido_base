
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
    st.subheader("Simulador cualitativo")
    st.caption("Mueve una variable y predice primero qué debería ocurrir con H⁺ y el pH.")

    var = st.radio(
        "¿Qué quieres modificar?",
        ["Ventilación", "PCO₂", "HCO₃⁻", "Excreción renal de H⁺"],
        horizontal=True
    )

    if var == "Ventilación":
        estado = st.select_slider("Ventilación", options=["Disminuida", "Normal", "Aumentada"], value="Normal")
        if estado == "Disminuida":
            st.markdown("**Cadena:** ↓ ventilación → ↓ eliminación de CO₂ → ↑ CO₂ → ↑ H⁺ → ↓ pH")
            st.error("Tendencia acidificante de origen respiratorio.")
        elif estado == "Aumentada":
            st.markdown("**Cadena:** ↑ ventilación → ↑ eliminación de CO₂ → ↓ CO₂ → ↓ H⁺ → ↑ pH")
            st.success("Tendencia alcalinizante de origen respiratorio.")
        else:
            st.info("Sin cambio primario respiratorio simulado.")

    elif var == "PCO₂":
        estado = st.select_slider("PCO₂", options=["Baja", "Normal", "Alta"], value="Normal")
        if estado == "Alta":
            st.markdown("**Cadena:** ↑ CO₂ → reacción hacia H⁺ + HCO₃⁻ → ↑ H⁺ → ↓ pH")
            st.error("Compatible con tendencia a acidosis respiratoria.")
        elif estado == "Baja":
            st.markdown("**Cadena:** ↓ CO₂ → ↓ H⁺ → ↑ pH")
            st.success("Compatible con tendencia a alcalosis respiratoria.")
        else:
            st.info("PCO₂ dentro del intervalo de referencia usado en el material.")

    elif var == "HCO₃⁻":
        estado = st.select_slider("HCO₃⁻", options=["Bajo", "Normal", "Alto"], value="Normal")
        if estado == "Bajo":
            st.markdown("**Interpretación:** hay menor base disponible para amortiguar H⁺.")
            st.error("Compatible con tendencia a acidosis metabólica.")
        elif estado == "Alto":
            st.markdown("**Interpretación:** aumenta el componente básico del sistema bicarbonato.")
            st.success("Compatible con tendencia a alcalosis metabólica.")
        else:
            st.info("HCO₃⁻ dentro del intervalo de referencia usado en el material.")

    else:
        estado = st.select_slider("Excreción renal de H⁺", options=["Disminuida", "Normal", "Aumentada"], value="Normal")
        if estado == "Disminuida":
            st.markdown("**Cadena:** ↓ excreción de H⁺ → retención relativa de ácido → ↓ pH")
            st.error("Tendencia acidificante.")
        elif estado == "Aumentada":
            st.markdown("**Cadena:** ↑ excreción de H⁺ + conservación de HCO₃⁻ → apoyo a recuperación del pH")
            st.success("Respuesta renal que favorece una menor carga ácida.")
        else:
            st.info("Sin modificación renal simulada.")

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
