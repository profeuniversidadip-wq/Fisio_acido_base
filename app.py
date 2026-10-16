
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
    height:7px;
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



/* Navegación principal estilo archivador */
.stTabs [data-baseweb="tab-list"]{
    gap:.28rem !important;
    background:transparent !important;
    padding:.2rem 0 0 0 !important;
    border-bottom:2px solid rgba(80,100,120,.18) !important;
    align-items:flex-end !important;
}
.stTabs [data-baseweb="tab"]{
    position:relative !important;
    border-radius:12px 12px 0 0 !important;
    border:1px solid rgba(50,70,90,.22) !important;
    border-bottom:none !important;
    padding:.58rem .95rem .52rem !important;
    min-height:44px !important;
    font-weight:800 !important;
    color:#18324a !important;
    transition:transform .15s ease, box-shadow .15s ease, filter .15s ease !important;
    top:2px !important;
}
.stTabs [data-baseweb="tab"]:nth-child(1){
    background:#90CAF9 !important;
}
.stTabs [data-baseweb="tab"]:nth-child(2){
    background:#B39DDB !important;
}
.stTabs [data-baseweb="tab"]:nth-child(3){
    background:#A5D6A7 !important;
}
.stTabs [data-baseweb="tab"]:nth-child(4){
    background:#FFCC80 !important;
}
.stTabs [data-baseweb="tab"]::before{
    content:"" !important;
    position:absolute !important;
    top:-7px !important;
    left:10px !important;
    width:42% !important;
    height:8px !important;
    border-radius:7px 7px 0 0 !important;
    background:inherit !important;
    border:1px solid rgba(50,70,90,.20) !important;
    border-bottom:none !important;
}
.stTabs [aria-selected="true"]{
    top:0 !important;
    filter:saturate(1.1) brightness(1.02) !important;
    box-shadow:0 -2px 8px rgba(0,0,0,.10) !important;
    border-width:2px !important;
    z-index:2 !important;
}
.stTabs [aria-selected="true"]:nth-child(1){
    border-color:#1976D2 !important;
    color:#0D47A1 !important;
}
.stTabs [aria-selected="true"]:nth-child(2){
    border-color:#5E35B1 !important;
    color:#311B92 !important;
}
.stTabs [aria-selected="true"]:nth-child(3){
    border-color:#388E3C !important;
    color:#1B5E20 !important;
}
.stTabs [aria-selected="true"]:nth-child(4){
    border-color:#F57C00 !important;
    color:#E65100 !important;
}
.stTabs [data-baseweb="tab-highlight"]{
    display:none !important;
}
@media (hover:hover) and (pointer:fine){
    .stTabs [data-baseweb="tab"]:hover{
        transform:translateY(-2px) !important;
        box-shadow:0 -2px 6px rgba(0,0,0,.08) !important;
    }
}
@media (max-width:760px){
    .stTabs [data-baseweb="tab-list"]{
        display:grid !important;
        grid-template-columns:repeat(2,minmax(0,1fr)) !important;
        gap:.4rem .35rem !important;
        border-bottom:none !important;
        padding-top:.3rem !important;
    }
    .stTabs [data-baseweb="tab"]{
        width:100% !important;
        justify-content:center !important;
        border-radius:12px !important;
        border:1px solid rgba(50,70,90,.22) !important;
        top:0 !important;
        padding:.58rem .5rem !important;
        font-size:.92rem !important;
        text-align:center !important;
        white-space:normal !important;
    }
    .stTabs [data-baseweb="tab"]::before{
        display:none !important;
    }
    .stTabs [aria-selected="true"]{
        border-width:2px !important;
        box-shadow:0 2px 8px rgba(0,0,0,.10) !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Equilibrio ácido-base</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Comprender antes de memorizar · Fisiología y Fisiopatología · Kinesiología</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Fundamentos", "Simulador", "Gasometría", "Práctica"])

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
    st.caption("Faders verticales táctiles. Arrastra directamente el control con el dedo o mouse.")

    mixer_html = """
    <style>
      *{box-sizing:border-box;}
      .ab-wrap{
        font-family:Arial,Helvetica,sans-serif;
        border:1px solid #d8e0e8;
        border-radius:18px;
        padding:10px;
        background:linear-gradient(180deg,#f8fbff 0%,#eef5fb 100%);
        user-select:none;
        -webkit-user-select:none;
      }
      .ab-grid{
        display:grid;
        grid-template-columns:repeat(4,minmax(78px,1fr));
        gap:8px;
      }
      .ab-channel{
        background:#14202b;
        border-radius:13px;
        padding:8px 6px 9px;
        text-align:center;
        color:white;
        min-width:0;
      }
      .ab-label{
        font-size:12px;
        font-weight:700;
        line-height:1.1;
        min-height:27px;
        display:flex;
        align-items:center;
        justify-content:center;
      }
      .ab-value{
        font-size:13px;
        font-weight:800;
        margin:3px 0 5px;
      }
      .fader-area{
        height:138px;
        display:flex;
        align-items:center;
        justify-content:center;
        touch-action:none;
      }
      .vtrack{
        position:relative;
        width:18px;
        height:122px;
        border-radius:999px;
        background:linear-gradient(to top,#4b5563,#9ca3af);
        box-shadow:inset 0 0 0 1px rgba(255,255,255,.08);
        touch-action:none;
      }
      .vhandle{
        position:absolute;
        left:50%;
        width:34px;
        height:18px;
        transform:translate(-50%,50%);
        border-radius:5px;
        background:#f8fafc;
        border:2px solid #0f172a;
        box-shadow:0 2px 5px rgba(0,0,0,.35);
        cursor:grab;
        touch-action:none;
      }
      .vhandle:active{cursor:grabbing;}
      .scale{
        display:flex;
        justify-content:space-between;
        font-size:9px;
        color:#cbd5e1;
        margin:1px 2px 0;
      }
      .mini-status{
        margin-top:5px;
        border-radius:9px;
        padding:5px 6px;
        font-size:10px;
        font-weight:700;
        line-height:1.15;
        min-height:29px;
        display:flex;
        align-items:center;
        justify-content:center;
      }
      .mini-normal{background:#e8f5e9;color:#1b5e20;}
      .mini-acid{background:#ffebee;color:#b71c1c;}
      .mini-alk{background:#e3f2fd;color:#0d47a1;}
      .mini-warn{background:#fff8e1;color:#8d6e00;}
      .summary{
        margin-top:8px;
        border-radius:11px;
        padding:6px 9px;
        border:1px solid rgba(80,110,140,.20);
        font-size:11px;
        font-weight:700;
      }
      .summary .title{font-size:13px;font-weight:800;margin-bottom:1px;}
      .sum-normal{background:#e8f5e9;color:#1b5e20;}
      .sum-acid{background:#ffebee;color:#b71c1c;}
      .sum-alk{background:#e3f2fd;color:#0d47a1;}
      .sum-warn{background:#fff8e1;color:#8d6e00;}
      .details{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:6px;
        margin-top:7px;
      }
      .detail-card{
        border-radius:9px;
        padding:5px 7px;
        font-size:10px;
        line-height:1.15;
        border:1px solid rgba(80,110,140,.14);
      }
      .equation{
        text-align:center;
        font-weight:800;
        font-size:11px;
        margin-top:7px;
        padding:6px;
        border-radius:9px;
        background:#fff;
        border:1px solid rgba(80,110,140,.15);
      }
      .note{
        text-align:center;
        font-size:9px;
        color:#475569;
        margin-top:5px;
      }
      .blue{color:#60a5fa;}
      .pink{color:#fb7185;}
      .green{color:#4ade80;}
      .orange{color:#fbbf24;}

      @media(max-width:700px){
        .ab-grid{
          grid-template-columns:repeat(2,minmax(0,1fr));
          gap:7px;
        }
        .fader-area{height:118px;}
        .vtrack{height:102px;width:16px;}
        .vhandle{width:31px;height:17px;}
        .ab-channel{padding:7px 5px 8px;}
        .ab-label{font-size:11px;min-height:25px;}
        .ab-value{font-size:12px;}
        .mini-status{font-size:9px;min-height:26px;padding:4px 5px;}
        .details{grid-template-columns:1fr;}
      }
    </style>

    <div class="ab-wrap">
      <div class="ab-grid">

        <div class="ab-channel">
          <div class="ab-label">Ventilación</div>
          <div id="ventVal" class="ab-value blue">100%</div>
          <div class="fader-area">
            <div id="ventTrack" class="vtrack" data-min="25" data-max="200" data-step="5" data-value="100">
              <div class="vhandle"></div>
            </div>
          </div>
          <div class="scale"><span>25</span><span>100</span><span>200</span></div>
          <div id="ventStatus" class="mini-status mini-normal">Referencia</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">PCO₂</div>
          <div id="pco2Val" class="ab-value pink">40 mmHg</div>
          <div class="fader-area">
            <div id="pco2Track" class="vtrack" data-min="20" data-max="70" data-step="1" data-value="40">
              <div class="vhandle"></div>
            </div>
          </div>
          <div class="scale"><span>20</span><span>45</span><span>70</span></div>
          <div id="pco2Status" class="mini-status mini-normal">En rango</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">HCO₃⁻</div>
          <div id="hco3Val" class="ab-value green">24 mEq/L</div>
          <div class="fader-area">
            <div id="hco3Track" class="vtrack" data-min="10" data-max="40" data-step="1" data-value="24">
              <div class="vhandle"></div>
            </div>
          </div>
          <div class="scale"><span>10</span><span>24</span><span>40</span></div>
          <div id="hco3Status" class="mini-status mini-normal">En rango</div>
        </div>

        <div class="ab-channel">
          <div class="ab-label">Excreción renal H⁺</div>
          <div id="renalVal" class="ab-value orange">100%</div>
          <div class="fader-area">
            <div id="renalTrack" class="vtrack" data-min="25" data-max="200" data-step="5" data-value="100">
              <div class="vhandle"></div>
            </div>
          </div>
          <div class="scale"><span>25</span><span>100</span><span>200</span></div>
          <div id="renalStatus" class="mini-status mini-normal">Referencia</div>
        </div>

      </div>

      <div id="summary" class="summary sum-normal">
        <div class="title">Condición cercana a referencia</div>
        <div id="summaryText">Sin predominio acidificante ni alcalinizante.</div>
      </div>

      <div class="details">
        <div id="d1" class="detail-card" style="background:#fff;">PCO₂ en rango · 35–45 mmHg</div>
        <div id="d2" class="detail-card" style="background:#fff;">HCO₃⁻ en rango · 22–26 mEq/L</div>
        <div id="d3" class="detail-card" style="background:#fff;">Ventilación cercana a referencia</div>
        <div id="d4" class="detail-card" style="background:#fff;">Excreción renal cercana a referencia</div>
      </div>

      <div class="equation">CO₂ + H₂O ⇄ H₂CO₃ ⇄ H⁺ + HCO₃⁻</div>
      <div class="note">Arrastra el fader vertical. En celular se bloquea el desplazamiento de la página mientras lo mueves.</div>
    </div>

    <script>
      const tracks = {
        vent: document.getElementById('ventTrack'),
        pco2: document.getElementById('pco2Track'),
        hco3: document.getElementById('hco3Track'),
        renal: document.getElementById('renalTrack')
      };

      function clamp(v,min,max){ return Math.max(min,Math.min(max,v)); }

      function getCfg(track){
        return {
          min:Number(track.dataset.min),
          max:Number(track.dataset.max),
          step:Number(track.dataset.step),
          value:Number(track.dataset.value)
        };
      }

      function setValue(track, raw){
        const c=getCfg(track);
        let v=clamp(raw,c.min,c.max);
        v=Math.round((v-c.min)/c.step)*c.step+c.min;
        v=clamp(v,c.min,c.max);
        track.dataset.value=String(v);
        positionHandle(track);
        updateMixer();
      }

      function positionHandle(track){
        const c=getCfg(track);
        const pct=(c.value-c.min)/(c.max-c.min);
        const handle=track.querySelector('.vhandle');
        handle.style.bottom=(pct*100)+'%';
      }

      function valueFromPointer(track, clientY){
        const c=getCfg(track);
        const rect=track.getBoundingClientRect();
        const y=clamp(clientY-rect.top,0,rect.height);
        const pct=1-(y/rect.height);
        return c.min+pct*(c.max-c.min);
      }

      function attachFader(track){
        let active=false;

        const start=(e)=>{
          active=true;
          track.setPointerCapture?.(e.pointerId);
          e.preventDefault();
          setValue(track,valueFromPointer(track,e.clientY));
        };

        const move=(e)=>{
          if(!active) return;
          e.preventDefault();
          setValue(track,valueFromPointer(track,e.clientY));
        };

        const end=(e)=>{
          if(!active) return;
          active=false;
          e.preventDefault();
          try{ track.releasePointerCapture?.(e.pointerId); }catch(_){}
        };

        track.addEventListener('pointerdown',start,{passive:false});
        track.addEventListener('pointermove',move,{passive:false});
        track.addEventListener('pointerup',end,{passive:false});
        track.addEventListener('pointercancel',end,{passive:false});
      }

      function setStatus(id,text,cls){
        const el=document.getElementById(id);
        el.className='mini-status '+cls;
        el.textContent=text;
      }

      function setDetail(id,text,bg){
        const el=document.getElementById(id);
        el.textContent=text;
        el.style.background=bg;
      }

      function updateMixer(){
        const v=Number(tracks.vent.dataset.value);
        const p=Number(tracks.pco2.dataset.value);
        const h=Number(tracks.hco3.dataset.value);
        const r=Number(tracks.renal.dataset.value);

        document.getElementById('ventVal').textContent=v+'%';
        document.getElementById('pco2Val').textContent=p+' mmHg';
        document.getElementById('hco3Val').textContent=h+' mEq/L';
        document.getElementById('renalVal').textContent=r+'%';

        let acid=0, alk=0;

        if(p>45){ acid+=2; setStatus('pco2Status','Alta','mini-acid'); setDetail('d1','PCO₂ alta → ↑ CO₂ → ↑ H⁺ → ↓ pH','#ffebee');}
        else if(p<35){ alk+=2; setStatus('pco2Status','Baja','mini-alk'); setDetail('d1','PCO₂ baja → ↓ CO₂ → ↓ H⁺ → ↑ pH','#e3f2fd');}
        else{ setStatus('pco2Status','En rango','mini-normal'); setDetail('d1','PCO₂ en rango · 35–45 mmHg','#fff');}

        if(h<22){ acid+=2; setStatus('hco3Status','Bajo','mini-acid'); setDetail('d2','HCO₃⁻ bajo → menor base → ↓ pH','#ffebee');}
        else if(h>26){ alk+=2; setStatus('hco3Status','Alto','mini-alk'); setDetail('d2','HCO₃⁻ alto → mayor base → ↑ pH','#e3f2fd');}
        else{ setStatus('hco3Status','En rango','mini-normal'); setDetail('d2','HCO₃⁻ en rango · 22–26 mEq/L','#fff');}

        if(v<80){ acid+=1; setStatus('ventStatus','Hipoventilación','mini-acid'); setDetail('d3','↓ ventilación → ↑ CO₂ → ↓ pH','#ffebee');}
        else if(v>120){ alk+=1; setStatus('ventStatus','Hiperventilación','mini-alk'); setDetail('d3','↑ ventilación → ↓ CO₂ → ↑ pH','#e3f2fd');}
        else{ setStatus('ventStatus','Referencia','mini-normal'); setDetail('d3','Ventilación cercana a referencia','#fff');}

        if(r<80){ acid+=1; setStatus('renalStatus','Menor excreción','mini-acid'); setDetail('d4','↓ excreción H⁺ → retención relativa de ácido','#ffebee');}
        else if(r>120){ alk+=1; setStatus('renalStatus','Mayor excreción','mini-alk'); setDetail('d4','↑ excreción H⁺ → menor carga ácida','#e3f2fd');}
        else{ setStatus('renalStatus','Referencia','mini-normal'); setDetail('d4','Excreción renal cercana a referencia','#fff');}

        const s=document.getElementById('summary');
        const st=s.querySelector('.title');
        const txt=document.getElementById('summaryText');

        if(acid===0 && alk===0){
          s.className='summary sum-normal';
          st.textContent='Condición cercana a referencia';
          txt.textContent='Sin predominio acidificante ni alcalinizante.';
        }else if(acid>alk){
          s.className='summary sum-acid';
          st.textContent='Predominio acidificante';
          txt.textContent='Las variables favorecen ↑ H⁺ y tendencia a ↓ pH.';
        }else if(alk>acid){
          s.className='summary sum-alk';
          st.textContent='Predominio alcalinizante';
          txt.textContent='Las variables favorecen ↓ H⁺ y tendencia a ↑ pH.';
        }else{
          s.className='summary sum-warn';
          st.textContent='Fuerzas opuestas';
          txt.textContent='Puede existir compensación o un patrón mixto.';
        }
      }

      Object.values(tracks).forEach(t=>{
        positionHandle(t);
        attachFader(t);
      });
      updateMixer();
    </script>
    """

    components.html(mixer_html, height=510, scrolling=False)

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
