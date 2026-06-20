import streamlit as st

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d0f14;
    color: #e8e8e6;
    font-family: 'Inter', sans-serif;
}
[data-testid="stAppViewContainer"] > .main > div {
    padding: 1.5rem 2.5rem 4rem 2.5rem;
    max-width: 1100px;
    margin: 0 auto;
}


/* ── HERO ── */
.hero {
    padding: 2rem 0 1.8rem 0;
    border-bottom: 1px solid #1f2330;
    margin-bottom: 2rem;
}
.hero-label {
    font-size: 0.68rem; font-weight: 600; letter-spacing: 0.18em;
    text-transform: uppercase; color: #e05c2a; margin-bottom: 0.7rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 700; line-height: 1.1; color: #f0ede8; margin: 0 0 0.8rem 0;
}
.hero-title span { color: #e05c2a; }
.hero-desc { font-size: 0.9rem; color: #7a7a76; max-width: 640px; line-height: 1.65; }

/* ── SECCIÓN ── */
.sec-label {
    font-size: 0.65rem; font-weight: 600; letter-spacing: 0.16em;
    text-transform: uppercase; color: #e05c2a; margin-bottom: 0.4rem;
}
.sec-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.25rem; font-weight: 700; color: #f0ede8;
    margin: 0 0 0.3rem 0;
}
.sec-desc { font-size: 0.85rem; color: #6a6a66; line-height: 1.6; margin-bottom: 1.4rem; }

/* ── GRILLA 3 COLUMNAS ── */
.grid3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.9rem;
    margin-bottom: 2rem;
}
.grid2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.9rem;
    margin-bottom: 2rem;
}

