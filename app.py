
import streamlit as st
import streamlit.components.v1 as components

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

.nav-card {
    border-radius: 14px;
    padding: 10px 14px;
    font-weight: 800;
    text-align: center;
    border: 1px solid rgba(80,110,140,.22);
    margin-bottom: .4rem;
}
.nav-blue {background:#E3F2FD;}
.nav-green {background:#E8F5E9;}
.nav-orange {background:#FFF3E0;}
.nav-purple {background:#F3E5F5;}
.fader-panel-note {
    font-size:.9rem;
    opacity:.8;
    margin-top:.25rem;
}

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
    st.caption("Panel interactivo tipo mesa de sonido. Los propios faders son móviles; no necesitas controles debajo.")

    mixer_html = """
    <style>
      .ab-wrap{
        font-family: Arial, Helvetica, sans-serif;
        border:1px solid #d8e0e8;
        border-radius:18px;
        padding:14px 14px 10px;
        background:linear-gradient(180deg,#f8fbff 0%, #eef5fb 100%);
      }
      .ab-grid{
        display:grid;
        grid-template-columns:repeat(4, minmax(95px,1fr));
        gap:12px;
        align-items:start;
      }
      .ab-channel{
        background:#14202b;
        border-radius:16px;
        padding:10px 8px 12px;
        text-align:center;
        color:white;
        box-shadow:0 3px 10px rgba(0,0,0,.12);
      }
      .ab-label{
        font-size:13px;
        font-weight:700;
        line-height:1.15;
        min-height:30px;
        margin-bottom:4px;
      }
      .ab-value{
        font-size:15px;
        font-weight:800;
        margin-bottom:8px;
      }
      .slider-box{
        height:200px;
        display:flex;
        align-items:center;
        justify-content:center;
        margin:0 auto 6px;
      }
      input[type=range].vslider{
        -webkit-appearance:none;
        appearance:none;
        width:180px;
        height:14px;
        transform:rotate(-90deg);
        background:transparent;
      }
      input[type=range].vslider::-webkit-slider-runnable-track{
        height:10px;
        border-radius:999px;
        background:linear-gradient(90deg,#4b5563 0%, #9ca3af 100%);
      }
      input[type=range].vslider::-webkit-slider-thumb{
        -webkit-appearance:none;
        appearance:none;
        width:18px;
        height:30px;
        border-radius:6px;
        background:#f8fafc;
        border:2px solid #111827;
        margin-top:-10px;
        box-shadow:0 2px 4px rgba(0,0,0,.28);
        cursor:pointer;
      }
      input[type=range].vslider::-moz-range-track{
        height:10px;
        border-radius:999px;
        background:linear-gradient(90deg,#4b5563 0%, #9ca3af 100%);
      }
      input[type=range].vslider::-moz-range-thumb{
        width:18px;
        height:30px;
        border-radius:6px;
        background:#f8fafc;
        border:2px solid #111827;
        box-shadow:0 2px 4px rgba(0,0,0,.28);
        cursor:pointer;
      }
      .scale{
        display:flex;
        justify-content:space-between;
        color:#cbd5e1;
        font-size:10px;
        margin-top:-3px;
      }
      .mini-status{
        margin-top:8px;
        border-radius:10px;
        padding:6px 8px;
        font-size:11px;
        font-weight:700;
        line-height:1.2;
        min-height:34px;
      }
      .mini-normal{background:#e8f5e9;color:#1b5e20;}
      .mini-acid{background:#ffebee;color:#b71c1c;}
      .mini-alk{background:#e3f2fd;color:#0d47a1;}
      .mini-warn{background:#fff8e1;color:#8d6e00;}

      .summary{
        margin-top:10px;
        border-radius:12px;
        padding:8px 11px;
        border:1px solid rgba(80,110,140,.20);
        font-size:13px;
        font-weight:700;
      }
      .summary .title{
        font-size:15px;
        font-weight:800;
        margin-bottom:2px;
      }
      .sum-normal{background:#e8f5e9;color:#1b5e20;}
      .sum-acid{background:#ffebee;color:#b71c1c;}
      .sum-alk{background:#e3f2fd;color:#0d47a1;}
      .sum-warn{background:#fff8e1;color:#8d6e00;}

      .details{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:8px;
        margin-top:10px;
      }
      .detail-card{
        border-radius:10px;
        padding:7px 9px;
        font-size:12px;
        line-height:1.2;
        border:1px solid rgba(80,110,140,.14);
      }
      .equation{
        text-align:center;
        font-weight:800;
        font-size:14px;
        margin-top:10px;
        padding:8px;
        border-radius:10px;
        background:#ffffff;
        border:1px solid rgba(80,110,140,.15);
      }
      .note{
        text-align:center;
        font-size:11px;
        color:#475569;
        margin-top:6px;
      }
      .blue{color:#60a5fa;}
      .pink{color:#fb7185;}
      .green{color:#4ade80;}
      .orange{color:#fbbf24;}

      @media(max-width:700px){
        .ab-grid{grid-template-columns:repeat(2,minmax(120px,1fr));}
        .slider-box{height:165px;}
        input[type=range].vslider{width:145px;}
        .details{grid-template-columns:1fr;}
      }
    </style>

    <div class="ab-wrap">
      <div class="ab-grid">
        <div class="ab-channel">
          <div class="ab-label">Ventilación</div>
          <div id="ventVal" class="ab-value blue">100%</div>
          <div class="slider-box">
            <input id="vent" class="vslider" type="range" min="25" max="200" step="5" value="100">
          </div>
          <div class="scale"><span>25</span><span>100</span><span>200</span></div>
          <div id="ventStatus" class="mini-status mini-normal">Cercana a referencia</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">PCO₂</div>
          <div id="pco2Val" class="ab-value pink">40 mmHg</div>
          <div class="slider-box">
            <input id="pco2" class="vslider" type="range" min="20" max="70" step="1" value="40">
          </div>
          <div class="scale"><span>20</span><span>45</span><span>70</span></div>
          <div id="pco2Status" class="mini-status mini-normal">En rango</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">HCO₃⁻</div>
          <div id="hco3Val" class="ab-value green">24 mEq/L</div>
          <div class="slider-box">
            <input id="hco3" class="vslider" type="range" min="10" max="40" step="1" value="24">
          </div>
          <div class="scale"><span>10</span><span>24</span><span>40</span></div>
          <div id="hco3Status" class="mini-status mini-normal">En rango</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">Excreción renal H⁺</div>
          <div id="renalVal" class="ab-value orange">100%</div>
          <div class="slider-box">
            <input id="renal" class="vslider" type="range" min="25" max="200" step="5" value="100">
          </div>
          <div class="scale"><span>25</span><span>100</span><span>200</span></div>
          <div id="renalStatus" class="mini-status mini-normal">Cercana a referencia</div>
        </div>
      </div>

      <div id="summary" class="summary sum-normal">
        <div class="title">Condición cercana a referencia</div>
        <div id="summaryText">Sin predominio acidificante ni alcalinizante.</div>
      </div>

      <div class="details">
        <div id="leftDetail1" class="detail-card" style="background:#ffffff;">PCO₂ en rango · 35–45 mmHg</div>
        <div id="rightDetail1" class="detail-card" style="background:#ffffff;">HCO₃⁻ en rango · 22–26 mEq/L</div>
        <div id="leftDetail2" class="detail-card" style="background:#ffffff;">Ventilación cercana a referencia</div>
        <div id="rightDetail2" class="detail-card" style="background:#ffffff;">Excreción renal cercana a referencia</div>
      </div>

      <div class="equation">CO₂ + H₂O ⇄ H₂CO₃ ⇄ H⁺ + HCO₃⁻</div>
      <div class="note">Simulación cualitativa educativa. No calcula compensaciones esperadas cuantitativamente.</div>
    </div>

    <script>
      const vent = document.getElementById('vent');
      const pco2 = document.getElementById('pco2');
      const hco3 = document.getElementById('hco3');
      const renal = document.getElementById('renal');

      const setBox = (el, text, cls) => {
        el.className = 'mini-status ' + cls;
        el.textContent = text;
      };
      const setDetail = (id, text, bg) => {
        const el = document.getElementById(id);
        el.textContent = text;
        el.style.background = bg;
      };

      function updateMixer(){
        const v = Number(vent.value);
        const p = Number(pco2.value);
        const h = Number(hco3.value);
        const r = Number(renal.value);

        document.getElementById('ventVal').textContent = v + '%';
        document.getElementById('pco2Val').textContent = p + ' mmHg';
        document.getElementById('hco3Val').textContent = h + ' mEq/L';
        document.getElementById('renalVal').textContent = r + '%';

        let acidScore = 0;
        let alkScore = 0;

        // PCO2
        if (p > 45){
          acidScore += 2;
          setBox(document.getElementById('pco2Status'), 'Alta', 'mini-acid');
          setDetail('leftDetail1', 'PCO₂ alta → ↑ CO₂ → ↑ H⁺ → ↓ pH', '#ffebee');
        } else if (p < 35){
          alkScore += 2;
          setBox(document.getElementById('pco2Status'), 'Baja', 'mini-alk');
          setDetail('leftDetail1', 'PCO₂ baja → ↓ CO₂ → ↓ H⁺ → ↑ pH', '#e3f2fd');
        } else {
          setBox(document.getElementById('pco2Status'), 'En rango', 'mini-normal');
          setDetail('leftDetail1', 'PCO₂ en rango · 35–45 mmHg', '#ffffff');
        }

        // HCO3
        if (h < 22){
          acidScore += 2;
          setBox(document.getElementById('hco3Status'), 'Bajo', 'mini-acid');
          setDetail('rightDetail1', 'HCO₃⁻ bajo → menor base → tendencia a ↓ pH', '#ffebee');
        } else if (h > 26){
          alkScore += 2;
          setBox(document.getElementById('hco3Status'), 'Alto', 'mini-alk');
          setDetail('rightDetail1', 'HCO₃⁻ alto → mayor base → tendencia a ↑ pH', '#e3f2fd');
        } else {
          setBox(document.getElementById('hco3Status'), 'En rango', 'mini-normal');
          setDetail('rightDetail1', 'HCO₃⁻ en rango · 22–26 mEq/L', '#ffffff');
        }

        // Ventilation
        if (v < 80){
          acidScore += 1;
          setBox(document.getElementById('ventStatus'), 'Hipoventilación', 'mini-acid');
          setDetail('leftDetail2', '↓ ventilación → ↓ eliminación de CO₂ → ↓ pH', '#ffebee');
        } else if (v > 120){
          alkScore += 1;
          setBox(document.getElementById('ventStatus'), 'Hiperventilación', 'mini-alk');
          setDetail('leftDetail2', '↑ ventilación → ↑ eliminación de CO₂ → ↑ pH', '#e3f2fd');
        } else {
          setBox(document.getElementById('ventStatus'), 'Cercana a referencia', 'mini-normal');
          setDetail('leftDetail2', 'Ventilación cercana a referencia', '#ffffff');
        }

        // Renal H+
        if (r < 80){
          acidScore += 1;
          setBox(document.getElementById('renalStatus'), 'Menor excreción', 'mini-acid');
          setDetail('rightDetail2', '↓ excreción renal de H⁺ → retención relativa de ácido', '#ffebee');
        } else if (r > 120){
          alkScore += 1;
          setBox(document.getElementById('renalStatus'), 'Mayor excreción', 'mini-alk');
          setDetail('rightDetail2', '↑ excreción renal de H⁺ → menor carga ácida', '#e3f2fd');
        } else {
          setBox(document.getElementById('renalStatus'), 'Cercana a referencia', 'mini-normal');
          setDetail('rightDetail2', 'Excreción renal cercana a referencia', '#ffffff');
        }

        const sum = document.getElementById('summary');
        const sumText = document.getElementById('summaryText');

        if (acidScore === 0 && alkScore === 0){
          sum.className = 'summary sum-normal';
          sum.querySelector('.title').textContent = 'Condición cercana a referencia';
          sumText.textContent = 'Sin predominio acidificante ni alcalinizante.';
        } else if (acidScore > alkScore){
          sum.className = 'summary sum-acid';
          sum.querySelector('.title').textContent = 'Predominio acidificante';
          sumText.textContent = 'Las variables favorecen ↑ H⁺ y tendencia a ↓ pH.';
        } else if (alkScore > acidScore){
          sum.className = 'summary sum-alk';
          sum.querySelector('.title').textContent = 'Predominio alcalinizante';
          sumText.textContent = 'Las variables favorecen ↓ H⁺ y tendencia a ↑ pH.';
        } else {
          sum.className = 'summary sum-warn';
          sum.querySelector('.title').textContent = 'Fuerzas opuestas';
          sumText.textContent = 'Puede existir compensación o un patrón mixto; integra pH, PCO₂ y HCO₃⁻.';
        }
      }

      [vent,pco2,hco3,renal].forEach(el => el.addEventListener('input', updateMixer));
      updateMixer();
    </script>
    """
    components.html(mixer_html, height=560, scrolling=False)

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
