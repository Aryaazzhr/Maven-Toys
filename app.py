import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Maven Toys - Business Analytics Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS - Refined Neon Cyberpunk Theme (Improved Readability)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-dark: #060e1a;
    --bg-panel: rgba(10, 22, 48, 0.90);
    --bg-glass: rgba(16, 32, 68, 0.65);
    --bg-card: rgba(12, 26, 56, 0.75);
    --border-glow: rgba(180, 77, 255, 0.30);
    --border-dim: rgba(77, 195, 255, 0.18);
    --border-subtle: rgba(100, 140, 200, 0.12);
    --neon-pink: #ff5cb8;
    --neon-purple: #b84dff;
    --neon-blue: #4dc3ff;
    --neon-green: #3dff6f;
    --neon-orange: #ffaa33;
    --text-primary: #e4ecff;
    --text-secondary: #b0c4e8;
    --text-dim: #7a9abf;
    --text-label: #8faac8;
    --radius-lg: 16px;
    --radius-md: 12px;
    --radius-sm: 8px;
}

/* Hide Streamlit defaults */
#MainMenu, footer, header, .stDeployButton,
div[data-testid="stToolbar"],
div[data-testid="stDecoration"],
div[data-testid="stStatusWidget"] { display: none !important; visibility: hidden !important; }

/* ── Main Background ── */
.stApp, [data-testid="stAppViewContainer"], .main, section[data-testid="stMain"] {
    background: var(--bg-dark) !important;
    background-image:
        radial-gradient(ellipse at 15% 5%, rgba(184,77,255,0.07) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 90%, rgba(77,195,255,0.05) 0%, transparent 55%),
        radial-gradient(ellipse at 50% 50%, rgba(255,92,184,0.03) 0%, transparent 60%) !important;
    font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif !important;
}
.block-container {
    padding-top: 0 !important;
    max-width: 100% !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
}

/* ── Custom Header ── */
.custom-header {
    background: linear-gradient(180deg, rgba(10,22,48,0.95) 0%, rgba(10,22,48,0.88) 100%);
    border-bottom: 1px solid rgba(180,77,255,0.25);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 16px 36px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 40px rgba(184,77,255,0.10), 0 1px 0 rgba(77,195,255,0.08);
    margin: -1rem -2.5rem 0 -2.5rem;
    width: calc(100% + 5rem);
}
.logo-area { display: flex; align-items: center; gap: 16px; }
.logo-icon {
    width: 42px; height: 42px;
    background: linear-gradient(135deg, #b84dff 0%, #ff5cb8 100%);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 900; color: #fff;
    box-shadow: 0 0 24px rgba(184,77,255,0.35), inset 0 1px 0 rgba(255,255,255,0.2);
    letter-spacing: 0.5px;
}
.logo-text {
    font-size: 19px; font-weight: 800; color: var(--text-primary);
    letter-spacing: 0.3px;
    text-shadow: 0 0 20px rgba(184,77,255,0.2);
}
.logo-sub { font-size: 11.5px; color: var(--text-dim); margin-top: 1px; font-weight: 400; }
.header-right { display: flex; align-items: center; gap: 14px; }
.badge-header {
    font-size: 10px; padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.6px;
    font-weight: 600;
}
.badge-pink { background: rgba(255,92,184,0.12); border: 1px solid rgba(255,92,184,0.35); color: var(--neon-pink); }
.badge-blue { background: rgba(77,195,255,0.10); border: 1px solid rgba(77,195,255,0.30); color: var(--neon-blue); }
.live-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--neon-green);
    box-shadow: 0 0 12px var(--neon-green), 0 0 4px var(--neon-green);
    animation: pulse 2.5s ease-in-out infinite;
    display: inline-block;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(0.85)} }

/* ── Tabs ── */
div[data-testid="stTabs"] {
    background: rgba(10,22,48,0.92);
    border-bottom: 1px solid rgba(77,195,255,0.12);
    margin: 0 -2.5rem;
    padding: 0 36px;
    backdrop-filter: blur(12px);
}
div[data-testid="stTabs"] button {
    color: var(--text-dim) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.3px;
    border-bottom: 3px solid transparent !important;
    background: none !important;
    padding: 16px 30px !important;
    transition: all 0.25s ease;
}
div[data-testid="stTabs"] button:hover {
    color: var(--neon-blue) !important;
    background: rgba(77,195,255,0.04) !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: var(--neon-pink) !important;
    border-bottom-color: var(--neon-pink) !important;
    background: rgba(255,92,184,0.06) !important;
    text-shadow: 0 0 12px rgba(255,92,184,0.3);
}

/* ── Filter Area ── */
.filter-container {
    background: rgba(12,26,56,0.6);
    border: 1px solid rgba(77,195,255,0.12);
    border-radius: var(--radius-md);
    padding: 16px 22px;
    margin-bottom: 22px;
    backdrop-filter: blur(8px);
}
.filter-label {
    font-size: 10px; font-weight: 700; color: var(--text-dim);
    letter-spacing: 1.2px; text-transform: uppercase;
    margin-bottom: 8px;
}

/* ── KPI Cards (Enhanced) ── */
.kpi-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 22px 24px 18px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    min-height: 135px;
}
.kpi-card:hover {
    border-color: var(--border-glow);
    box-shadow: 0 8px 32px rgba(184,77,255,0.15), 0 0 0 1px rgba(184,77,255,0.1);
    transform: translateY(-2px);
}
.kpi-glow-bar {
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    border-radius: var(--radius-lg) var(--radius-lg) 0 0;
}
.kpi-glow-pink { background: linear-gradient(90deg, var(--neon-pink), rgba(255,92,184,0.1)); }
.kpi-glow-purple { background: linear-gradient(90deg, var(--neon-purple), rgba(184,77,255,0.1)); }
.kpi-glow-blue { background: linear-gradient(90deg, var(--neon-blue), rgba(77,195,255,0.1)); }
.kpi-glow-green { background: linear-gradient(90deg, var(--neon-green), rgba(61,255,111,0.1)); }
.kpi-icon-bg { display: none !important; }
.kpi-icon-pink { background: rgba(255,92,184,0.10); color: var(--neon-pink); }
.kpi-icon-purple { background: rgba(184,77,255,0.10); color: var(--neon-purple); }
.kpi-icon-blue { background: rgba(77,195,255,0.10); color: var(--neon-blue); }
.kpi-icon-green { background: rgba(61,255,111,0.08); color: var(--neon-green); }
.kpi-label {
    font-size: 10.5px; color: var(--text-dim); font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase;
    margin-bottom: 12px; margin-top: 4px;
}
.kpi-value {
    font-size: 28px; font-weight: 800; line-height: 1;
    margin-bottom: 8px; letter-spacing: -0.5px;
}
.kpi-sub {
    font-size: 11.5px; color: var(--text-dim);
    display: flex; align-items: center; gap: 6px;
}
.kpi-trend-up {
    display: inline-flex; align-items: center; gap: 3px;
    color: var(--neon-green); font-weight: 600; font-size: 11px;
}
.kpi-trend-neutral {
    display: inline-flex; align-items: center; gap: 3px;
    color: var(--text-dim); font-weight: 600; font-size: 11px;
}

/* ── Section Title ── */
.section-title {
    font-size: 11px; font-weight: 700; letter-spacing: 1.8px;
    color: var(--text-dim); text-transform: uppercase;
    margin-bottom: 16px; padding-left: 2px;
    display: flex; align-items: center; gap: 10px;
}
.section-title::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(77,195,255,0.15), transparent);
}

/* ── Chart Card (Enhanced) ── */
.chart-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-lg);
    padding: 24px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    margin-bottom: 18px;
}
.chart-card:hover { border-color: rgba(184,77,255,0.25); }
.chart-header { margin-bottom: 16px; }
.chart-title {
    font-size: 14px; font-weight: 700; color: var(--text-primary);
    margin-bottom: 4px; letter-spacing: 0.1px;
}
.chart-sub {
    font-size: 11.5px; color: var(--text-dim);
    line-height: 1.4;
}

/* ── Page Title ── */
.page-title {
    font-size: 24px; font-weight: 800; color: var(--text-primary);
    margin-bottom: 6px; letter-spacing: -0.3px;
    display: flex; align-items: center; gap: 12px;
}
.page-desc {
    font-size: 13.5px; color: var(--text-dim);
    margin-bottom: 24px; line-height: 1.5;
}
.tag {
    display: inline-block; padding: 3px 12px; border-radius: 10px; font-size: 11px;
    background: rgba(77,195,255,0.08); color: var(--neon-blue);
    border: 1px solid rgba(77,195,255,0.20); font-weight: 600;
    vertical-align: middle;
}

