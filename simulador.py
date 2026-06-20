import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d0f14 !important;
    color: #e8e8e6;
    font-family: 'Inter', sans-serif;
}
[data-testid="stSidebar"] { background-color: #0b0d12 !important; border-right: 1px solid #1f2330; }
[data-testid="stSidebar"] * { color: #c8c5c0 !important; }
[data-testid="stTabs"] [data-baseweb="tab-list"] { background: #10131a; border-bottom: 1px solid #1f2330; }
[data-testid="stTabs"] [data-baseweb="tab"] { background: transparent; color: #6a6a66 !important; font-size: 0.82rem; }
[data-testid="stTabs"] [aria-selected="true"] { color: #e05c2a !important; border-bottom: 2px solid #e05c2a !important; background: transparent !important; }
[data-testid="stTabs"] [data-baseweb="tab-panel"] { background: #0d0f14; padding-top: 1.5rem; }
[data-testid="metric-container"] { background: #10131a; border: 1px solid #1f2330; border-radius: 12px; padding: 1rem 1.2rem; }
[data-testid="metric-container"] label { color: #6a6a66 !important; font-size: 0.78rem !important; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #e05c2a !important; font-family: 'Space Grotesk', sans-serif !important; }
h1, h2, h3 { color: #f0ede8 !important; font-family: 'Space Grotesk', sans-serif !important; }
.hero { padding: 2rem 0 1.8rem 0; border-bottom: 1px solid #1f2330; margin-bottom: 2rem; }
.hero-label { font-size: 0.68rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: #e05c2a; margin-bottom: 0.7rem; }
.hero-title { font-family: 'Space Grotesk', sans-serif; font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 700; line-height: 1.1; color: #f0ede8; margin: 0 0 0.8rem 0; }
.hero-title span { color: #e05c2a; }
.hero-desc { font-size: 0.9rem; color: #7a7a76; max-width: 640px; line-height: 1.65; }
</style>
""", unsafe_allow_html=True)

# ── Datos ────────────────────────────────────────────────────────────────────
@st.cache_data
def inicializar_sistema():
    df_c = pd.read_csv("Biobio_comunas.csv")
    df_c['comuna'] = df_c['Comuna'].str.strip()
    df_c['latitud_decimal'] = df_c['Latitud (Decimal)']
    df_c['longitud_decimal'] = df_c['Longitud (decimal)']
    df_c['poblacion_2017'] = df_c['Población Año 2017'].astype(str).str.replace(',', '').str.replace('.', '').astype(float).astype(int)

    df_b = pd.read_csv("bosques_chile_excel.csv", sep=';')
    df_b['Región'] = df_b['Región'].str.strip()

    def limpiar(val):
        if pd.isna(val): return 0.0
        return float(str(val).strip().replace('.', '').replace(',', '.'))

    row = df_b[df_b['Región'] == 'Biobío'].iloc[0]
    veg = {
        "plantacion_forestal_ha": limpiar(row['Plantación Forestal']),
        "bosque_nativo_ha":       limpiar(row['Bosque Nativo']),
        "bosque_mixto_ha":        limpiar(row['Bosque Mixto']),
        "humedales_ha":           10172.8,
        "bosques_total_ha":       limpiar(row['Total']),
        "superficie_total_ha":    2399067.7
    }
    return df_c, veg

try:
    df_comunas, datos_biobio = inicializar_sistema()
except Exception as e:
    st.error(f"❌ Error cargando datos: {e}")
    st.stop()

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-label">SIC 2026 · Grupo 5 · Región del Biobío</div>
  <h1 class="hero-title">🚨 Sistema Integrado de<br><span>Gestión de Crisis</span></h1>
  <p class="hero-desc">Centro de Operaciones de Emergencia — simulación de propagación territorial en tiempo real.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.header("📍 Foco del Incendio")
comuna_origen = st.sidebar.selectbox("Comuna de origen", sorted(df_comunas['comuna'].unique()))
st.sidebar.markdown("---")
st.sidebar.header("🧭 Variables Atmosféricas")
dir_viento  = st.sidebar.selectbox("Dirección del viento", ["Norte","Sur","Este","Oeste","Omnidireccional (Sin control)"])
viento      = st.sidebar.slider("💨 Velocidad del Viento (km/h)", 5, 110, 35)
temperatura = st.sidebar.slider("🌡️ Temperatura (°C)", 15, 45, 34)
humedad     = st.sidebar.slider("💧 Humedad Relativa (%)", 5, 95, 18)
pendiente   = st.sidebar.slider("⛰️ Pendiente media (%)", 0, 50, 12)
horas_ev    = st.sidebar.slider("⏳ Ventana de Simulación (Horas)", 1, 12, 4)

# ── Algoritmo ─────────────────────────────────────────────────────────────────
combustible = (
    (datos_biobio["plantacion_forestal_ha"] * 1.0) +
    (datos_biobio["bosque_mixto_ha"]        * 0.8) +
    (datos_biobio["bosque_nativo_ha"]       * 0.6)
) / datos_biobio["bosques_total_ha"] * 100

sequedad       = 100 - humedad
ip             = min(max((0.30*viento)+(0.30*combustible)+(0.20*temperatura)+(0.10*sequedad)+(0.10*pendiente), 0), 100)
velocidad_fuego = 0.5 + (ip/100*4.0) + (viento/100*3.0)
alcance_km     = velocidad_fuego * horas_ev

origen_fila = df_comunas[df_comunas['comuna'] == comuna_origen].iloc[0]
lat_o, lon_o = origen_fila['latitud_decimal'], origen_fila['longitud_decimal']

df_comunas['distancia_foco_km'] = np.sqrt(
    (df_comunas['latitud_decimal']  - lat_o)**2 +
    (df_comunas['longitud_decimal'] - lon_o)**2
) * 111.12
df_comunas['dif_lat'] = df_comunas['latitud_decimal']  - lat_o
df_comunas['dif_lon'] = df_comunas['longitud_decimal'] - lon_o

def evaluar_trayectoria(row):
    if row['comuna'] == comuna_origen: return True
    if dir_viento == "Norte" and row['dif_lat'] > 0: return True
    if dir_viento == "Sur"   and row['dif_lat'] < 0: return True
    if dir_viento == "Este"  and row['dif_lon'] > 0: return True
    if dir_viento == "Oeste" and row['dif_lon'] < 0: return True
    if dir_viento == "Omnidireccional (Sin control)": return True
    return False

df_comunas['En_Trayectoria'] = df_comunas.apply(evaluar_trayectoria, axis=1)

def calcular_prob(row):
    if row['comuna'] == comuna_origen: return 100.0, "🔴 Extremo (Foco)"
    if row['distancia_foco_km'] <= alcance_km and row['En_Trayectoria']:
        prob = min(max(100-(row['distancia_foco_km']/alcance_km)*100, 0), 100)
    else:
        prob = 0.0
    if prob >= 75: return float(prob), "🔴 Extremo"
    elif prob >= 50: return float(prob), "🟠 Alto"
    elif prob >= 25: return float(prob), "🟡 Medio"
    else: return float(prob), "🟢 Bajo"

res = df_comunas.apply(calcular_prob, axis=1)
df_comunas['Probabilidad (%)']    = [round(r[0],1) for r in res]
df_comunas['Clasificacion_Riesgo'] = [r[1] for r in res]

afectadas         = df_comunas[df_comunas['Probabilidad (%)'] >= 25]
poblacion_afectada = afectadas['poblacion_2017'].sum()
viviendas_afectadas = poblacion_afectada / 3.2

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_mapa, tab_tabla, tab_csv, tab_prev = st.tabs([
    "🗺️ Mapa de Crisis",
    "📊 Propagación por Comuna",
    "💾 Descargar CSV",
    "🌲 Prevención"
])

with tab_mapa:
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Índice de Gravedad (IP)", f"{ip:.1f} %")
    with m2: st.metric("Velocidad de Avance",     f"{velocidad_fuego:.2f} km/h")
    with m3: st.metric("Población en Riesgo",     f"{poblacion_afectada:,.0f} hab")
    with m4: st.metric("Viviendas en Riesgo",     f"{viviendas_afectadas:,.0f} casas")

    st.markdown("---")
    col_mapa, col_graf = st.columns([2, 1])

    with col_mapa:
        st.subheader("🗺️ Mapeo de Amenaza Territorial")
        fig = px.scatter_mapbox(
            df_comunas, lat="latitud_decimal", lon="longitud_decimal",
            color="Clasificacion_Riesgo", size="poblacion_2017",
            color_discrete_map={
                "🔴 Extremo (Foco)":"#FF0000","🔴 Extremo":"#D32F2F",
                "🟠 Alto":"#F57C00","🟡 Medio":"#FBC02D","🟢 Bajo":"#388E3C"
            },
            category_orders={"Clasificacion_Riesgo":["🔴 Extremo (Foco)","🔴 Extremo","🟠 Alto","🟡 Medio","🟢 Bajo"]},
            hover_name="comuna",
            hover_data={"Clasificacion_Riesgo":True,"distancia_foco_km":":.2f Km","Probabilidad (%)":True},
            zoom=7.5, center=dict(lat=lat_o, lon=lon_o),
            mapbox_style="open-street-map", height=480
        )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
            legend=dict(title_text="Riesgo SENAPRED", y=0.99, x=0.01, bgcolor="rgba(20,20,30,0.85)"),
            paper_bgcolor="#0d0f14", plot_bgcolor="#0d0f14")
        st.plotly_chart(fig, use_container_width=True)

    with col_graf:
        st.subheader("🌲 Cobertura Forestal")
        df_veg = pd.DataFrame({
            'Tipo': ['Plantación Forestal','Bosque Nativo','Bosque Mixto','Humedales'],
            'Hectáreas': [datos_biobio["plantacion_forestal_ha"], datos_biobio["bosque_nativo_ha"],
                          datos_biobio["bosque_mixto_ha"], datos_biobio["humedales_ha"]]
        })
        fig_bar = px.bar(df_veg, x='Hectáreas', y='Tipo', orientation='h',
            color='Tipo', color_discrete_sequence=['#A12312','#345922','#6E8131','#417392'],
            text='Hectáreas', height=480)
        fig_bar.update_traces(texttemplate='%{text:,.0f} ha', textposition='outside')
        fig_bar.update_layout(showlegend=False, paper_bgcolor="#0d0f14", plot_bgcolor="#0d0f14",
            xaxis=dict(color="#6a6a66"), yaxis=dict(color="#9a9a95"), margin={"r":40,"t":10,"l":10,"b":10})
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.subheader("🏃 Rutas de Evacuación")
        peligrosas = df_comunas[df_comunas['Probabilidad (%)'] >= 50]
        if not peligrosas.empty:
            for com in peligrosas['comuna'].unique():
                ruta = "Eje Vial Ruta 160 Sur" if dir_viento == "Norte" else "Eje Vial Ruta 5 Sur / Autopista del Itata"
                st.markdown(f"* **{com}:** Evacuar vía **{ruta}**")
        else:
            st.success("✓ Todos los accesos se encuentran estables.")
    with col_der:
        st.subheader("🚨 Contactos de Emergencia")
        st.table(pd.DataFrame({"Organismo":["CONAF","Bomberos","SAMU","Carabineros"],"Línea":["130","132","131","133"]}))

with tab_tabla:
    st.subheader("📊 Tabla Comparativa de Impacto Territorial")
    df_tabla = df_comunas[['comuna','Provincia','poblacion_2017','distancia_foco_km','Probabilidad (%)','Clasificacion_Riesgo']].sort_values(by='Probabilidad (%)', ascending=False)
    df_tabla.columns = ['Comuna','Provincia','Población','Distancia al Foco (km)','Probabilidad (%)','Nivel de Riesgo']
    st.dataframe(df_tabla, use_container_width=True, hide_index=True)

with tab_csv:
    st.subheader("💾 Exportar Reporte Técnico")
    csv_data = df_tabla.to_csv(index=False, sep=';').encode('utf-8-sig')
    st.download_button("📥 Descargar CSV para Excel", data=csv_data,
        file_name=f"simulacion_{comuna_origen}.csv", mime="text/csv")

with tab_prev:
    st.subheader("🌲 Medidas Preventivas Comunitarias")
    p1, p2 = st.columns(2)
    with p1:
        st.markdown("""
#### 🏡 Alrededor del Hogar
* **Combustible:** Limpia techos y canaletas de hojas y ramas secas.
* **Cortafuegos:** Mantén el pasto corto en un radio mínimo de 10 m.
* **Podas:** Elimina ramas bajas hasta 2 m de altura para evitar incendios de copa.
""")
    with p2:
        st.markdown("""
#### 🚜 En Actividades Rurales
* **Quemas:** Prohibidas durante toda la época de altas temperaturas.
* **Recreación:** No hagas fogatas cerca de vegetación seca.
* **Denuncia:** Avisa de inmediato a **CONAF (130)** o **Bomberos (132)**.
""")