/* ── CARD PARÁMETRO (cuadrado/circular visual) ── */
.param-card {
    background: #10131a;
    border: 1px solid #1f2330;
    border-radius: 14px;
    padding: 1.2rem 1.3rem;
    transition: border-color 0.2s;
    display: flex; flex-direction: column; gap: 0.5rem;
}
.param-card:hover { border-color: #e05c2a55; }
.param-icon-wrap {
    width: 42px; height: 42px; border-radius: 10px;
    background: #1a1d28;
    border: 1px solid #262a3a;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem; margin-bottom: 0.2rem;
}
.param-title {
    font-size: 0.88rem; font-weight: 600; color: #d8d5d0;
}
.param-range {
    font-size: 0.72rem; color: #e05c2a; font-weight: 500;
    letter-spacing: 0.04em; text-transform: uppercase;
}
.param-body { font-size: 0.8rem; color: #6a6a66; line-height: 1.55; }

/* ── BARRA DE RIESGO ── */
.risk-bar {
    height: 4px; border-radius: 99px; margin: 0.5rem 0 0.3rem 0;
}
.risk-zones { display: flex; gap: 0.4rem; flex-wrap: wrap; }
.ztag {
    font-size: 0.67rem; padding: 0.2rem 0.5rem;
    border-radius: 99px; font-weight: 600;
}
.z-low  { background:#1a3a1a; color:#6dbf6d; }
.z-mid  { background:#3a2a0a; color:#e09a2a; }
.z-high { background:#3a1010; color:#e04a2a; }

/* ── DIVIDER ── */
.div { border:none; border-top:1px solid #1a1d28; margin:2rem 0; }

/* ── ROTHERMEL ── */
.formula-box {
    background: #0b0e15;
    border: 1px solid #1f2330;
    border-left: 3px solid #e05c2a;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    font-size: 0.85rem;
    margin-bottom: 1.2rem;
}
.formula-eq {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem; color: #f0c080; letter-spacing: 0.04em;
    margin-bottom: 0.7rem;
}
.var-row { display:flex; gap:1.5rem; flex-wrap:wrap; }
.var-item { font-size:0.78rem; color:#7a7a76; line-height:1.5; }
.var-item strong { color:#c8c5c0; }

/* ── PRO/CONTRA ── */
.pro-con { display:grid; grid-template-columns:1fr 1fr; gap:0.9rem; margin-bottom:2rem; }
.pc-card { background:#10131a; border:1px solid #1f2330; border-radius:12px; padding:1rem 1.2rem; }
.pc-head { font-size:0.78rem; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.7rem; }
.pc-head.pro { color:#6dbf6d; }
.pc-head.con { color:#e04a2a; }
.pc-list { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:0.45rem; }
.pc-list li { font-size:0.8rem; color:#7a7a76; line-height:1.5; padding-left:1rem; position:relative; }
.pc-list li::before { position:absolute; left:0; }
.pc-list.pro-list li::before { content:"✓"; color:#6dbf6d; }
.pc-list.con-list li::before { content:"✗"; color:#e04a2a; }

/* ── ALERTAS SENAPRED ── */
.alert-grid { display:flex; flex-direction:column; gap:0.7rem; margin-bottom:2rem; }
.alert-row {
    display:flex; align-items:flex-start; gap:1rem;
    background:#10131a; border:1px solid #1f2330;
    border-radius:10px; padding:0.85rem 1.1rem;
}
.alert-dot { width:12px; height:12px; border-radius:50%; flex-shrink:0; margin-top:4px; }
.alert-level { font-size:0.82rem; font-weight:600; color:#d8d5d0; margin-bottom:0.15rem; }
.alert-tech  { font-size:0.77rem; color:#7a7a76; line-height:1.5; }
.alert-action{ font-size:0.73rem; color:#5a5a56; margin-top:0.2rem; font-style:italic; }

/* ── TETRAEDRO ── */
.tetra-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:0.8rem; margin-bottom:2rem; }
.tetra-card {
    background:#10131a; border:1px solid #1f2330; border-radius:12px;
    padding:1rem; text-align:center;
}
.tetra-icon { font-size:1.6rem; margin-bottom:0.5rem; }
.tetra-name { font-size:0.82rem; font-weight:600; color:#d8d5d0; margin-bottom:0.3rem; }
.tetra-desc { font-size:0.75rem; color:#6a6a66; line-height:1.5; }

/* ── DATOS REGIÓN ── */
.datos-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:0.8rem; margin-bottom:2rem; }
.dato-card {
    background:#10131a; border:1px solid #1f2330; border-radius:12px;
    padding:1rem 1.2rem;
}
.dato-num { font-family:'Space Grotesk',sans-serif; font-size:1.3rem; font-weight:700; color:#e05c2a; }
.dato-label { font-size:0.76rem; color:#6a6a66; margin-top:0.2rem; line-height:1.4; }

/* ── NOTA ── */
.nota { font-size:0.75rem; color:#3a3a36; line-height:1.6; margin-top:2rem;
    padding-top:1.2rem; border-top:1px solid #14171f; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────── HERO ───────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">Simulador Técnico · Región del Biobío</div>
  <h1 class="hero-title">Fundamentos del<br><span>Simulador de Incendios</span></h1>
  <p class="hero-desc">
    Marco científico, parámetros de control, escala de alertas institucionales
    y limitaciones del modelo. Todo lo que necesitas saber antes de simular.
  </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────── DATOS REGIÓN ───────────────
st.markdown('<div class="sec-label">Contexto regional</div><h2 class="sec-title">Biobío en cifras</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="datos-grid">
  <div class="dato-card">
    <div class="dato-num">875.178 ha</div>
    <div class="dato-label">Plantación Forestal — combustible de mayor riesgo por continuidad vertical y horizontal</div>
  </div>
  <div class="dato-card">
    <div class="dato-num">597.572 ha</div>
    <div class="dato-label">Bosque Nativo — ponderación media de combustible</div>
  </div>
  <div class="dato-card">
    <div class="dato-num">51.635 ha</div>
    <div class="dato-label">Bosque Mixto — riesgo intermedio entre nativo y plantación</div>
  </div>
  <div class="dato-card">
    <div class="dato-num">10.172 ha</div>
    <div class="dato-label">Humedales — barrera natural de baja combustibilidad</div>
  </div>
  <div class="dato-card">
    <div class="dato-num">2.399.067 ha</div>
    <div class="dato-label">Superficie total regional bajo análisis</div>
  </div>
  <div class="dato-card">
    <div class="dato-num">33</div>
    <div class="dato-label">Comunas modeladas con coordenadas, población y superficie</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="div">', unsafe_allow_html=True)

# ─────────────────────── PARÁMETROS DEL SIMULADOR ───
st.markdown("""
<div class="sec-label">Parámetros del simulador</div>
<h2 class="sec-title">Las 6 variables de control</h2>
<p class="sec-desc">Cada slider modifica el índice de propagación calculado en tiempo real. Aquí se explica el rol físico de cada uno.</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid3">

  <div class="param-card">
    <div class="param-icon-wrap">💨</div>
    <div class="param-title">Velocidad del viento</div>
    <div class="param-range">Slider · 0 – 120 km/h · Peso 0.30</div>
    <div class="risk-bar" style="background:linear-gradient(to right,#2a5c2a,#e09a2a,#e04a2a)"></div>
    <div class="param-body">Factor cinético principal. Aporta oxígeno, deseca el combustible y genera <em>spotting</em> (brasas transportadas a distancia). Sobre 60 km/h el frente es incontrolable.</div>
    <div class="risk-zones">
      <span class="ztag z-low">0–20 bajo</span>
      <span class="ztag z-mid">20–60 moderado</span>
      <span class="ztag z-high">60+ extremo</span>
    </div>
  </div>

  <div class="param-card">
    <div class="param-icon-wrap">💧</div>
    <div class="param-title">Humedad relativa</div>
    <div class="param-range">Slider · 0 – 100 % · Peso 0.10 (inverso)</div>
    <div class="risk-bar" style="background:linear-gradient(to right,#e04a2a,#e09a2a,#2a5c2a)"></div>
    <div class="param-body">En el modelo se calcula como Sequedad = 100 − HR. Bajo 25 % la vegetación pierde resistencia térmica; bajo 15 % incluso material verde puede arder.</div>
    <div class="risk-zones">
      <span class="ztag z-high">0–25 extremo</span>
      <span class="ztag z-mid">25–50 moderado</span>
      <span class="ztag z-low">50+ bajo</span>
    </div>
  </div>

  <div class="param-card">
    <div class="param-icon-wrap">🌡️</div>
    <div class="param-title">Temperatura ambiente</div>
    <div class="param-range">Slider · 10 – 45 °C · Peso 0.20</div>
    <div class="risk-bar" style="background:linear-gradient(to right,#2a5c2a,#e09a2a,#e04a2a)"></div>
    <div class="param-body">Activa la pirolisis del material vegetal. Por cada 10 °C adicionales, la velocidad de propagación aumenta hasta un 40 %. Sobre 35 °C el riesgo es extremo.</div>
    <div class="risk-zones">
      <span class="ztag z-low">10–22 bajo</span>
      <span class="ztag z-mid">22–35 moderado</span>
      <span class="ztag z-high">35+ extremo</span>
    </div>
  </div>

  <div class="param-card">
    <div class="param-icon-wrap">⛰️</div>
    <div class="param-title">Pendiente del terreno</div>
    <div class="param-range">Slider · 0 – 100 (índice) · Peso 0.10</div>
    <div class="risk-bar" style="background:linear-gradient(to right,#2a5c2a,#e09a2a,#e04a2a)"></div>
    <div class="param-body">Emula el factor Φs de Rothermel. En laderas pronunciadas el fuego asciende hasta 4× más rápido y dificulta el acceso de brigadas terrestres.</div>
    <div class="risk-zones">
      <span class="ztag z-low">0–30 accesible</span>
      <span class="ztag z-mid">30–65 difícil</span>
      <span class="ztag z-high">65+ inaccesible</span>
    </div>
  </div>

  <div class="param-card">
    <div class="param-icon-wrap">⏱️</div>
    <div class="param-title">Tiempo de propagación</div>
    <div class="param-range">Slider · 1 – 72 horas</div>
    <div class="risk-bar" style="background:linear-gradient(to right,#2a5c2a,#e09a2a,#e04a2a)"></div>
    <div class="param-body">Multiplica el alcance: Alcance (km) = Velocidad × Tiempo. Las primeras 6–8 h son la ventana de control. Pasadas 24 h sin contención, el frente entra en fase autónoma.</div>
    <div class="risk-zones">
      <span class="ztag z-low">1–6 h inicial</span>
      <span class="ztag z-mid">6–24 h activo</span>
      <span class="ztag z-high">24+ h masivo</span>
    </div>
  </div>

  <div class="param-card">
    <div class="param-icon-wrap">📍</div>
    <div class="param-title">Comuna de origen</div>
    <div class="param-range">Selector · 33 comunas del Biobío</div>
    <div class="risk-bar" style="background:#1f2330"></div>
    <div class="param-body">Define el epicentro geográfico. El radio de afectación se calcula con distancia Haversine desde el centroide comunal. Zonas costeras como Arauco o Lebu tienen mayor recurrencia histórica.</div>
    <div class="risk-zones">
      <span class="ztag z-mid">Costeras · mayor frecuencia</span>
      <span class="ztag z-high">Andinas · mayor biomasa</span>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="div">', unsafe_allow_html=True)

# ─────────────────────── TETRAEDRO DEL FUEGO ────────
st.markdown("""
<div class="sec-label">Química del fuego</div>
<h2 class="sec-title">El Tetraedro del Fuego</h2>
<p class="sec-desc">Los sliders del simulador emulan los cuatro elementos que sostienen o detienen la combustión.</p>
<div class="tetra-grid">
  <div class="tetra-card">
    <div class="tetra-icon">🌿</div>
    <div class="tetra-name">Combustible</div>
    <div class="tetra-desc">Modulado por la densidad de plantaciones forestales (peso 0.30 en el IP). A mayor continuidad vegetal, mayor propagación.</div>
  </div>
  <div class="tetra-card">
    <div class="tetra-icon">🌡️</div>
    <div class="tetra-name">Calor</div>
    <div class="tetra-desc">Temperatura ambiente. Reduce la humedad interna del material vegetal y acelera la energía de ignición (pyrolisis).</div>
  </div>
  <div class="tetra-card">
    <div class="tetra-icon">💨</div>
    <div class="tetra-name">Oxígeno</div>
    <div class="tetra-desc">Viento. Actúa como comburente cinético que aviva la llama y transporta brasas (spotting), creando focos secundarios.</div>
  </div>
  <div class="tetra-card">
    <div class="tetra-icon">🔗</div>
    <div class="tetra-name">Reacción en cadena</div>
    <div class="tetra-desc">Determinada inversamente por la Humedad Relativa. Sequedad extrema elimina la barrera térmica del agua entre partículas.</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="div">', unsafe_allow_html=True)

# ─────────────────────── ROTHERMEL ──────────────────
st.markdown("""
<div class="sec-label">Base científica</div>
<h2 class="sec-title">Modelo de Rothermel (1972)</h2>
<p class="sec-desc">Ecuación física estándar usada por CONAF y agencias internacionales para calcular la velocidad de avance del frente de fuego.</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="formula-box">
  <div class="formula-eq">R = (I_R × ξ × (1 + Φw + Φs)) / (ρb × ε × Qig)</div>
  <div class="var-row">
    <div class="var-item"><strong>R</strong> velocidad de propagación</div>
    <div class="var-item"><strong>I_R</strong> intensidad de reacción</div>
    <div class="var-item"><strong>ξ</strong> eficiencia de propagación</div>
    <div class="var-item"><strong>Φw</strong> factor viento</div>
    <div class="var-item"><strong>Φs</strong> factor pendiente</div>
    <div class="var-item"><strong>ρb</strong> densidad del combustible</div>
    <div class="var-item"><strong>ε</strong> calentamiento efectivo</div>
    <div class="var-item"><strong>Qig</strong> energía de ignición</div>
  </div>
</div>
""", unsafe_allow_html=True)

# PRO/CONTRA
st.markdown("""
<div class="pro-con">
  <div class="pc-card">
    <div class="pc-head pro">✓ Implementación del simulador</div>
    <ul class="pc-list pro-list">
      <li>Simplificamos los factores físicos en un sistema matricial de pesos ponderados (IP)</li>
      <li>Interfaz interactiva en tiempo real sin parámetros de laboratorio</li>
      <li>Alta legibilidad educativa para usuarios sin formación técnica</li>
      <li>Fácilmente escalable con datos reales de CONAF o estaciones meteorológicas</li>
    </ul>
  </div>
  <div class="pc-card">
    <div class="pc-head con">✗ Limitaciones del modelo</div>
    <ul class="pc-list con-list">
      <li>Rothermel requiere carga molecular del combustible y tamaño microscópico de partículas</li>
      <li>No modela humedad interna del combustible fino muerto ni densidad de empaquetamiento</li>
      <li>La propagación asume forma radial uniforme (no considera corredores de viento locales)</li>
      <li>No incluye capacidad de respuesta ni recursos de contención</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="div">', unsafe_allow_html=True)

# ─────────────────────── ECUACIONES DEL MODELO ──────
st.markdown("""
<div class="sec-label">Algoritmo implementado</div>
<h2 class="sec-title">Ecuaciones del simulador</h2>
<p class="sec-desc">Fórmulas aplicadas en tiempo real para calcular el índice de propagación y el radio de afectación.</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid3">
  <div class="param-card">
    <div class="param-range">A · Factor combustible</div>
    <div class="formula-eq" style="font-size:0.78rem;color:#f0c080;margin:0.5rem 0;">C = (Forest×1.0 + Mixto×0.8 + Nativo×0.6) / Total × 100</div>
    <div class="param-body">Pondera la superficie de cada tipo de cobertura vegetal según su inflamabilidad relativa.</div>
  </div>
  <div class="param-card">
    <div class="param-range">B · Índice de propagación (IP)</div>
    <div class="formula-eq" style="font-size:0.78rem;color:#f0c080;margin:0.5rem 0;">IP = 0.30V + 0.30C + 0.20T + 0.10S + 0.10P</div>
    <div class="param-body">Donde S = Sequedad = 100 − HR. Suma ponderada de los cinco factores ambientales.</div>
  </div>
  <div class="param-card">
    <div class="param-range">C · Velocidad y alcance</div>
    <div class="formula-eq" style="font-size:0.78rem;color:#f0c080;margin:0.5rem 0;">Vel = 0.5 + (IP/100 × 4.0) + (V/100 × 3.0)<br>Alcance = Vel × Tiempo</div>
    <div class="param-body">El alcance en km define el radio del círculo de afectación sobre el mapa.</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="div">', unsafe_allow_html=True)

# ─────────────────────── ALERTAS SENAPRED ───────────
st.markdown("""
<div class="sec-label">Institucionalidad chilena</div>
<h2 class="sec-title">Escala de alertas SENAPRED / CONAF</h2>
<p class="sec-desc">El simulador clasifica localidades con los colores técnicos oficiales de emergencia según probabilidad de afectación calculada.</p>
<div class="alert-grid">
  <div class="alert-row">
    <div class="alert-dot" style="background:#e04a2a"></div>
    <div>
      <div class="alert-level">🔴 75–100% · Alerta Roja (Extremo)</div>
      <div class="alert-tech">Amenaza inminente a vidas, viviendas e infraestructura crítica. Humedad &lt; 20% + viento ≥ 20 km/h activan el "Botón Rojo" de CONAF.</div>
      <div class="alert-action">Acción: evacuación obligatoria, movilización total de brigadas y recursos técnicos.</div>
    </div>
  </div>
  <div class="alert-row">
    <div class="alert-dot" style="background:#e09a2a"></div>
    <div>
      <div class="alert-level">🟠 50–74% · Alerta Amarilla (Alto)</div>
      <div class="alert-tech">El siniestro presenta proyecciones de crecimiento que amenazan con superar la capacidad de control local.</div>
      <div class="alert-action">Acción: alistamiento de recursos adicionales y preparación de apoyo regional.</div>
    </div>
  </div>
  <div class="alert-row">
    <div class="alert-dot" style="background:#e0cc2a"></div>
    <div>
      <div class="alert-level">🟡 25–49% · Alerta Temprana Preventiva (Medio)</div>
      <div class="alert-tech">Estado de anticipación coordinado ante condiciones meteorológicas extremas (viento adverso y calor).</div>
      <div class="alert-action">Acción: refuerzo del monitoreo continuo y patrullajes preventivos.</div>
    </div>
  </div>
  <div class="alert-row">
    <div class="alert-dot" style="background:#4a9a4a"></div>
    <div>
      <div class="alert-level">🟢 0–24% · Alerta Verde (Bajo)</div>
      <div class="alert-tech">Condiciones bajo control técnico o fuera del cono de trayectoria del vector de viento.</div>
      <div class="alert-action">Acción: monitoreo estándar sin intervención activa.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="nota">
  <strong>Nota metodológica:</strong> Simulador educativo de aproximación conceptual basado en el modelo de Rothermel (1972).
  Las probabilidades de afectación se calculan con distancia Haversine entre centroides comunales. No reemplaza
  sistemas operativos como FARSITE ni la información oficial de CONAF/SENAPRED.
  Datos de cobertura vegetal: inventario territorial región del Biobío. Datos de población y superficie: Censo 2017 (INE).
</div>
""", unsafe_allow_html=True)