/* ── Insight Boxes (Enhanced) ── */
.insight-box {
    background: var(--bg-card);
    border-radius: var(--radius-md);
    padding: 18px 20px;
    font-size: 12.5px; color: var(--text-secondary); line-height: 1.7;
    border: 1px solid var(--border-subtle);
    transition: all 0.25s ease;
    margin-bottom: 12px;
}
.insight-box:hover { border-color: rgba(184,77,255,0.2); }
.insight-purple { border-left: 4px solid var(--neon-purple); }
.insight-pink { border-left: 4px solid var(--neon-pink); }
.insight-blue { border-left: 4px solid var(--neon-blue); }
.insight-green { border-left: 4px solid var(--neon-green); }
.ins-title {
    font-size: 11.5px; font-weight: 700;
    letter-spacing: 0.8px; text-transform: uppercase;
    margin-bottom: 8px;
    display: flex; align-items: center; gap: 8px;
}
.ins-title::before {
    content: ''; width: 6px; height: 6px; border-radius: 50%;
    display: inline-block;
}
.ins-title-purple { color: var(--neon-purple); }
.ins-title-purple::before { background: var(--neon-purple); box-shadow: 0 0 8px var(--neon-purple); }
.ins-title-pink { color: var(--neon-pink); }
.ins-title-pink::before { background: var(--neon-pink); box-shadow: 0 0 8px var(--neon-pink); }
.ins-title-blue { color: var(--neon-blue); }
.ins-title-blue::before { background: var(--neon-blue); box-shadow: 0 0 8px var(--neon-blue); }
.ins-title-green { color: var(--neon-green); }
.ins-title-green::before { background: var(--neon-green); box-shadow: 0 0 8px var(--neon-green); }
.hl { font-weight: 700; color: var(--text-primary); }

/* ── Tables (Enhanced) ── */
.custom-table { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 13px; }
.custom-table thead tr {
    background: rgba(184,77,255,0.08);
}
.custom-table thead th {
    padding: 14px 18px; text-align: left; font-size: 10.5px; font-weight: 700;
    color: var(--neon-purple); letter-spacing: 1px; text-transform: uppercase;
    white-space: nowrap;
    border-bottom: 2px solid rgba(180,77,255,0.20);
    position: sticky; top: 0;
    background: rgba(12,26,56,0.95);
    backdrop-filter: blur(8px);
}
.custom-table tbody tr {
    border-bottom: 1px solid rgba(77,195,255,0.06);
    transition: all 0.2s ease;
}
.custom-table tbody tr:nth-child(even) { background: rgba(77,195,255,0.02); }
.custom-table tbody tr:hover { background: rgba(184,77,255,0.08); }
.custom-table tbody td {
    padding: 13px 18px; color: var(--text-secondary); vertical-align: middle;
}
.td-name { color: var(--text-primary) !important; font-weight: 600; }
.td-badge {
    display: inline-block; padding: 4px 12px; border-radius: 20px;
    font-size: 10px; font-weight: 700; letter-spacing: 0.4px;
}
.badge-electronics { background: rgba(77,195,255,0.12); color: var(--neon-blue); border: 1px solid rgba(77,195,255,0.25); }
.badge-toys { background: rgba(255,92,184,0.12); color: var(--neon-pink); border: 1px solid rgba(255,92,184,0.25); }
.badge-arts { background: rgba(184,77,255,0.12); color: var(--neon-purple); border: 1px solid rgba(184,77,255,0.25); }
.badge-games { background: rgba(61,255,111,0.08); color: var(--neon-green); border: 1px solid rgba(61,255,111,0.20); }
.badge-sports { background: rgba(255,170,51,0.12); color: var(--neon-orange); border: 1px solid rgba(255,170,51,0.25); }
.bar-mini {
    height: 7px; border-radius: 4px;
    background: linear-gradient(90deg, var(--neon-purple), var(--neon-pink));
    box-shadow: 0 0 8px rgba(255,92,184,0.3);
    transition: width 0.5s ease;
}
.bar-mini-blue {
    height: 7px; border-radius: 4px;
    background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
    box-shadow: 0 0 8px rgba(77,195,255,0.3);
    transition: width 0.5s ease;
}

/* ── Selectbox / Multiselect ── */
div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label {
    color: var(--text-dim) !important; font-size: 11px !important; font-weight: 700 !important;
    letter-spacing: 0.8px; text-transform: uppercase;
}
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stMultiSelect"] > div > div {
    background: var(--bg-card) !important;
    border: 1px solid rgba(77,195,255,0.15) !important;
    border-radius: 10px !important;
    color: var(--text-secondary) !important;
}

/* ── Plotly ── */
.stPlotlyChart { background: transparent !important; }

/* ── General ── */
.stMarkdown, p, span, label { color: var(--text-primary); }
hr { border-color: rgba(77,195,255,0.10) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: rgba(6,14,26,0.5); }
::-webkit-scrollbar-thumb { background: rgba(184,77,255,0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(184,77,255,0.5); }

/* ── Pipeline nodes ── */
.pipe-flow {
    display: flex; align-items: center; justify-content: center;
    gap: 0; flex-wrap: wrap; margin-bottom: 32px; padding: 10px 0;
}
.pipe-node {
    background: var(--bg-card);
    border-radius: var(--radius-md); padding: 18px 22px;
    text-align: center; min-width: 150px;
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1);
    backdrop-filter: blur(8px);
}
.pipe-node:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); }
.pipe-node-extract { border: 1.5px solid rgba(77,195,255,0.35); }
.pipe-node-extract:hover { border-color: var(--neon-blue); box-shadow: 0 0 20px rgba(77,195,255,0.15); }
.pipe-node-transform { border: 1.5px solid rgba(184,77,255,0.35); }
.pipe-node-transform:hover { border-color: var(--neon-purple); box-shadow: 0 0 20px rgba(184,77,255,0.15); }
.pipe-node-load { border: 1.5px solid rgba(61,255,111,0.30); }
.pipe-node-load:hover { border-color: var(--neon-green); box-shadow: 0 0 20px rgba(61,255,111,0.12); }
.pipe-node-analyze { border: 1.5px solid rgba(255,92,184,0.35); }
.pipe-node-analyze:hover { border-color: var(--neon-pink); box-shadow: 0 0 20px rgba(255,92,184,0.15); }
.pipe-label {
    font-size: 9px; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; margin-bottom: 8px;
}
.pipe-label-blue { color: var(--neon-blue); }
.pipe-label-purple { color: var(--neon-purple); }
.pipe-label-green { color: var(--neon-green); }
.pipe-label-pink { color: var(--neon-pink); }
.pipe-icon { display: none !important; }
.pipe-desc { font-size: 11.5px; color: var(--text-secondary); line-height: 1.5; }
.pipe-arrow {
    font-size: 22px; color: var(--text-dim); padding: 0 10px;
    animation: arrowPulse 2s ease-in-out infinite;
}
@keyframes arrowPulse { 0%,100%{opacity:0.35;transform:translateX(0)} 50%{opacity:1;transform:translateX(3px)} }

/* ── Step cards ── */
.step-card {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    padding: 14px 20px;
    margin-bottom: 10px;
    transition: all 0.25s ease;
}
.step-card:hover {
    border-color: rgba(184,77,255,0.2);
    background: rgba(16,34,72,0.7);
}

/* ── Footer ── */
.dashboard-footer {
    text-align: center; padding: 24px 0 16px;
    font-size: 11px; color: var(--text-dim);
    border-top: 1px solid rgba(77,195,255,0.08);
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA LOADING
# ============================================================
@st.cache_data
def load_data():
    sales = pd.read_csv("sales.csv").dropna()
    products = pd.read_csv("products.csv").dropna()
    stores = pd.read_csv("stores.csv").dropna()
    inventory = pd.read_csv("inventory.csv").dropna()
    
    products['Product_Cost'] = products['Product_Cost'].replace(r'[\$,\s]', '', regex=True).astype(float)
    products['Product_Price'] = products['Product_Price'].replace(r'[\$,\s]', '', regex=True).astype(float)
    
    # Build merged sales dataset
    df = sales.merge(products, on='Product_ID', how='left').merge(stores, on='Store_ID', how='left')
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Revenue'] = df['Units'] * df['Product_Price']
    df['Profit'] = df['Units'] * (df['Product_Price'] - df['Product_Cost'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    inv = inventory.merge(products, on='Product_ID').merge(stores, on='Store_ID')
    inv['Inv_Value'] = inv['Stock_On_Hand'] * inv['Product_Cost']
    
    return df, products, stores, inventory, inv

df, products, stores, inventory, inv = load_data()

# ============================================================
# PLOTLY THEME & HELPERS
# ============================================================
NEON = dict(pink='#ff5cb8', purple='#b84dff', blue='#4dc3ff', green='#3dff6f', orange='#ffaa33')

CAT_COLORS = {
    'Art & Crafts': NEON['pink'],
    'Electronics': NEON['purple'],
    'Games': NEON['blue'],
    'Sports & Outdoors': NEON['green'],
    'Toys': NEON['orange'],
}

PLOTLY_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Inter, Segoe UI, sans-serif', color='#b0c4e8', size=11),
    margin=dict(l=50, r=30, t=35, b=50),
)

DEFAULT_AXIS = dict(
    gridcolor='rgba(40,65,110,0.35)',
    gridwidth=1,
    tickfont=dict(color='#7a9abf', size=11),
    zeroline=False,
    linecolor='rgba(77,195,255,0.1)',
    linewidth=1,
)

def apply_layout(fig, height=320, **kwargs):
    xaxis_kw = {**DEFAULT_AXIS, **kwargs.pop('xaxis', {})}
    yaxis_kw = {**DEFAULT_AXIS, **kwargs.pop('yaxis', {})}
    legend_default = dict(font=dict(size=11, color='#b0c4e8'), bgcolor='rgba(0,0,0,0)')
    legend_kw = {**legend_default, **kwargs.pop('legend', {})}
    fig.update_layout(**PLOTLY_LAYOUT, height=height, xaxis=xaxis_kw, yaxis=yaxis_kw, legend=legend_kw, **kwargs)

def fmt(n):
    if n >= 1e6: return f"${n/1e6:.2f}M"
    elif n >= 1e3: return f"${n/1e3:.1f}K"
    else: return f"${n:.0f}"

def hex_rgba(hex_color, alpha=1.0):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{alpha})'

def show_chart(fig, key=None):
    st.plotly_chart(fig, key=key, width='stretch', config={'displayModeBar': False})

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="custom-header">
  <div class="logo-area">
    <div class="logo-icon">MT</div>
    <div>
      <div class="logo-text">Maven Toys Analytics</div>
      <div class="logo-sub">Business Analytics Dashboard &nbsp;·&nbsp; ITS Statistika 2026</div>
    </div>
  </div>
  <div class="header-right">
    <span class="badge-header badge-pink">DIAGNOSTIC ANALYTICS</span>
    <span class="badge-header badge-blue">Case Study 7</span>
    <div class="live-dot"></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs(["  Overview & Profitabilitas", "  Inventory & Stockout", "  Data Pipeline", "  Executive Insights"])

# ============================================================
# TAB 1: OVERVIEW & PROFITABILITAS
# ============================================================
with tab1:
    st.markdown("""
    <div style="margin-top:8px; margin-bottom:24px;">
        <div class="page-title">Sales Performance Overview <span class="tag">2022 – 2023</span></div>
        <div class="page-desc">Descriptive & Diagnostic Analytics — Profitabilitas kategori produk, tren temporal, dan performa toko.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── FILTERS ──
    fc1, fc2, _spacer = st.columns([1, 1, 3])
    with fc1:
        year_filter = st.selectbox("TAHUN", ["Semua", 2022, 2023], key="year_f")
    with fc2:
        loc_filter = st.selectbox("LOKASI", ["Semua", "Downtown", "Commercial", "Airport", "Residential"], key="loc_f")

    dff = df.copy()
    if year_filter != "Semua":
        dff = dff[dff['Year'] == int(year_filter)]
    if loc_filter != "Semua":
        dff = dff[dff['Store_Location'] == loc_filter]

    # ── KPIs ──
    total_rev = dff['Revenue'].sum()
    total_prof = dff['Profit'].sum()
    total_units = int(dff['Units'].sum())
    avg_margin = (total_prof / total_rev * 100) if total_rev > 0 else 0
    avg_ticket = total_rev / len(dff) if len(dff) > 0 else 0

    st.markdown('<div class="section-title">Key Performance Indicators</div>', unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-pink"></div>
        <div class="kpi-icon-bg kpi-icon-pink"></div>
        <div class="kpi-label">Total Revenue</div>
        <div class="kpi-value" style="color:var(--neon-pink);">{fmt(total_rev)}</div>
        <div class="kpi-sub">
            <span class="kpi-trend-up">● Jan 2022 – Sep 2023</span>
        </div></div>''', unsafe_allow_html=True)
    with k2:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-purple"></div>
        <div class="kpi-icon-bg kpi-icon-purple"></div>
        <div class="kpi-label">Total Profit</div>
        <div class="kpi-value" style="color:var(--neon-purple);">{fmt(total_prof)}</div>
        <div class="kpi-sub">
            <span class="kpi-trend-neutral">Gross profit keseluruhan</span>
        </div></div>''', unsafe_allow_html=True)
    with k3:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-blue"></div>
        <div class="kpi-icon-bg kpi-icon-blue"></div>
        <div class="kpi-label">Total Units Terjual</div>
        <div class="kpi-value" style="color:var(--neon-blue);">{total_units:,}</div>
        <div class="kpi-sub">
            <span class="kpi-trend-neutral">Seluruh toko & produk</span>
        </div></div>''', unsafe_allow_html=True)
    with k4:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-green"></div>
        <div class="kpi-icon-bg kpi-icon-green">%</div>
        <div class="kpi-label">Avg. Profit Margin</div>
        <div class="kpi-value" style="color:var(--neon-green);">{avg_margin:.1f}%</div>
        <div class="kpi-sub">
            <span class="kpi-trend-neutral">Rata-rata seluruh transaksi</span>
        </div></div>''', unsafe_allow_html=True)

    st.write("")

    # ── CHART ROW 1: Profit per Category & Margin per Category ──
    cat_data = dff.groupby('Product_Category').agg(
        Revenue=('Revenue','sum'), Profit=('Profit','sum'), Units=('Units','sum')
    ).reset_index()
    cat_data['Margin'] = cat_data['Profit'] / cat_data['Revenue'] * 100
    cat_data = cat_data.sort_values('Profit', ascending=False)

    cr1, cr2 = st.columns(2)

    with cr1:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Profit per Kategori Produk</div>
        <div class="chart-sub">Diagnosa: Kategori mana yang mendorong profit terbesar?</div>
        </div></div>''', unsafe_allow_html=True)

        colors_list = [CAT_COLORS.get(c, NEON['blue']) for c in cat_data['Product_Category']]
        fig = go.Figure(go.Bar(
            x=cat_data['Product_Category'], y=cat_data['Profit'],
            marker=dict(
                color=[hex_rgba(c, 0.78) for c in colors_list],
                line=dict(width=1.5, color=colors_list),
                pattern=dict(shape=""),
            ),
            text=[fmt(v) for v in cat_data['Profit']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=11, family='Inter'),
            hovertemplate='<b>%{x}</b><br>Profit: %{text}<extra></extra>',
        ))
        apply_layout(fig, height=320, showlegend=False, bargap=0.35,
                     yaxis=dict(DEFAULT_AXIS, tickformat='$,.0f'))
        show_chart(fig, key='cat_profit')

    with cr2:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Margin Profit per Kategori (%)</div>
        <div class="chart-sub">Diagnosa: Efisiensi profitabilitas per kategori</div>
        </div></div>''', unsafe_allow_html=True)

        margin_colors = []
        margin_borders = []
        for m in cat_data['Margin']:
            if m >= 40:
                margin_colors.append(hex_rgba(NEON['green'], 0.75))
                margin_borders.append(NEON['green'])
            elif m >= 30:
                margin_colors.append(hex_rgba(NEON['purple'], 0.70))
                margin_borders.append(NEON['purple'])
            else:
                margin_colors.append(hex_rgba(NEON['blue'], 0.55))
                margin_borders.append(NEON['blue'])

        fig2 = go.Figure(go.Bar(
            x=cat_data['Product_Category'], y=cat_data['Margin'],
            marker=dict(color=margin_colors,
                       line=dict(width=1.5, color=margin_borders)),
            text=[f"{v:.1f}%" for v in cat_data['Margin']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=11),
            hovertemplate='<b>%{x}</b><br>Margin: %{y:.1f}%<extra></extra>',
        ))
        fig2.add_hline(y=avg_margin, line_dash="dot", line_color=NEON['pink'], line_width=2,
                      annotation_text=f"Rata-rata: {avg_margin:.1f}%",
                      annotation_font=dict(color=NEON['pink'], size=11, family='Inter'),
                      annotation_position="right")
        apply_layout(fig2, height=320, showlegend=False, bargap=0.35,
                     yaxis=dict(DEFAULT_AXIS, ticksuffix='%', range=[0, max(cat_data['Margin'])*1.25]))
        show_chart(fig2, key='cat_margin')

    # ── CHART ROW 2: Monthly Trend ──
    st.markdown('''<div class="chart-card"><div class="chart-header">
    <div class="chart-title"> Tren Revenue & Profit Bulanan</div>
    <div class="chart-sub">Diagnosa: Pola seasonal — Penjualan tertinggi terjadi pada periode apa?</div>
    </div></div>''', unsafe_allow_html=True)
    monthly = dff.groupby('YearMonth').agg(Revenue=('Revenue','sum'), Profit=('Profit','sum')).reset_index()
    monthly = monthly.sort_values('YearMonth')

    fig3 = go.Figure()
    # Revenue area
    fig3.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Revenue'], name='Revenue',
        line=dict(color=NEON['blue'], width=2.5, shape='spline'),
        fill='tozeroy', fillcolor='rgba(77,195,255,0.08)',
        mode='lines+markers',
        marker=dict(size=6, color=NEON['blue'], line=dict(width=1.5, color='rgba(77,195,255,0.4)'),
                   symbol='circle'),
        hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>',
    ))
    # Profit area
    fig3.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Profit'], name='Profit',
        line=dict(color=NEON['pink'], width=2.5, shape='spline'),
        fill='tozeroy', fillcolor='rgba(255,92,184,0.06)',
        mode='lines+markers',
        marker=dict(size=6, color=NEON['pink'], line=dict(width=1.5, color='rgba(255,92,184,0.4)'),
                   symbol='circle'),
        hovertemplate='<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>',
    ))
    apply_layout(fig3, height=280,
                 xaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=10), tickangle=-45),
                 yaxis=dict(DEFAULT_AXIS, tickformat='$,.0f'),
                 legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='right', x=1,
                            font=dict(size=11, color='#b0c4e8'), bgcolor='rgba(0,0,0,0)'),
                 hovermode='x unified')
    show_chart(fig3, key='monthly_trend')

    # ── CHART ROW 3: Location, City Top 10, Quarterly ──
    c31, c32, c33 = st.columns(3)

    with c31:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Revenue per Lokasi Toko</div>
        <div class="chart-sub">Distribusi revenue berdasarkan tipe lokasi</div>
        </div></div>''', unsafe_allow_html=True)
        loc_data = dff.groupby('Store_Location')['Revenue'].sum().reset_index()
        loc_data = loc_data.sort_values('Revenue', ascending=False)

        loc_colors_map = {'Airport': NEON['blue'], 'Commercial': NEON['purple'],
                         'Downtown': NEON['pink'], 'Residential': NEON['green']}
        loc_c = [loc_colors_map.get(l, NEON['blue']) for l in loc_data['Store_Location']]

        fig4 = go.Figure(go.Pie(
            labels=loc_data['Store_Location'], values=loc_data['Revenue'],
            hole=0.58,
            marker=dict(colors=[hex_rgba(c, 0.82) for c in loc_c],
                       line=dict(color=loc_c, width=2)),
            textfont=dict(color='#e4ecff', size=11.5, family='Inter'),
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>Share: %{percent}<extra></extra>',
            pull=[0.04 if i == 0 else 0 for i in range(len(loc_data))],
        ))
        fig4.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter, sans-serif', color='#b0c4e8', size=11),
            margin=dict(l=10, r=10, t=25, b=20),
            height=340, showlegend=False,
            annotations=[dict(text='<b>Revenue</b><br>by Location', x=0.5, y=0.5, font_size=11,
                            font_color='#7a9abf', showarrow=False, font_family='Inter')]
        )
        show_chart(fig4, key='loc_donut')

    with c32:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Revenue per Kota (Top 10)</div>
        <div class="chart-sub">Kota dengan kontribusi tertinggi</div>
        </div></div>''', unsafe_allow_html=True)
        city_data = dff.groupby('Store_City')['Revenue'].sum().nlargest(10).reset_index()
        city_data = city_data.sort_values('Revenue', ascending=True)

        n_bars = len(city_data)
        grad_colors = [hex_rgba(NEON['green'], 0.25 + 0.65*(i/max(n_bars-1,1))) for i in range(n_bars)]

        fig5 = go.Figure(go.Bar(
            y=city_data['Store_City'], x=city_data['Revenue'],
            orientation='h',
            marker=dict(color=grad_colors, line=dict(width=1, color=NEON['green'])),
            text=[fmt(v) for v in city_data['Revenue']],
            textposition='outside',
            textfont=dict(color='#b0c4e8', size=10),
            hovertemplate='<b>%{y}</b><br>Revenue: $%{x:,.0f}<extra></extra>',
        ))
        apply_layout(fig5, height=340, showlegend=False, bargap=0.25,
                     xaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=10), tickformat='$,.0f'),
                     yaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#c0d0e8', size=10)))
        show_chart(fig5, key='city_rev')

    with c33:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Revenue & Profit per Kuartal</div>
        <div class="chart-sub">Tren kuartalan 2022 vs 2023</div>
        </div></div>''', unsafe_allow_html=True)
        qdata = dff.groupby(['Year','Quarter']).agg(Revenue=('Revenue','sum'), Profit=('Profit','sum')).reset_index()
        qdata['Label'] = qdata.apply(lambda r: f"Q{int(r['Quarter'])} {int(r['Year'])}", axis=1)

        fig6 = go.Figure()
        fig6.add_trace(go.Bar(
            x=qdata['Label'], y=qdata['Revenue'], name='Revenue',
            marker=dict(color=hex_rgba(NEON['purple'], 0.70), line=dict(width=1.5, color=NEON['purple'])),
            hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>',
        ))
        fig6.add_trace(go.Bar(
            x=qdata['Label'], y=qdata['Profit'], name='Profit',
            marker=dict(color=hex_rgba(NEON['pink'], 0.70), line=dict(width=1.5, color=NEON['pink'])),
            hovertemplate='<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>',
        ))
        apply_layout(fig6, height=340, barmode='group', bargap=0.3,
                     yaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=10), tickformat='$,.0f'),
                     xaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=10), tickangle=-30),
                     legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='right', x=1,
                                font=dict(size=10, color='#b0c4e8'), bgcolor='rgba(0,0,0,0)'))
        show_chart(fig6, key='quarterly')

    # ── INSIGHTS ──
    st.markdown('<div class="section-title">Diagnostic Insights — Profitabilitas & Seasonal</div>', unsafe_allow_html=True)
    i1, i2 = st.columns(2)
    with i1:
        st.markdown('''<div class="insight-box insight-pink">
        <div class="ins-title ins-title-pink">Kategori Produk Dominan</div>
        <span class="hl">Electronics</span> memiliki margin tertinggi (~44.6%), meskipun revenue totalnya di urutan ke-3.
        <span class="hl">Toys</span> menghasilkan profit nominal terbesar ($1.08M) karena volume tinggi.
        Pola ini konsisten di seluruh lokasi toko.</div>''', unsafe_allow_html=True)
    with i2:
        st.markdown('''<div class="insight-box insight-purple">
        <div class="ins-title ins-title-purple">Pola Seasonal</div>
        Revenue puncak pada <span class="hl">April–Mei dan Nov–Des</span>, mengindikasikan holiday season.
        Q4 2022 dan Q2 2023 merupakan kuartal paling menguntungkan — perlu strategi stok proaktif menjelang periode tersebut.</div>''', unsafe_allow_html=True)
    i3, i4 = st.columns(2)
    with i3:
        st.markdown('''<div class="insight-box insight-blue">
        <div class="ins-title ins-title-blue">Performa Lokasi Toko</div>
        <span class="hl">Downtown</span> mendominasi ~56.9% total revenue ($8.2M). Airport memiliki margin lebih tinggi
        meski volume lebih rendah. ANOVA menunjukkan perbedaan signifikan (p &lt; 0.001).</div>''', unsafe_allow_html=True)
    with i4:
        st.markdown('''<div class="insight-box insight-green">
        <div class="ins-title ins-title-green">Rekomendasi Strategis</div>
        Fokuskan margin <span class="hl">Electronics</span> dengan bundling. Alokasikan inventory lebih besar menjelang April & November.
        Evaluasi harga Sports &amp; Outdoors (margin terendah ~23.3%).</div>''', unsafe_allow_html=True)

    st.write("")

    # ── TOP 15 PRODUCTS TABLE ──
    st.markdown('<div class="section-title">Top 15 Produk Berdasarkan Profit</div>', unsafe_allow_html=True)
    top_prod = dff.groupby(['Product_Name','Product_Category']).agg(
        Revenue=('Revenue','sum'), Profit=('Profit','sum'), Units=('Units','sum')
    ).reset_index().nlargest(15, 'Profit')
    max_p = top_prod['Profit'].max()
    cat_badge = {'Electronics':'badge-electronics','Toys':'badge-toys',
                 'Art & Crafts':'badge-arts','Games':'badge-games','Sports & Outdoors':'badge-sports'}
    
    rows_html = ""
    for i, r in enumerate(top_prod.itertuples(), 1):
        margin = (r.Profit/r.Revenue*100) if r.Revenue > 0 else 0
        bw = (r.Profit/max_p*100) if max_p > 0 else 0
        badge_cls = cat_badge.get(r.Product_Category, 'badge-toys')
        rows_html += f"""<tr>
        <td style="color:var(--text-dim);font-size:12px;font-weight:600;">{i}</td>
        <td class="td-name">{r.Product_Name}</td>
        <td><span class="td-badge {badge_cls}">{r.Product_Category}</span></td>
        <td style="font-weight:600;">{fmt(r.Revenue)}</td>
        <td style="color:var(--neon-pink);font-weight:700;">{fmt(r.Profit)}</td>
        <td style="font-weight:500;">{r.Units:,}</td>
        <td style="color:var(--neon-green);font-weight:600;">{margin:.1f}%</td>
        <td style="width:110px;"><div class="bar-mini" style="width:{bw:.1f}%"></div></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:var(--radius-lg);max-height:520px;overflow-y:auto;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Nama Produk</th><th>Kategori</th><th>Revenue</th>
    <th>Profit</th><th>Units</th><th>Margin</th><th>Profit Bar</th>
    </tr></thead><tbody>{rows_html}</tbody></table></div></div>""", unsafe_allow_html=True)


# ============================================================
# TAB 2: INVENTORY & STOCKOUT
# ============================================================
with tab2:
    st.markdown("""
    <div style="margin-top:8px; margin-bottom:24px;">
        <div class="page-title">Inventory & Stockout Analysis <span class="tag">Diagnostic</span></div>
        <div class="page-desc">Berapa nilai inventori yang terikat? Toko mana yang mengalami stockout? Berapa potensi kehilangan penjualan?</div>
    </div>
    """, unsafe_allow_html=True)

    # ── FILTERS ──
    fc21, fc22, _sp2 = st.columns([1, 1, 3])
    with fc21:
        cat_filter2 = st.selectbox("KATEGORI", ["Semua"] + sorted(inv['Product_Category'].unique().tolist()), key="cat_f2")
    with fc22:
        dos_filter = st.selectbox("THRESHOLD DoS", ["Semua", "Kritis (<7 hari)", "Rendah (<30 hari)"], key="dos_f")

    # Calculate avg daily sales per store-product
    period_days = (df['Date'].max() - df['Date'].min()).days + 1
    daily_sales = df.groupby(['Store_ID','Product_ID']).agg(
        total_units=('Units','sum')
    ).reset_index()
    daily_sales['avg_daily'] = daily_sales['total_units'] / period_days

    inv2 = inv.merge(daily_sales[['Store_ID','Product_ID','avg_daily']], on=['Store_ID','Product_ID'], how='left')
    inv2['avg_daily'] = inv2['avg_daily'].fillna(0)
    inv2['DoS'] = np.where(inv2['avg_daily'] > 0, inv2['Stock_On_Hand'] / inv2['avg_daily'], np.nan)

    if cat_filter2 != "Semua":
        inv2 = inv2[inv2['Product_Category'] == cat_filter2]
        
    if dos_filter == "Kritis (<7 hari)":
        inv2 = inv2[inv2['DoS'] < 7]
    elif dos_filter == "Rendah (<30 hari)":
        inv2 = inv2[inv2['DoS'] < 30]

    # KPIs
    total_inv_val = inv2['Inv_Value'].sum()
    stockout_count = int((inv2['Stock_On_Hand'] == 0).sum())
    valid_dos = inv2['DoS'].dropna()
    median_dos = valid_dos.median() if len(valid_dos) > 0 else 0
    critical_count = int((valid_dos < 7).sum())

    st.markdown('<div class="section-title">Inventory Key Metrics</div>', unsafe_allow_html=True)
    ik1, ik2, ik3, ik4 = st.columns(4)
    with ik1:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-blue"></div>
        <div class="kpi-icon-bg kpi-icon-blue"></div>
        <div class="kpi-label">Nilai Inventori (at Cost)</div>
        <div class="kpi-value" style="color:var(--neon-blue);">{fmt(total_inv_val)}</div>
        <div class="kpi-sub"><span class="kpi-trend-neutral">Total dana terikat di stok</span></div>
        </div>''', unsafe_allow_html=True)
    with ik2:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-pink"></div>
        <div class="kpi-icon-bg kpi-icon-pink"></div>
        <div class="kpi-label">Kombinasi Stockout</div>
        <div class="kpi-value" style="color:var(--neon-pink);">{stockout_count}</div>
        <div class="kpi-sub"><span class="kpi-trend-neutral">Store-Product stok = 0</span></div>
        </div>''', unsafe_allow_html=True)
    with ik3:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-purple"></div>
        <div class="kpi-icon-bg kpi-icon-purple"></div>
        <div class="kpi-label">Median Days of Supply</div>
        <div class="kpi-value" style="color:var(--neon-purple);">{median_dos:.1f} <span style="font-size:14px;">hari</span></div>
        <div class="kpi-sub"><span class="kpi-trend-neutral">Rata-rata ketahanan stok</span></div>
        </div>''', unsafe_allow_html=True)
    with ik4:
        st.markdown(f'''<div class="kpi-card">
        <div class="kpi-glow-bar kpi-glow-green"></div>
        <div class="kpi-icon-bg kpi-icon-green"></div>
        <div class="kpi-label">Produk Stok Kritis</div>
        <div class="kpi-value" style="color:var(--neon-green);">{critical_count}</div>
        <div class="kpi-sub"><span class="kpi-trend-neutral">Kombinasi DoS &lt; 7 hari</span></div>
        </div>''', unsafe_allow_html=True)

    st.write("")

    # ── CHART ROW: Inv per Category & Stockout per Location ──
    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Nilai Inventori per Kategori (USD)</div>
        <div class="chart-sub">Diagnosa: Dana terikat paling besar di kategori mana?</div>
        </div></div>''', unsafe_allow_html=True)
        inv_cat = inv2.groupby('Product_Category')['Inv_Value'].sum().reset_index()
        inv_cat = inv_cat.sort_values('Inv_Value', ascending=False)
        inv_colors = [hex_rgba(CAT_COLORS.get(c, NEON['blue']), 0.75) for c in inv_cat['Product_Category']]
        inv_borders = [CAT_COLORS.get(c, NEON['blue']) for c in inv_cat['Product_Category']]

        fig7 = go.Figure(go.Bar(
            x=inv_cat['Product_Category'], y=inv_cat['Inv_Value'],
            marker=dict(color=inv_colors, line=dict(width=1.5, color=inv_borders)),
            text=[f"${v:,.0f}" for v in inv_cat['Inv_Value']],
            textposition='outside',
            textfont=dict(color='#b0c4e8', size=10),
            hovertemplate='<b>%{x}</b><br>Inventory Value: $%{y:,.0f}<extra></extra>',
        ))
        apply_layout(fig7, height=320, showlegend=False, bargap=0.35,
                     yaxis=dict(DEFAULT_AXIS, tickformat='$,.0f'))
        show_chart(fig7, key='inv_cat')

    with cc2:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Stockout per Lokasi Toko</div>
        <div class="chart-sub">Diagnosa: Lokasi toko mana paling banyak stockout?</div>
        </div></div>''', unsafe_allow_html=True)
        stockout_loc = inv2[inv2['Stock_On_Hand'] == 0].groupby('Store_Location').size().reset_index(name='count')
        stockout_loc = stockout_loc.sort_values('count', ascending=False)

        so_loc_colors = {'Airport': NEON['blue'], 'Commercial': NEON['purple'],
                        'Downtown': NEON['pink'], 'Residential': NEON['green']}
        so_c = [hex_rgba(so_loc_colors.get(l, NEON['blue']), 0.75) for l in stockout_loc['Store_Location']]
        so_b = [so_loc_colors.get(l, NEON['blue']) for l in stockout_loc['Store_Location']]

        fig8 = go.Figure(go.Bar(
            x=stockout_loc['Store_Location'], y=stockout_loc['count'],
            marker=dict(color=so_c, line=dict(width=1.5, color=so_b)),
            text=stockout_loc['count'],
            textposition='outside',
            textfont=dict(color='#b0c4e8', size=12, family='Inter'),
            hovertemplate='<b>%{x}</b><br>Stockout Count: %{y}<extra></extra>',
        ))
        apply_layout(fig8, height=320, showlegend=False, bargap=0.35,
                     yaxis=dict(**DEFAULT_AXIS))
        show_chart(fig8, key='stockout_loc')

    # ── CHART ROW 2: Inv per City & DoS Distribution ──
    cc3, cc4 = st.columns(2)
    with cc3:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Top 10 Kota: Nilai Inventori (USD)</div>
        <div class="chart-sub">Distribusi nilai inventori antar kota</div>
        </div></div>''', unsafe_allow_html=True)
        inv_city = inv2.groupby('Store_City')['Inv_Value'].sum().nlargest(10).reset_index()
        inv_city = inv_city.sort_values('Inv_Value', ascending=True)

        n_city = len(inv_city)
        city_grad = [hex_rgba(NEON['blue'], 0.25 + 0.65*(i/max(n_city-1,1))) for i in range(n_city)]

        fig9 = go.Figure(go.Bar(
            y=inv_city['Store_City'], x=inv_city['Inv_Value'], orientation='h',
            marker=dict(color=city_grad, line=dict(width=1, color=NEON['blue'])),
            text=[f"${v:,.0f}" for v in inv_city['Inv_Value']],
            textposition='outside',
            textfont=dict(color='#b0c4e8', size=9.5),
            hovertemplate='<b>%{y}</b><br>Inventory Value: $%{x:,.0f}<extra></extra>',
        ))
        apply_layout(fig9, height=340, showlegend=False,
                     xaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=10), tickformat='$,.0f'),
                     yaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#c0d0e8', size=10)))
        show_chart(fig9, key='inv_city')

    with cc4:
        st.markdown('''<div class="chart-card"><div class="chart-header">
        <div class="chart-title"> Distribusi Days of Supply</div>
        <div class="chart-sub">Sebaran ketahanan stok per Store-Product (capped 180 hari)</div>
        </div></div>''', unsafe_allow_html=True)
        dos_vals = inv2['DoS'].dropna()
        dos_capped = dos_vals.clip(upper=180)
        bins_edges = [0, 10, 20, 30, 40, 50, 60, 80, 100, 120, 150, 180]
        counts_h, _ = np.histogram(dos_capped, bins=bins_edges)
        bin_labels = [f"{bins_edges[i]}–{bins_edges[i+1]}" for i in range(len(bins_edges)-1)]

        bar_colors_dos = []
        bar_borders_dos = []
        for i in range(len(counts_h)):
            if i < 1:
                bar_colors_dos.append(hex_rgba(NEON['pink'], 0.85))
                bar_borders_dos.append(NEON['pink'])
            elif i < 3:
                bar_colors_dos.append(hex_rgba(NEON['orange'], 0.70))
                bar_borders_dos.append(NEON['orange'])
            elif i < 5:
                bar_colors_dos.append(hex_rgba(NEON['purple'], 0.60))
                bar_borders_dos.append(NEON['purple'])
            else:
                bar_colors_dos.append(hex_rgba(NEON['blue'], 0.45))
                bar_borders_dos.append(NEON['blue'])

        fig10 = go.Figure(go.Bar(
            x=bin_labels, y=counts_h,
            marker=dict(color=bar_colors_dos, line=dict(width=1.5, color=bar_borders_dos)),
            text=counts_h,
            textposition='outside',
            textfont=dict(color='#b0c4e8', size=10),
            hovertemplate='<b>DoS %{x} hari</b><br>Frekuensi: %{y} kombinasi<extra></extra>',
        ))
        fig10.add_vline(x=0.5, line_dash="dot", line_color=NEON['pink'], line_width=2,
                       annotation_text=" Kritis",
                       annotation_font=dict(color=NEON['pink'], size=10),
                       annotation_position="top")
        apply_layout(fig10, height=340, showlegend=False,
                     xaxis=dict(DEFAULT_AXIS, tickfont=dict(color='#7a9abf', size=9),
                               title=dict(text='Days of Supply', font=dict(color='#7a9abf', size=11))),
                     yaxis=dict(DEFAULT_AXIS,
                               title=dict(text='Frekuensi', font=dict(color='#7a9abf', size=11))))
        show_chart(fig10, key='dos_dist')

    # ── INSIGHTS ──
    st.markdown('<div class="section-title">Diagnostic Insights — Inventory & Stockout</div>', unsafe_allow_html=True)
    ii1, ii2 = st.columns(2)
    with ii1:
        st.markdown(f'''<div class="insight-box insight-pink">
        <div class="ins-title ins-title-pink">Risiko Stockout</div>
        Terdapat <span class="hl">{stockout_count} kombinasi store-product</span> dengan stok habis.
        <span class="hl">Colorbuds (Electronics)</span> paling sering stockout padahal merupakan produk profit tertinggi — potensi kerugian signifikan.</div>''', unsafe_allow_html=True)
    with ii2:
        st.markdown(f'''<div class="insight-box insight-purple">
        <div class="ins-title ins-title-purple">Ketahanan Stok</div>
        Median DoS <span class="hl">{median_dos:.1f} hari</span> — rotasi cukup baik.
        Namun <span class="hl">{critical_count} kombinasi</span> store-product memiliki DoS &lt; 7 hari, perlu reorder segera.</div>''', unsafe_allow_html=True)
    ii3, ii4 = st.columns(2)
    with ii3:
        st.markdown(f'''<div class="insight-box insight-blue">
        <div class="ins-title ins-title-blue">Dana Terikat di Inventori</div>
        Total <span class="hl">{fmt(total_inv_val)}</span> terikat di inventori (at cost). <span class="hl">Toys</span>
        mendominasi nilai inventori — margin rendah → indikasi over-stocking.</div>''', unsafe_allow_html=True)
    with ii4:
        st.markdown('''<div class="insight-box insight-green">
        <div class="ins-title ins-title-green">Rekomendasi Operasional</div>
        Terapkan <span class="hl">reorder point otomatis</span> saat DoS &lt; 14 hari. Prioritaskan restock Electronics (margin tinggi).
        Kurangi over-stock Toys di lokasi Residential.</div>''', unsafe_allow_html=True)

    st.write("")

    # ── STORE TABLE ──
    st.markdown('<div class="section-title">Performa 15 Toko Teratas</div>', unsafe_allow_html=True)
    store_perf = df.groupby(['Store_Name','Store_City','Store_Location']).agg(
        Revenue=('Revenue','sum'), Profit=('Profit','sum'), Units=('Units','sum')
    ).reset_index()
    store_perf['Margin'] = store_perf['Profit'] / store_perf['Revenue']
    top_stores = store_perf.nlargest(15, 'Revenue')
    max_r = top_stores['Revenue'].max()
    loc_color_map = {'Airport':'#4dc3ff','Commercial':'#b84dff','Downtown':'#ff5cb8','Residential':'#3dff6f'}

    srows = ""
    for i, r in enumerate(top_stores.itertuples(), 1):
        lc = loc_color_map.get(r.Store_Location, '#4dc3ff')
        bw = (r.Revenue/max_r*100)
        srows += f"""<tr>
        <td style="color:var(--text-dim);font-size:12px;font-weight:600;">{i}</td>
        <td class="td-name">{r.Store_Name}</td><td>{r.Store_City}</td>
        <td><span style="display:inline-block;padding:4px 12px;border-radius:20px;font-size:10px;font-weight:700;
            background:{lc}18;color:{lc};border:1px solid {lc}40;">{r.Store_Location}</span></td>
        <td style="color:var(--neon-blue);font-weight:700;">{fmt(r.Revenue)}</td>
        <td style="color:var(--neon-pink);font-weight:600;">{fmt(r.Profit)}</td>
        <td style="font-weight:500;">{int(r.Units):,}</td>
        <td style="color:var(--neon-green);font-weight:600;">{r.Margin*100:.1f}%</td>
        <td style="width:110px;"><div class="bar-mini-blue" style="width:{bw:.1f}%"></div></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:var(--radius-lg);max-height:520px;overflow-y:auto;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Nama Toko</th><th>Kota</th><th>Lokasi</th>
    <th>Revenue</th><th>Profit</th><th>Units</th><th>Margin</th><th>Revenue Bar</th>
    </tr></thead><tbody>{srows}</tbody></table></div></div>""", unsafe_allow_html=True)


# ============================================================
# TAB 3: DATA PIPELINE
# ============================================================
with tab3:
    st.markdown("""
    <div style="margin-top:8px; margin-bottom:24px;">
        <div class="page-title">Data Pipeline <span class="tag">ETL Process</span></div>
        <div class="page-desc">Visualisasi alur pemrosesan data dari sumber mentah hingga siap analisis — Extract, Transform, Load.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── PIPELINE FLOW DIAGRAM ──
    st.markdown('<div class="section-title">Pipeline Architecture</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="pipe-flow">
        <div class="pipe-node pipe-node-extract">
            <div class="pipe-label pipe-label-blue">Extract</div>
            <div class="pipe-icon"></div>
            <div class="pipe-desc">4 file CSV<br>sumber data mentah</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-transform">
            <div class="pipe-label pipe-label-purple">Clean</div>
            <div class="pipe-icon"></div>
            <div class="pipe-desc">Parsing harga,<br>konversi tipe data</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-transform">
            <div class="pipe-label pipe-label-purple">Merge</div>
            <div class="pipe-icon"></div>
            <div class="pipe-desc">Join tabel via<br>Product_ID & Store_ID</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-load">
            <div class="pipe-label pipe-label-green">Engineer</div>
            <div class="pipe-icon"></div>
            <div class="pipe-desc">Revenue, Profit,<br>Margin, DoS</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-analyze">
            <div class="pipe-label pipe-label-pink">Analyze</div>
            <div class="pipe-icon"></div>
            <div class="pipe-desc">Dashboard<br>interaktif</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── STEP 1: EXTRACT ──
    st.markdown('<div class="section-title">Step 1 — Extract (Sumber Data)</div>', unsafe_allow_html=True)

    source_files = [
        ("sales.csv", "Transaksi penjualan", len(pd.read_csv("sales.csv")), 5, "Sale_ID, Date, Store_ID, Product_ID, Units"),
        ("products.csv", "Master produk", len(products), 5, "Product_ID, Product_Name, Product_Category, Product_Cost, Product_Price"),
        ("stores.csv", "Master toko", len(stores), 5, "Store_ID, Store_Name, Store_City, Store_Location, Store_Open_Date"),
        ("inventory.csv", "Stok per toko-produk", len(inventory), 3, "Store_ID, Product_ID, Stock_On_Hand"),
    ]

    src_rows = ""
    total_raw_rows = 0
    for fname, desc, rows, cols, columns in source_files:
        total_raw_rows += rows
        src_rows += f"""<tr>
        <td class="td-name"> {fname}</td>
        <td>{desc}</td>
        <td style="color:var(--neon-blue);font-weight:700;">{rows:,}</td>
        <td style="font-weight:600;">{cols}</td>
        <td style="font-size:11px;color:var(--text-dim);font-family:'JetBrains Mono',monospace;">{columns}</td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:var(--radius-lg);">
    <table class="custom-table"><thead><tr>
    <th>File</th><th>Deskripsi</th><th>Baris</th><th>Kolom</th><th>Kolom Utama</th>
    </tr></thead><tbody>{src_rows}</tbody></table></div></div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-box insight-blue" style="margin-top:14px;">
        <div class="ins-title ins-title-blue">Ringkasan Extract</div>
        Total <span class="hl">{total_raw_rows:,}</span> baris data mentah dari <span class="hl">4 file CSV</span>.
        Dataset utama: <span class="hl">Dataframe Merged Sales</span> ({len(df):,} baris).
        Sumber: <span class="hl">Maven Analytics — Maven Toys Dataset </span>.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 2: TRANSFORM (CLEAN) ──
    st.markdown('<div class="section-title">Step 2 — Transform (Pembersihan Data)</div>', unsafe_allow_html=True)

    clean_steps = [
        ("1", "Parsing Harga", "Menghapus simbol <code>$</code> dan spasi dari kolom Product_Cost & Product_Price",
         "<code style='color:#ff5cb8;'>$9.99  → 9.99</code>", "#ff5cb8"),
        ("2", "Konversi Tanggal", "Mengubah kolom Date dari string ke tipe datetime",
         "<code style='color:#b84dff;'>2022-01-01 → Timestamp</code>", "#b84dff"),
        ("3", "Handling Missing", "Mengecek dan menangani nilai null pada semua kolom",
         f"<code style='color:#4dc3ff;'>Null count: {df.isnull().sum().sum()}</code>", "#4dc3ff"),
        ("4", "Validasi Tipe Data", "Memastikan kolom numerik bertipe float/int, kategorikal bertipe object",
         "<code style='color:#3dff6f;'>Units: int64, Revenue: float64</code>", "#3dff6f"),
    ]

    for step_num, title, desc, example, color in clean_steps:
        st.markdown(f"""
        <div class="step-card" style="border-left: 4px solid {color};">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="min-width:36px;height:36px;border-radius:10px;background:{color}15;
                     display:flex;align-items:center;justify-content:center;
                     font-weight:800;color:{color};font-size:15px;border:1px solid {color}35;
                     flex-shrink:0;">{step_num}</div>
                <div style="flex:1;">
                    <div style="font-size:13.5px;font-weight:700;color:var(--text-primary);margin-bottom:3px;">{title}</div>
                    <div style="font-size:12px;color:var(--text-secondary);">{desc}</div>
                </div>
                <div style="font-size:11.5px;color:var(--text-dim);text-align:right;flex-shrink:0;">{example}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 3: MERGE / JOIN ──
    st.markdown('<div class="section-title">Step 3 — Merge (Penggabungan Tabel)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card" style="text-align:center; padding:28px;">
        <div style="display:flex; align-items:center; justify-content:center; gap:14px; flex-wrap:wrap;">
            <div style="background:rgba(77,195,255,0.08); border:1px solid rgba(77,195,255,0.25); border-radius:var(--radius-md); padding:16px 22px;">
                <div style="font-size:9px;color:var(--neon-blue);font-weight:700;letter-spacing:1.2px;">SALES</div>
                <div style="font-size:20px;font-weight:800;color:var(--text-primary);margin:4px 0;">829K rows</div>
                <div style="font-size:10px;color:var(--text-dim);font-family:'JetBrains Mono',monospace;">Sale_ID, Date, Store_ID,<br>Product_ID, Units</div>
            </div>
            <div style="font-size:14px;color:var(--neon-purple);font-weight:700;text-align:center;">⟕<br><span style="font-size:8.5px;letter-spacing:0.5px;">LEFT JOIN<br>Product_ID</span></div>
            <div style="background:rgba(184,77,255,0.08); border:1px solid rgba(184,77,255,0.25); border-radius:var(--radius-md); padding:16px 22px;">
                <div style="font-size:9px;color:var(--neon-purple);font-weight:700;letter-spacing:1.2px;">PRODUCTS</div>
                <div style="font-size:20px;font-weight:800;color:var(--text-primary);margin:4px 0;">35 rows</div>
                <div style="font-size:10px;color:var(--text-dim);font-family:'JetBrains Mono',monospace;">Product_Name, Category,<br>Cost, Price</div>
            </div>
            <div style="font-size:14px;color:var(--neon-purple);font-weight:700;text-align:center;">⟕<br><span style="font-size:8.5px;letter-spacing:0.5px;">LEFT JOIN<br>Store_ID</span></div>
            <div style="background:rgba(61,255,111,0.06); border:1px solid rgba(61,255,111,0.20); border-radius:var(--radius-md); padding:16px 22px;">
                <div style="font-size:9px;color:var(--neon-green);font-weight:700;letter-spacing:1.2px;">STORES</div>
                <div style="font-size:20px;font-weight:800;color:var(--text-primary);margin:4px 0;">50 rows</div>
                <div style="font-size:10px;color:var(--text-dim);font-family:'JetBrains Mono',monospace;">Store_Name, City,<br>Location</div>
            </div>
            <div style="font-size:22px;color:var(--neon-pink);padding:0 12px;">→</div>
            <div style="background:rgba(255,92,184,0.08); border:1px solid rgba(255,92,184,0.25); border-radius:var(--radius-md); padding:16px 22px;">
                <div style="font-size:9px;color:var(--neon-pink);font-weight:700;letter-spacing:1.2px;">MERGED DATASET</div>
                <div style="font-size:20px;font-weight:800;color:var(--text-primary);margin:4px 0;">829K × 14</div>
                <div style="font-size:10px;color:var(--text-dim);font-family:'JetBrains Mono',monospace;">Merged in Memory</div>
            </div>
        </div>
        <div style="margin-top:18px; font-size:11.5px; color:var(--text-dim); line-height:1.6;">
            Pipeline inventori terpisah: <span style="color:var(--neon-blue);">inventory.csv</span> ⟕ products ⟕ stores →
            <span style="color:var(--neon-green);">inv DataFrame</span> (1,593 baris)
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 4: FEATURE ENGINEERING ──
    st.markdown('<div class="section-title">Step 4 — Feature Engineering (Kolom Turunan)</div>', unsafe_allow_html=True)

    features = [
        ("Revenue", "Units × Product_Price", "Pendapatan per transaksi", "float64", "#ff5cb8"),
        ("Profit", "Units × (Price − Cost)", "Laba kotor per transaksi", "float64", "#b84dff"),
        ("Year", "Date.dt.year", "Tahun transaksi", "int64", "#4dc3ff"),
        ("Month", "Date.dt.month", "Bulan transaksi (1-12)", "int64", "#4dc3ff"),
        ("Quarter", "Date.dt.quarter", "Kuartal transaksi (1-4)", "int64", "#4dc3ff"),
        ("YearMonth", "Date.dt.to_period('M')", "Periode bulanan (2022-01)", "str", "#4dc3ff"),
        ("Inv_Value", "Stock × Product_Cost", "Nilai inventori at cost", "float64", "#3dff6f"),
        ("Avg_Daily_Sales", "Total_Units / Days", "Rata-rata penjualan harian", "float64", "#3dff6f"),
        ("Days_of_Supply", "Stock / Avg_Daily", "Ketahanan stok (hari)", "float64", "#ffaa33"),
    ]

    feat_rows = ""
    for name, formula, desc, dtype, color in features:
        feat_rows += f"""<tr>
        <td class="td-name" style="color:{color};">{name}</td>
        <td style="font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);">{formula}</td>
        <td>{desc}</td>
        <td><span class="td-badge" style="background:{color}12;color:{color};border:1px solid {color}35;">{dtype}</span></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:var(--radius-lg);">
    <table class="custom-table"><thead><tr>
    <th>Kolom Baru</th><th>Formula</th><th>Deskripsi</th><th>Tipe</th>
    </tr></thead><tbody>{feat_rows}</tbody></table></div></div>""", unsafe_allow_html=True)

    st.write("")

    # ── STEP 5: DATA QUALITY ──
    st.markdown('<div class="section-title">Step 5 — Data Quality Check</div>', unsafe_allow_html=True)

    null_count = int(df.isnull().sum().sum())
    dup_count = int(df.duplicated(subset=['Sale_ID']).sum())
    date_min = df['Date'].min().strftime('%Y-%m-%d')
    date_max = df['Date'].max().strftime('%Y-%m-%d')
    period_days_val = (df['Date'].max() - df['Date'].min()).days + 1
    n_stores = df['Store_ID'].nunique()
    n_products = df['Product_ID'].nunique()
    n_cities = df['Store_City'].nunique()
    neg_revenue = int((df['Revenue'] < 0).sum())
    neg_profit = int((df['Profit'] < 0).sum())

    qc1, qc2 = st.columns(2)
    with qc1:
        checks = [
            ("Null Values", f"{null_count}", " Bersih" if null_count == 0 else f" {null_count} null", "#3dff6f" if null_count == 0 else "#ff5cb8"),
            ("Duplikat Sale_ID", f"{dup_count}", " Tidak ada duplikat" if dup_count == 0 else f" {dup_count} duplikat", "#3dff6f" if dup_count == 0 else "#ffaa33"),
            ("Revenue Negatif", f"{neg_revenue}", " Tidak ada" if neg_revenue == 0 else f" {neg_revenue} baris", "#3dff6f" if neg_revenue == 0 else "#ff5cb8"),
            ("Profit Negatif", f"{neg_profit}", " Tidak ada" if neg_profit == 0 else f" {neg_profit} baris (wajar)", "#3dff6f" if neg_profit == 0 else "#4dc3ff"),
        ]

        st.markdown('<div style="font-size:13px;font-weight:700;color:var(--text-primary);margin-bottom:12px;">Quality Checks</div>', unsafe_allow_html=True)
        for check_name, value, status, color in checks:
            st.markdown(f"""
            <div class="step-card" style="border-left:4px solid {color}; padding:12px 18px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-size:12.5px;font-weight:600;color:var(--text-primary);">{check_name}</span>
                        <span style="font-size:11px;color:var(--text-dim);margin-left:8px;">({value})</span>
                    </div>
                    <span style="font-size:11.5px;color:{color};font-weight:600;">{status}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with qc2:
        st.markdown(f"""
        <div class="chart-card" style="padding:20px;">
            <div style="font-size:13px;font-weight:700;color:var(--text-primary);margin-bottom:16px;"> Dataset Summary</div>
            <table style="width:100%;font-size:12.5px;color:var(--text-secondary);">
            <tr><td style="padding:7px 0;"> Periode Data</td>
                <td style="text-align:right;color:var(--text-primary);font-weight:600;">{date_min} → {date_max}</td></tr>
            <tr><td style="padding:7px 0;"> Total Hari</td>
                <td style="text-align:right;color:var(--neon-blue);font-weight:700;">{period_days_val:,} hari</td></tr>
            <tr><td style="padding:7px 0;"> Total Transaksi</td>
                <td style="text-align:right;color:var(--neon-pink);font-weight:700;">{len(df):,}</td></tr>
            <tr><td style="padding:7px 0;"> Jumlah Toko</td>
                <td style="text-align:right;color:var(--neon-purple);font-weight:700;">{n_stores}</td></tr>
            <tr><td style="padding:7px 0;"> Jumlah Produk</td>
                <td style="text-align:right;color:var(--neon-green);font-weight:700;">{n_products}</td></tr>
            <tr><td style="padding:7px 0;"> Jumlah Kota</td>
                <td style="text-align:right;color:var(--neon-orange);font-weight:700;">{n_cities}</td></tr>
            <tr><td style="padding:7px 0;"> Kombinasi Inventori</td>
                <td style="text-align:right;color:var(--neon-blue);font-weight:700;">{len(inventory):,}</td></tr>
            <tr style="border-top:1px solid rgba(77,195,255,0.12);">
                <td style="padding:9px 0;font-weight:600;color:var(--text-primary);"> Kolom Final</td>
                <td style="text-align:right;color:var(--text-primary);font-weight:700;">{len(df.columns)} kolom</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ── SCHEMA OVERVIEW ──
    st.markdown('<div class="section-title">Schema — Kolom Dataset Final</div>', unsafe_allow_html=True)

    schema_rows = ""
    for i, col in enumerate(df.columns):
        dtype_str = str(df[col].dtype)
        sample_val = str(df[col].dropna().iloc[0]) if len(df[col].dropna()) > 0 else "N/A"
        if len(sample_val) > 35:
            sample_val = sample_val[:35] + "…"
        null_pct = df[col].isnull().mean() * 100
        unique_count = df[col].nunique()

        dtype_color = "#4dc3ff" if "int" in dtype_str else ("#ff5cb8" if "float" in dtype_str else ("#b84dff" if "datetime" in dtype_str else "#7a9abf"))

        schema_rows += f"""<tr>
        <td style="color:var(--text-dim);font-size:11px;font-weight:600;">{i+1}</td>
        <td class="td-name">{col}</td>
        <td><span class="td-badge" style="background:{dtype_color}12;color:{dtype_color};border:1px solid {dtype_color}35;">{dtype_str}</span></td>
        <td style="font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);">{sample_val}</td>
        <td style="color:var(--neon-green);font-weight:600;">{unique_count:,}</td>
        <td style="color:{'var(--neon-green)' if null_pct == 0 else 'var(--neon-pink)'};font-weight:600;">{null_pct:.1f}%</td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:var(--radius-lg);max-height:480px;overflow-y:auto;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Kolom</th><th>Tipe Data</th><th>Contoh Nilai</th><th>Unik</th><th>Null %</th>
    </tr></thead><tbody>{schema_rows}</tbody></table></div></div>""", unsafe_allow_html=True)


# ============================================================
# TAB 4: EXECUTIVE INSIGHTS
# ============================================================
with tab4:
    st.markdown('''
    <div style="margin-top:8px; margin-bottom:24px;">
        <div class="page-title">Executive Insights <span class="tag">Rekomendasi Strategis</span></div>
        <div class="page-desc">Rangkuman temuan utama (insights) dan tindakan strategis berdasarkan pengolahan data keseluruhan Maven Toys.</div>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Temuan Utama & Tindakan (Actionable Insights)</div>', unsafe_allow_html=True)
    
    ic1, ic2 = st.columns(2)
    with ic1:
        st.markdown('''<div class="chart-card" style="min-height:220px; margin-bottom:20px;">
        <div class="kpi-glow-bar kpi-glow-pink"></div>
        <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:12px;">Paradoks Profit: Electronics vs Toys</div>
        <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.6;">
        Kategori <span style="color:var(--neon-pink); font-weight:700;">Electronics</span> memiliki rata-rata margin keuntungan tertinggi mencapai nyaris <span style="color:var(--text-primary); font-weight:700;">45%</span>, jauh melampaui kategori lain. Sebaliknya, kategori <span style="color:var(--neon-blue); font-weight:700;">Toys</span> mendominasi secara absolut dalam volume penjualan dan mengikat ruang gudang mendalam, namun memiliki margin yang tergolong pas-pasan.<br><br>
        <span style="color:var(--neon-green); font-weight:600;">Rekomendasi Strategis:</span><br>
        Terapkan taktik "bundling" strategis. Gabungkan produk Toys lambat-laku sebagai diskon paket dengan pembelian item Electronics untuk mendongkrak marjin transaksi keranjang (checkout) secara keseluruhan.
        </div></div>''', unsafe_allow_html=True)
        
        st.markdown('''<div class="chart-card" style="min-height:220px;">
        <div class="kpi-glow-bar kpi-glow-blue"></div>
        <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:12px;">Dominasi Lokasi Downtown & Peluang Airport</div>
        <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.6;">
        Jaringan toko di wilayah <span style="color:var(--neon-blue); font-weight:700;">Downtown</span> memberikan sumbangsih revenue raksasa yang menyentuh angka <span style="color:var(--text-primary); font-weight:700;">~57%</span> dari total usabilitas seluruh perseroan. Namun, pemodelan margin juga menemukan bahwa gerai Airport menghasilkan porsi per transaksi yang lebih tinggi yang menandakan tingkat pembelian impresif spontan (impulse buy).<br><br>
        <span style="color:var(--neon-green); font-weight:600;">Rekomendasi Strategis:</span><br> 
        Optimalkan alokasi logistik prioritas ke Downtown. Selain itu, buka perluasan stan skala kecil ekspres (kios pop-up) di area check-in Airport yang diisi *merchandise* premium berukuran kecil untuk dibawa ke pesawat.
        </div></div>''', unsafe_allow_html=True)

    with ic2:
        st.markdown('''<div class="chart-card" style="min-height:220px; margin-bottom:20px;">
        <div class="kpi-glow-bar kpi-glow-purple"></div>
        <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:12px;">Kerentanan Rantai Pasok (Stockouts)</div>
        <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.6;">
        Pemetaan ketersediaan saat ini membaca ada puluhan toko yang telah membukukan metrik <span style="color:var(--text-primary); font-weight:700;">Stok Kosong</span> pada kombinasi barang. Hal paling rawan adalah benda berprofil keuntungan tebal sering kali terjual habis sebelum siklus pengiriman reguler tiba dari pemasok, memakan potensi pemasukan.<br><br>
        <span style="color:var(--neon-green); font-weight:600;">Rekomendasi Strategis:</span><br>
        Peringatan Dini (Early Warning System) yang menggunakan matriks Days of Supply (Ketahanan Stok) harus dimanfaatkan tim logistik untuk mendanai inventori sebelum kurun batas 10 HARI terakhir.
        </div></div>''', unsafe_allow_html=True)
        
        st.markdown('''<div class="chart-card" style="min-height:220px;">
        <div class="kpi-glow-bar kpi-glow-green"></div>
        <div style="font-size:16px; font-weight:800; color:var(--text-primary); margin-bottom:12px;">Lonjakan Musiman (Festive Seasonality)</div>
        <div style="font-size:12.5px; color:var(--text-secondary); line-height:1.6;">
        Diagnosis data berbasis deret waktu menyoroti adanya siklus perputaran tajam yang sangat terfokus di ambang gerbang waktu liburan tengah tahun, serta terutama <span style="color:var(--text-primary); font-weight:700;">Kuartal 4 (Q4)</span> yang menjadi tumpuan utama penciptaan omzet.<br><br>
        <span style="color:var(--neon-green); font-weight:600;">Rekomendasi Strategis:</span><br>
        Fase persiapan tidak boleh dimulai pada bulan November. Modifikasi kalender distribusi gudang pusat ke depan memajukan re-stok material musim festival maju 1,5 hingga 2 bulan (mulai pertengahan kuartal 3) guna menepis naiknya biaya transportasi saat kuartal akhir.
        </div></div>''', unsafe_allow_html=True)

# ── FOOTER ──
st.markdown("""
<div class="dashboard-footer">
    <span style="color:var(--neon-purple);">●</span> &nbsp;
    Maven Toys Business Analytics Dashboard &nbsp;·&nbsp; ITS Statistika 2026 &nbsp;·&nbsp; Case Study 7
    &nbsp;·&nbsp; Built with Streamlit & Plotly
</div>
""", unsafe_allow_html=True)
