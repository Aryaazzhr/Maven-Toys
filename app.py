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
    page_icon="🧸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS - Neon Cyberpunk Theme
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg-dark: #050d1a;
    --bg-panel: rgba(8, 20, 45, 0.85);
    --bg-glass: rgba(14, 30, 65, 0.6);
    --border-glow: rgba(180, 77, 255, 0.35);
    --border-dim: rgba(77, 195, 255, 0.2);
    --neon-pink: #ff4da6;
    --neon-purple: #b84dff;
    --neon-blue: #4dc3ff;
    --neon-green: #39ff14;
    --text-primary: #dce8ff;
    --text-dim: #7a9abf;
    --text-label: #aabdd8;
}

/* Hide Streamlit defaults */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}
div[data-testid="stToolbar"] {display: none;}
div[data-testid="stDecoration"] {display: none;}
div[data-testid="stStatusWidget"] {display: none;}

/* Main Background */
.stApp, [data-testid="stAppViewContainer"], .main, section[data-testid="stMain"] {
    background: #050d1a !important;
    background-image:
        radial-gradient(ellipse at 20% 10%, rgba(184,77,255,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(77,195,255,0.06) 0%, transparent 50%) !important;
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
}
.block-container {
    padding-top: 0 !important;
    max-width: 100% !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* Custom Header */
.custom-header {
    background: rgba(8, 20, 45, 0.85);
    border-bottom: 1px solid rgba(180, 77, 255, 0.35);
    backdrop-filter: blur(12px);
    padding: 14px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 30px rgba(184,77,255,0.15);
    margin: -1rem -2rem 0 -2rem;
    width: calc(100% + 4rem);
}
.logo-area { display: flex; align-items: center; gap: 14px; }
.logo-icon {
    width: 38px; height: 38px;
    background: linear-gradient(135deg, #b84dff, #ff4da6);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 900; color: #fff;
    box-shadow: 0 0 18px rgba(184,77,255,0.4);
}
.logo-text { font-size: 18px; font-weight: 700; color: #dce8ff; letter-spacing: 0.5px; }
.logo-sub { font-size: 11px; color: #7a9abf; margin-top: 2px; }
.header-right { display: flex; align-items: center; gap: 12px; }
.badge-header {
    font-size: 10px; padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.5px;
}
.badge-pink { background: rgba(255,77,166,0.1); border: 1px solid rgba(255,77,166,0.4); color: #ff4da6; }
.badge-blue { background: rgba(77,195,255,0.1); border: 1px solid rgba(77,195,255,0.4); color: #4dc3ff; }
.live-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #39ff14;
    box-shadow: 0 0 10px #39ff14;
    animation: pulse 2s infinite;
    display: inline-block;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }

/* Tabs */
div[data-testid="stTabs"] {
    background: rgba(8,20,45,0.9);
    border-bottom: 1px solid rgba(77,195,255,0.2);
    margin: 0 -2rem;
    padding: 0 32px;
}
div[data-testid="stTabs"] button {
    color: #7a9abf !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.3px;
    border-bottom: 3px solid transparent !important;
    background: none !important;
    padding: 14px 28px !important;
}
div[data-testid="stTabs"] button:hover { color: #4dc3ff !important; }
div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #ff4da6 !important;
    border-bottom-color: #ff4da6 !important;
    background: rgba(255,77,166,0.05) !important;
}

/* KPI Cards */
.kpi-card {
    background: rgba(14, 30, 65, 0.6);
    border: 1px solid rgba(77, 195, 255, 0.2);
    border-radius: 14px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(8px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.kpi-card:hover { border-color: #b84dff; box-shadow: 0 0 18px rgba(184,77,255,0.4); }
.kpi-label {
    font-size: 11px; color: #7a9abf; font-weight: 600;
    letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 10px;
}
.kpi-value { font-size: 26px; font-weight: 800; line-height: 1; margin-bottom: 6px; }
.kpi-sub { font-size: 11px; color: #7a9abf; }
.kpi-icon { position: absolute; right: 18px; top: 18px; font-size: 24px; opacity: 0.15; color: #dce8ff; }
.kpi-bar-pink { height: 2px; background: linear-gradient(90deg, #ff4da6, transparent); margin: -20px -22px 20px; }
.kpi-bar-purple { height: 2px; background: linear-gradient(90deg, #b84dff, transparent); margin: -20px -22px 20px; }
.kpi-bar-blue { height: 2px; background: linear-gradient(90deg, #4dc3ff, transparent); margin: -20px -22px 20px; }
.kpi-bar-green { height: 2px; background: linear-gradient(90deg, #39ff14, transparent); margin: -20px -22px 20px; }

/* Section Title */
.section-title {
    font-size: 11px; font-weight: 700; letter-spacing: 1.5px;
    color: #7a9abf; text-transform: uppercase;
    margin-bottom: 14px; padding-left: 2px;
}

/* Chart Card */
.chart-card {
    background: rgba(14, 30, 65, 0.6);
    border: 1px solid rgba(77, 195, 255, 0.2);
    border-radius: 14px;
    padding: 22px;
    backdrop-filter: blur(8px);
    transition: border-color 0.25s;
    margin-bottom: 18px;
}
.chart-card:hover { border-color: rgba(184,77,255,0.4); }
.chart-title { font-size: 13px; font-weight: 700; color: #dce8ff; margin-bottom: 4px; }
.chart-sub { font-size: 11px; color: #7a9abf; margin-bottom: 14px; }

/* Page Title */
.page-title { font-size: 22px; font-weight: 800; color: #dce8ff; margin-bottom: 4px; }
.page-desc { font-size: 13px; color: #7a9abf; margin-bottom: 22px; }
.tag {
    display: inline-block; padding: 2px 10px; border-radius: 10px; font-size: 11px;
    background: rgba(77,195,255,0.1); color: #4dc3ff;
    border: 1px solid rgba(77,195,255,0.25); margin-left: 10px;
    vertical-align: middle; font-weight: 600;
}

/* Insight Boxes */
.insight-box {
    background: rgba(14, 30, 65, 0.6);
    border-radius: 12px;
    padding: 16px 18px;
    font-size: 12.5px; color: #aabdd8; line-height: 1.6;
}
.insight-purple { border-left: 3px solid #b84dff; }
.insight-pink { border-left: 3px solid #ff4da6; }
.insight-blue { border-left: 3px solid #4dc3ff; }
.insight-green { border-left: 3px solid #39ff14; }
.ins-title {
    font-size: 12px; font-weight: 700;
    letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 6px;
}
.ins-title-purple { color: #b84dff; }
.ins-title-pink { color: #ff4da6; }
.ins-title-blue { color: #4dc3ff; }
.ins-title-green { color: #39ff14; }
.hl { font-weight: 700; color: #dce8ff; }

/* Tables */
.custom-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.custom-table thead tr {
    background: rgba(184,77,255,0.12);
    border-bottom: 1px solid rgba(180,77,255,0.35);
}
.custom-table thead th {
    padding: 13px 16px; text-align: left; font-size: 11px; font-weight: 700;
    color: #b84dff; letter-spacing: 0.8px; text-transform: uppercase; white-space: nowrap;
}
.custom-table tbody tr {
    border-bottom: 1px solid rgba(77,195,255,0.07);
    transition: background 0.15s;
}
.custom-table tbody tr:hover { background: rgba(184,77,255,0.07); }
.custom-table tbody td { padding: 12px 16px; color: #aabdd8; vertical-align: middle; }
.td-name { color: #dce8ff !important; font-weight: 600; }
.td-badge {
    display: inline-block; padding: 3px 10px; border-radius: 12px;
    font-size: 10px; font-weight: 700; letter-spacing: 0.3px;
}
.badge-electronics { background: rgba(77,195,255,0.15); color: #4dc3ff; border: 1px solid rgba(77,195,255,0.3); }
.badge-toys { background: rgba(255,77,166,0.15); color: #ff4da6; border: 1px solid rgba(255,77,166,0.3); }
.badge-arts { background: rgba(184,77,255,0.15); color: #b84dff; border: 1px solid rgba(184,77,255,0.3); }
.badge-games { background: rgba(57,255,20,0.12); color: #39ff14; border: 1px solid rgba(57,255,20,0.3); }
.badge-sports { background: rgba(255,170,0,0.15); color: #ffaa00; border: 1px solid rgba(255,170,0,0.3); }
.bar-mini {
    height: 6px; border-radius: 3px;
    background: linear-gradient(90deg, #b84dff, #ff4da6);
    box-shadow: 0 0 6px rgba(255,77,166,0.5);
}
.bar-mini-blue {
    height: 6px; border-radius: 3px;
    background: linear-gradient(90deg, #4dc3ff, #b84dff);
    box-shadow: 0 0 6px rgba(77,195,255,0.5);
}

/* Selectbox / Multiselect styling */
div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label {
    color: #7a9abf !important; font-size: 12px !important; font-weight: 600 !important;
    letter-spacing: 0.5px; text-transform: uppercase;
}
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stMultiSelect"] > div > div {
    background: rgba(14, 30, 65, 0.6) !important;
    border: 1px solid rgba(77,195,255,0.2) !important;
    border-radius: 10px !important;
    color: #aabdd8 !important;
}

/* Plotly chart background */
.stPlotlyChart { background: transparent !important; }

/* Streamlit elements color fix */
.stMarkdown, p, span, label { color: #dce8ff; }
hr { border-color: rgba(77,195,255,0.15) !important; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA LOADING
# ============================================================
@st.cache_data
def load_data():
    # 1. Load Raw Tables
    sales = pd.read_csv("sales.csv").dropna()
    products = pd.read_csv("products.csv").dropna()
    stores = pd.read_csv("stores.csv").dropna()
    inventory = pd.read_csv("inventory.csv").dropna()
    
    # 2. Clean Products
    products['Product_Cost'] = products['Product_Cost'].replace(r'[\$,\s]', '', regex=True).astype(float)
    products['Product_Price'] = products['Product_Price'].replace(r'[\$,\s]', '', regex=True).astype(float)
    
    # 3. Create Main Merged DataFrame (df)
    df = sales.merge(products, on='Product_ID', how='left').merge(stores, on='Store_ID', how='left')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Revenue'] = df['Units'] * df['Product_Price']
    df['Profit'] = df['Units'] * (df['Product_Price'] - df['Product_Cost'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    # 4. Create Inventory DataFrame (inv)
    inv = inventory.merge(products, on='Product_ID', how='left').merge(stores, on='Store_ID', how='left')
    inv['Inv_Value'] = inv['Stock_On_Hand'] * inv['Product_Cost']
    
    return df, products, stores, inventory, inv

df, products, stores, inventory, inv = load_data()

# ============================================================
# PLOTLY THEME & HELPERS
# ============================================================
NEON = dict(pink='#ff4da6', purple='#b84dff', blue='#4dc3ff', green='#39ff14', orange='#ffaa00')

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
    font=dict(family='Inter, Segoe UI, sans-serif', color='#c0d0e8', size=11),
    margin=dict(l=50, r=30, t=30, b=50),
)

DEFAULT_AXIS = dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11), zeroline=False)

def apply_layout(fig, height=300, **kwargs):
    """Apply standard layout + default axes with optional overrides."""
    xaxis_kw = {**DEFAULT_AXIS, **kwargs.pop('xaxis', {})}
    yaxis_kw = {**DEFAULT_AXIS, **kwargs.pop('yaxis', {})}
    legend_default = dict(font=dict(size=11, color='#c0d0e8'), bgcolor='rgba(0,0,0,0)')
    legend_kw = {**legend_default, **kwargs.pop('legend', {})}
    fig.update_layout(**PLOTLY_LAYOUT, height=height, xaxis=xaxis_kw, yaxis=yaxis_kw, legend=legend_kw, **kwargs)

def fmt(n):
    if n >= 1e6: return f"${n/1e6:.2f}M"
    elif n >= 1e3: return f"${n/1e3:.1f}K"
    else: return f"${n:.0f}"

def hex_rgba(hex_color, alpha=1.0):
    """Convert hex color to rgba string for Plotly compatibility."""
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f'rgba({r},{g},{b},{alpha})'

def show_chart(fig, key=None):
    """Helper to display plotly chart with stretch width."""
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
      <div class="logo-sub">Business Analytics Dashboard &nbsp;|&nbsp; ITS Statistika 2026</div>
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
tab1, tab2, tab3 = st.tabs(["📊 Overview & Profitabilitas", "📦 Inventory & Stockout", "🔄 Data Pipeline"])

# ============================================================
# TAB 1: OVERVIEW & PROFITABILITAS
# ============================================================
with tab1:
    st.markdown("""
    <div style="margin-bottom:22px;">
        <div class="page-title">Sales Performance Overview <span class="tag">2022 - 2023</span></div>
        <div class="page-desc">Descriptive & Diagnostic Analytics — Profitabilitas kategori produk, tren temporal, dan performa toko.</div>
    </div>
    """, unsafe_allow_html=True)

    # FILTERS
    fc1, fc2 = st.columns([1, 2])
    with fc1:
        year_filter = st.selectbox("TAHUN", ["Semua", 2022, 2023], key="year_f")
    with fc2:
        loc_filter = st.selectbox("LOKASI", ["Semua", "Downtown", "Commercial", "Airport", "Residential"], key="loc_f")

    dff = df.copy()
    if year_filter != "Semua":
        dff = dff[dff['Year'] == int(year_filter)]
    if loc_filter != "Semua":
        dff = dff[dff['Store_Location'] == loc_filter]

    # KPIs
    total_rev = dff['Revenue'].sum()
    total_prof = dff['Profit'].sum()
    total_units = int(dff['Units'].sum())
    avg_margin = (total_prof / total_rev * 100) if total_rev > 0 else 0

    st.markdown('<div class="section-title">Key Performance Indicators</div>', unsafe_allow_html=True)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-pink"></div>
        <div class="kpi-icon">$</div><div class="kpi-label">Total Revenue</div>
        <div class="kpi-value" style="color:#ff4da6;">{fmt(total_rev)}</div>
        <div class="kpi-sub">Jan 2022 - Sep 2023</div></div>''', unsafe_allow_html=True)
    with k2:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-purple"></div>
        <div class="kpi-icon">P</div><div class="kpi-label">Total Profit</div>
        <div class="kpi-value" style="color:#b84dff;">{fmt(total_prof)}</div>
        <div class="kpi-sub">Gross profit keseluruhan</div></div>''', unsafe_allow_html=True)
    with k3:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-blue"></div>
        <div class="kpi-icon">U</div><div class="kpi-label">Total Units Terjual</div>
        <div class="kpi-value" style="color:#4dc3ff;">{total_units:,}</div>
        <div class="kpi-sub">Seluruh toko & produk</div></div>''', unsafe_allow_html=True)
    with k4:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-green"></div>
        <div class="kpi-icon">%</div><div class="kpi-label">Avg. Profit Margin</div>
        <div class="kpi-value" style="color:#39ff14;">{avg_margin:.1f}%</div>
        <div class="kpi-sub">Rata-rata seluruh transaksi</div></div>''', unsafe_allow_html=True)

    st.write("")

    # ── CHART ROW 1: Profit per Category & Margin per Category ──
    cat_data = dff.groupby('Product_Category').agg(
        Revenue=('Revenue','sum'), Profit=('Profit','sum'), Units=('Units','sum')
    ).reset_index()
    cat_data['Margin'] = cat_data['Profit'] / cat_data['Revenue'] * 100
    cat_data = cat_data.sort_values('Profit', ascending=False)

    cr1, cr2 = st.columns(2)

    with cr1:
        st.markdown('''<div class="chart-card"><div class="chart-title">Profit per Kategori Produk</div>
        <div class="chart-sub">Diagnosa: Kategori mana yang mendorong profit terbesar?</div></div>''', unsafe_allow_html=True)

        colors_list = [CAT_COLORS.get(c, NEON['blue']) for c in cat_data['Product_Category']]
        fig = go.Figure(go.Bar(
            x=cat_data['Product_Category'], y=cat_data['Profit'],
            marker=dict(
                color=[hex_rgba(c, 0.73) for c in colors_list],
                line=dict(width=1.5, color=colors_list),
            ),
            text=[fmt(v) for v in cat_data['Profit']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=10),
            hovertemplate='<b>%{x}</b><br>Profit: %{text}<br>Units: ' +
                          '<br>'.join(['']*len(cat_data)) + '<extra></extra>',
        ))
        apply_layout(fig, height=300, showlegend=False, bargap=0.35,
                         yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                   zeroline=False, tickformat='$,.0f'))
        show_chart(fig, key='cat_profit')

    with cr2:
        st.markdown('''<div class="chart-card"><div class="chart-title">Margin Profit per Kategori (%)</div>
        <div class="chart-sub">Diagnosa: Efisiensi profitabilitas per kategori</div></div>''', unsafe_allow_html=True)

        margin_colors = []
        margin_borders = []
        for m in cat_data['Margin']:
            if m >= 40:
                margin_colors.append(hex_rgba(NEON['green'], 0.8))
                margin_borders.append(NEON['green'])
            elif m >= 30:
                margin_colors.append(hex_rgba(NEON['purple'], 0.73))
                margin_borders.append(NEON['purple'])
            else:
                margin_colors.append(hex_rgba(NEON['blue'], 0.53))
                margin_borders.append(NEON['blue'])

        fig2 = go.Figure(go.Bar(
            x=cat_data['Product_Category'], y=cat_data['Margin'],
            marker=dict(color=margin_colors,
                       line=dict(width=1.5, color=margin_borders)),
            text=[f"{v:.1f}%" for v in cat_data['Margin']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=10),
            hovertemplate='<b>%{x}</b><br>Margin: %{y:.1f}%<extra></extra>',
        ))
        fig2.add_hline(y=avg_margin, line_dash="dash", line_color=NEON['pink'], line_width=2,
                      annotation_text=f"Avg: {avg_margin:.1f}%",
                      annotation_font=dict(color=NEON['pink'], size=11),
                      annotation_position="right")
        apply_layout(fig2, height=300, showlegend=False, bargap=0.35,
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                    zeroline=False, ticksuffix='%', range=[0, max(cat_data['Margin'])*1.25]))
        show_chart(fig2, key='cat_margin')

    # ── CHART ROW 2: Monthly Trend ──
    st.markdown('''<div class="chart-card"><div class="chart-title">Tren Revenue & Profit Bulanan</div>
    <div class="chart-sub">Diagnosa: Pola seasonal — Penjualan tertinggi terjadi pada periode apa?</div></div>''', unsafe_allow_html=True)
    monthly = dff.groupby('YearMonth').agg(Revenue=('Revenue','sum'), Profit=('Profit','sum')).reset_index()
    monthly = monthly.sort_values('YearMonth')

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Revenue'], name='Revenue',
        line=dict(color=NEON['blue'], width=2.5, shape='spline'),
        fill='tozeroy', fillcolor='rgba(77,195,255,0.10)',
        mode='lines+markers', marker=dict(size=5, color=NEON['blue'], line=dict(width=1, color='#fff')),
        hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>',
    ))
    fig3.add_trace(go.Scatter(
        x=monthly['YearMonth'], y=monthly['Profit'], name='Profit',
        line=dict(color=NEON['pink'], width=2.5, shape='spline'),
        fill='tozeroy', fillcolor='rgba(255,77,166,0.10)',
        mode='lines+markers', marker=dict(size=5, color=NEON['pink'], line=dict(width=1, color='#fff')),
        hovertemplate='<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>',
    ))
    apply_layout(fig3, height=250,
                      xaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                zeroline=False, tickangle=-45),
                      yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                zeroline=False, tickformat='$,.0f'),
                      legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1,
                                 font=dict(size=11, color='#c0d0e8'), bgcolor='rgba(0,0,0,0)'),
                      hovermode='x unified')
    show_chart(fig3, key='monthly_trend')

    # ── CHART ROW 3: Location, City Top 10, Quarterly ──
    c31, c32, c33 = st.columns(3)

    with c31:
        st.markdown('''<div class="chart-card"><div class="chart-title">Revenue per Lokasi Toko</div>
        <div class="chart-sub">Distribusi revenue berdasarkan tipe lokasi</div></div>''', unsafe_allow_html=True)
        loc_data = dff.groupby('Store_Location')['Revenue'].sum().reset_index()
        loc_data = loc_data.sort_values('Revenue', ascending=False)

        loc_colors_map = {'Airport': NEON['blue'], 'Commercial': NEON['purple'],
                         'Downtown': NEON['pink'], 'Residential': NEON['green']}
        loc_c = [loc_colors_map.get(l, NEON['blue']) for l in loc_data['Store_Location']]

        fig4 = go.Figure(go.Pie(
            labels=loc_data['Store_Location'], values=loc_data['Revenue'],
            hole=0.55,
            marker=dict(colors=loc_c, line=dict(color=loc_c, width=2)),
            textfont=dict(color='#dce8ff', size=11),
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>Share: %{percent}<extra></extra>',
            pull=[0.03 if i == 0 else 0 for i in range(len(loc_data))],
        ))
        fig4.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter, sans-serif', color='#c0d0e8', size=11),
            margin=dict(l=10, r=10, t=20, b=20),
            height=320, showlegend=False,
        )
        show_chart(fig4, key='loc_donut')

    with c32:
        st.markdown('''<div class="chart-card"><div class="chart-title">Revenue per Kota (Top 10)</div>
        <div class="chart-sub">Kota dengan kontribusi tertinggi</div></div>''', unsafe_allow_html=True)
        city_data = dff.groupby('Store_City')['Revenue'].sum().nlargest(10).reset_index()
        city_data = city_data.sort_values('Revenue', ascending=True)

        # Gradient colors from dim to bright
        n_bars = len(city_data)
        grad_colors = [f'rgba(57,255,20,{0.3 + 0.7*(i/max(n_bars-1,1))})' for i in range(n_bars)]

        fig5 = go.Figure(go.Bar(
            y=city_data['Store_City'], x=city_data['Revenue'],
            orientation='h',
            marker=dict(color=grad_colors, line=dict(width=1, color=NEON['green'])),
            text=[fmt(v) for v in city_data['Revenue']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=9),
            hovertemplate='<b>%{y}</b><br>Revenue: $%{x:,.0f}<extra></extra>',
        ))
        apply_layout(fig5, height=320, showlegend=False, bargap=0.25,
                          xaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                    zeroline=False, tickformat='$,.0f'),
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#c0d0e8', size=10),
                                    zeroline=False))
        show_chart(fig5, key='city_rev')

    with c33:
        st.markdown('''<div class="chart-card"><div class="chart-title">Revenue per Kuartal</div>
        <div class="chart-sub">Tren kuartalan 2022 vs 2023</div></div>''', unsafe_allow_html=True)
        qdata = dff.groupby(['Year','Quarter']).agg(Revenue=('Revenue','sum'), Profit=('Profit','sum')).reset_index()
        qdata['Label'] = qdata.apply(lambda r: f"Q{int(r['Quarter'])} {int(r['Year'])}", axis=1)

        fig6 = go.Figure()
        fig6.add_trace(go.Bar(
            x=qdata['Label'], y=qdata['Revenue'], name='Revenue',
            marker=dict(color=hex_rgba(NEON['purple'], 0.73), line=dict(width=1.5, color=NEON['purple'])),
            hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>',
        ))
        fig6.add_trace(go.Bar(
            x=qdata['Label'], y=qdata['Profit'], name='Profit',
            marker=dict(color=hex_rgba(NEON['pink'], 0.73), line=dict(width=1.5, color=NEON['pink'])),
            hovertemplate='<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>',
        ))
        apply_layout(fig6, height=320, barmode='group', bargap=0.3,
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                    zeroline=False, tickformat='$,.0f'),
                          xaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                    zeroline=False, tickangle=-30),
                          legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1,
                                     font=dict(size=10, color='#c0d0e8'), bgcolor='rgba(0,0,0,0)'))
        show_chart(fig6, key='quarterly')

    # ── INSIGHTS ──
    st.markdown('<div class="section-title">Diagnostic Insights — Profitabilitas & Seasonal</div>', unsafe_allow_html=True)
    i1, i2 = st.columns(2)
    with i1:
        st.markdown('''<div class="insight-box insight-pink">
        <div class="ins-title ins-title-pink">Kategori Produk Dominan</div>
        <span class="hl">Electronics</span> memiliki margin tertinggi (44.6%), meskipun revenue totalnya berada di urutan ke-3.
        <span class="hl">Toys</span> menghasilkan profit nominal terbesar ($1.08M) karena volume penjualan tinggi.
        Pola dominasi ini konsisten di seluruh lokasi toko.</div>''', unsafe_allow_html=True)
    with i2:
        st.markdown('''<div class="insight-box insight-purple">
        <div class="ins-title ins-title-purple">Pola Seasonal</div>
        Revenue mencapai puncak pada <span class="hl">April–Mei dan November–Desember</span>, mengindikasikan pola holiday season.
        Q4 2022 dan Q2 2023 merupakan kuartal paling menguntungkan. Perlu strategi stok proaktif menjelang periode tersebut.</div>''', unsafe_allow_html=True)
    i3, i4 = st.columns(2)
    with i3:
        st.markdown('''<div class="insight-box insight-blue">
        <div class="ins-title ins-title-blue">Performa Lokasi Toko</div>
        <span class="hl">Downtown</span> mendominasi dengan 56.9% dari total revenue ($8.2M). Toko di Airport memiliki margin lebih tinggi
        meski volume transaksinya lebih rendah. Uji ANOVA menunjukkan perbedaan revenue antar lokasi sangat signifikan (p &lt; 0.001).</div>''', unsafe_allow_html=True)
    with i4:
        st.markdown('''<div class="insight-box insight-green">
        <div class="ins-title ins-title-green">Rekomendasi Strategis</div>
        Fokuskan margin pada <span class="hl">Electronics</span> dengan promosi bundling. Alokasikan inventory lebih besar menjelang
        April dan November. Evaluasi harga produk Sports & Outdoors yang memiliki margin terendah (23.3%).</div>''', unsafe_allow_html=True)

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
        <td style="color:#7a9abf;font-size:12px;">{i}</td>
        <td class="td-name">{r.Product_Name}</td>
        <td><span class="td-badge {badge_cls}">{r.Product_Category}</span></td>
        <td>{fmt(r.Revenue)}</td>
        <td style="color:#ff4da6;font-weight:700;">{fmt(r.Profit)}</td>
        <td>{r.Units:,}</td>
        <td style="color:#39ff14;">{margin:.1f}%</td>
        <td style="width:100px;"><div class="bar-mini" style="width:{bw:.1f}%"></div></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:10px;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Nama Produk</th><th>Kategori</th><th>Total Revenue (USD)</th>
    <th>Total Profit (USD)</th><th>Units Terjual</th><th>Margin</th><th>Profit Bar</th>
    </tr></thead><tbody>{rows_html}</tbody></table></div></div>""", unsafe_allow_html=True)


# ============================================================
# TAB 2: INVENTORY & STOCKOUT
# ============================================================
with tab2:
    st.markdown("""
    <div style="margin-bottom:22px;">
        <div class="page-title">Inventory & Stockout Analysis <span class="tag">Diagnostic</span></div>
        <div class="page-desc">Berapa nilai inventori yang terikat? Toko mana yang mengalami stockout? Berapa potensi kehilangan penjualan?</div>
    </div>
    """, unsafe_allow_html=True)

    # FILTERS PAGE 2
    fc21, fc22 = st.columns([1, 1])
    with fc21:
        cat_filter2 = st.selectbox("KATEGORI", ["Semua"] + sorted(inv['Product_Category'].unique().tolist()), key="cat_f2")
    with fc22:
        dos_filter = st.selectbox("THRESHOLD DoS", ["Semua", "Kritis (<7 hari)", "Rendah (<30 hari)"], key="dos_f")

    # Calculate avg daily sales per store-product
    # Use total calendar period (not just days with sales) for accurate avg daily rate
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

    # KPIs
    total_inv_val = inv2['Inv_Value'].sum()
    stockout_count = int((inv2['Stock_On_Hand'] == 0).sum())
    valid_dos = inv2['DoS'].dropna()
    median_dos = valid_dos.median() if len(valid_dos) > 0 else 0
    critical_count = int((valid_dos < 7).sum())

    st.markdown('<div class="section-title">Inventory Key Metrics</div>', unsafe_allow_html=True)
    ik1, ik2, ik3, ik4 = st.columns(4)
    with ik1:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-blue"></div>
        <div class="kpi-icon">$</div><div class="kpi-label">Nilai Inventori (at Cost)</div>
        <div class="kpi-value" style="color:#4dc3ff;">{fmt(total_inv_val)}</div>
        <div class="kpi-sub">Total dana terikat di stok</div></div>''', unsafe_allow_html=True)
    with ik2:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-pink"></div>
        <div class="kpi-icon">!</div><div class="kpi-label">Kombinasi Stockout</div>
        <div class="kpi-value" style="color:#ff4da6;">{stockout_count}</div>
        <div class="kpi-sub">Store-Product dengan stok = 0</div></div>''', unsafe_allow_html=True)
    with ik3:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-purple"></div>
        <div class="kpi-icon">D</div><div class="kpi-label">Median Days of Supply</div>
        <div class="kpi-value" style="color:#b84dff;">{median_dos:.1f} hari</div>
        <div class="kpi-sub">Rata-rata ketahanan stok</div></div>''', unsafe_allow_html=True)
    with ik4:
        st.markdown(f'''<div class="kpi-card"><div class="kpi-bar-green"></div>
        <div class="kpi-icon">W</div><div class="kpi-label">Produk Stok Kritis</div>
        <div class="kpi-value" style="color:#39ff14;">{critical_count}</div>
        <div class="kpi-sub">Kombinasi dengan DoS &lt; 7 hari</div></div>''', unsafe_allow_html=True)

    st.write("")

    # ── CHART ROW: Inv per Category & Stockout per Location ──
    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown('''<div class="chart-card"><div class="chart-title">Nilai Inventori per Kategori (USD)</div>
        <div class="chart-sub">Diagnosa: Dana terikat paling besar di kategori mana?</div></div>''', unsafe_allow_html=True)
        inv_cat = inv2.groupby('Product_Category')['Inv_Value'].sum().reset_index()
        inv_cat = inv_cat.sort_values('Inv_Value', ascending=False)
        inv_colors = [hex_rgba(CAT_COLORS.get(c, NEON['blue']), 0.73) for c in inv_cat['Product_Category']]
        inv_borders = [CAT_COLORS.get(c, NEON['blue']) for c in inv_cat['Product_Category']]

        fig7 = go.Figure(go.Bar(
            x=inv_cat['Product_Category'], y=inv_cat['Inv_Value'],
            marker=dict(color=inv_colors, line=dict(width=1.5, color=inv_borders)),
            text=[f"${v:,.0f}" for v in inv_cat['Inv_Value']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=10),
            hovertemplate='<b>%{x}</b><br>Inventory Value: $%{y:,.0f}<extra></extra>',
        ))
        apply_layout(fig7, height=300, showlegend=False, bargap=0.35,
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                    zeroline=False, tickformat='$,.0f'))
        show_chart(fig7, key='inv_cat')

    with cc2:
        st.markdown('''<div class="chart-card"><div class="chart-title">Stockout per Lokasi Toko</div>
        <div class="chart-sub">Diagnosa: Lokasi toko mana yang paling banyak mengalami stockout?</div></div>''', unsafe_allow_html=True)
        stockout_loc = inv2[inv2['Stock_On_Hand'] == 0].groupby('Store_Location').size().reset_index(name='count')
        stockout_loc = stockout_loc.sort_values('count', ascending=False)

        so_loc_colors = {'Airport': NEON['blue'], 'Commercial': NEON['purple'],
                        'Downtown': NEON['pink'], 'Residential': NEON['green']}
        so_c = [hex_rgba(so_loc_colors.get(l, NEON['blue']), 0.73) for l in stockout_loc['Store_Location']]
        so_b = [so_loc_colors.get(l, NEON['blue']) for l in stockout_loc['Store_Location']]

        fig8 = go.Figure(go.Bar(
            x=stockout_loc['Store_Location'], y=stockout_loc['count'],
            marker=dict(color=so_c, line=dict(width=1.5, color=so_b)),
            text=stockout_loc['count'],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=11),
            hovertemplate='<b>%{x}</b><br>Stockout Count: %{y}<extra></extra>',
        ))
        apply_layout(fig8, height=300, showlegend=False, bargap=0.35,
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                    zeroline=False))
        show_chart(fig8, key='stockout_loc')

    # ── CHART ROW 2: Inv per City & DoS Distribution ──
    cc3, cc4 = st.columns(2)
    with cc3:
        st.markdown('''<div class="chart-card"><div class="chart-title">Top 10 Kota: Nilai Inventori (USD)</div>
        <div class="chart-sub">Distribusi nilai inventori antar kota</div></div>''', unsafe_allow_html=True)
        inv_city = inv2.groupby('Store_City')['Inv_Value'].sum().nlargest(10).reset_index()
        inv_city = inv_city.sort_values('Inv_Value', ascending=True)

        n_city = len(inv_city)
        city_grad = [f'rgba(77,195,255,{0.3 + 0.7*(i/max(n_city-1,1))})' for i in range(n_city)]

        fig9 = go.Figure(go.Bar(
            y=inv_city['Store_City'], x=inv_city['Inv_Value'], orientation='h',
            marker=dict(color=city_grad, line=dict(width=1, color=NEON['blue'])),
            text=[f"${v:,.0f}" for v in inv_city['Inv_Value']],
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=9),
            hovertemplate='<b>%{y}</b><br>Inventory Value: $%{x:,.0f}<extra></extra>',
        ))
        apply_layout(fig9, height=300, showlegend=False,
                          xaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                    zeroline=False, tickformat='$,.0f'),
                          yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#c0d0e8', size=10),
                                    zeroline=False))
        show_chart(fig9, key='inv_city')

    with cc4:
        st.markdown('''<div class="chart-card"><div class="chart-title">Distribusi Days of Supply</div>
        <div class="chart-sub">Sebaran ketahanan stok per Store-Product (capped 180 hari)</div></div>''', unsafe_allow_html=True)
        dos_vals = inv2['DoS'].dropna()
        dos_capped = dos_vals.clip(upper=180)
        bins_edges = [0, 10, 20, 30, 40, 50, 60, 80, 100, 120, 150, 180]
        counts_h, _ = np.histogram(dos_capped, bins=bins_edges)
        bin_labels = [f"{bins_edges[i]}-{bins_edges[i+1]}" for i in range(len(bins_edges)-1)]

        # Color by risk level
        bar_colors_dos = []
        bar_borders_dos = []
        for i in range(len(counts_h)):
            if i < 1:
                bar_colors_dos.append(hex_rgba(NEON['pink'], 0.87))
                bar_borders_dos.append(NEON['pink'])
            elif i < 3:
                bar_colors_dos.append(hex_rgba(NEON['orange'], 0.73))
                bar_borders_dos.append(NEON['orange'])
            elif i < 5:
                bar_colors_dos.append(hex_rgba(NEON['purple'], 0.6))
                bar_borders_dos.append(NEON['purple'])
            else:
                bar_colors_dos.append(hex_rgba(NEON['blue'], 0.47))
                bar_borders_dos.append(NEON['blue'])

        fig10 = go.Figure(go.Bar(
            x=bin_labels, y=counts_h,
            marker=dict(color=bar_colors_dos, line=dict(width=1.5, color=bar_borders_dos)),
            text=counts_h,
            textposition='outside',
            textfont=dict(color='#c0d0e8', size=10),
            hovertemplate='<b>DoS %{x} hari</b><br>Frekuensi: %{y} kombinasi<extra></extra>',
        ))
        # Add critical threshold line
        fig10.add_vline(x=0.5, line_dash="dash", line_color=NEON['pink'], line_width=1.5,
                       annotation_text="Kritis", annotation_font=dict(color=NEON['pink'], size=9),
                       annotation_position="top")
        apply_layout(fig10, height=300, showlegend=False,
                           xaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=10),
                                     zeroline=False, title=dict(text='Days of Supply', font=dict(color='#7a9abf', size=11))),
                           yaxis=dict(gridcolor='rgba(30,58,95,0.6)', tickfont=dict(color='#7a9abf', size=11),
                                     zeroline=False, title=dict(text='Frekuensi', font=dict(color='#7a9abf', size=11))))
        show_chart(fig10, key='dos_dist')

    # ── INSIGHTS PAGE 2 ──
    st.markdown('<div class="section-title">Diagnostic Insights — Inventory & Stockout</div>', unsafe_allow_html=True)
    ii1, ii2 = st.columns(2)
    with ii1:
        st.markdown(f'''<div class="insight-box insight-pink">
        <div class="ins-title ins-title-pink">Risiko Stockout</div>
        Terdapat <span class="hl">{stockout_count} kombinasi store-product</span> dengan stok habis. Produk
        <span class="hl">Colorbuds (Electronics)</span> paling sering mengalami stockout padahal merupakan produk dengan
        profit tertinggi — potensi kerugian signifikan.</div>''', unsafe_allow_html=True)
    with ii2:
        st.markdown(f'''<div class="insight-box insight-purple">
        <div class="ins-title ins-title-purple">Ketahanan Stok</div>
        Median Days of Supply sebesar <span class="hl">{median_dos:.1f} hari</span> mengindikasikan rotasi stok yang cukup baik.
        Namun, <span class="hl">{critical_count} kombinasi</span> store-product memiliki DoS di bawah 7 hari — perlu reorder segera.</div>''', unsafe_allow_html=True)
    ii3, ii4 = st.columns(2)
    with ii3:
        st.markdown(f'''<div class="insight-box insight-blue">
        <div class="ins-title ins-title-blue">Dana Terikat di Inventori</div>
        Total <span class="hl">{fmt(total_inv_val)}</span> dana terikat dalam inventori (at cost). Kategori <span class="hl">Toys</span>
        mendominasi nilai inventori karena volume stok tertinggi, namun margin-nya paling rendah — indikasi over-stocking.</div>''', unsafe_allow_html=True)
    with ii4:
        st.markdown('''<div class="insight-box insight-green">
        <div class="ins-title ins-title-green">Rekomendasi Operasional</div>
        Terapkan <span class="hl">reorder point otomatis</span> saat DoS &lt; 14 hari. Prioritaskan restock untuk Electronics (margin tinggi).
        Tinjau kebijakan safety stock di toko Downtown. Kurangi over-stock Toys di lokasi Residential.</div>''', unsafe_allow_html=True)

    st.write("")

    # ── STORE TABLE ──
    st.markdown('<div class="section-title">Performa 15 Toko Teratas</div>', unsafe_allow_html=True)
    store_perf = df.groupby(['Store_Name','Store_City','Store_Location']).agg(
        Revenue=('Revenue','sum'), Profit=('Profit','sum'), Units=('Units','sum')
    ).reset_index()
    store_perf['Margin'] = store_perf['Profit'] / store_perf['Revenue']
    top_stores = store_perf.nlargest(15, 'Revenue')
    max_r = top_stores['Revenue'].max()
    loc_color_map = {'Airport':'#4dc3ff','Commercial':'#b84dff','Downtown':'#ff4da6','Residential':'#39ff14'}

    srows = ""
    for i, r in enumerate(top_stores.itertuples(), 1):
        lc = loc_color_map.get(r.Store_Location, '#4dc3ff')
        bw = (r.Revenue/max_r*100)
        srows += f"""<tr>
        <td style="color:#7a9abf;font-size:12px;">{i}</td>
        <td class="td-name">{r.Store_Name}</td><td>{r.Store_City}</td>
        <td><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:10px;font-weight:700;
            background:{lc}22;color:{lc};border:1px solid {lc}55;">{r.Store_Location}</span></td>
        <td style="color:#4dc3ff;font-weight:700;">{fmt(r.Revenue)}</td>
        <td style="color:#ff4da6;">{fmt(r.Profit)}</td>
        <td>{int(r.Units):,}</td>
        <td style="color:#39ff14;">{r.Margin*100:.1f}%</td>
        <td style="width:100px;"><div class="bar-mini-blue" style="width:{bw:.1f}%"></div></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:10px;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Nama Toko</th><th>Kota</th><th>Lokasi</th>
    <th>Revenue (USD)</th><th>Profit (USD)</th><th>Units</th><th>Margin</th><th>Revenue Bar</th>
    </tr></thead><tbody>{srows}</tbody></table></div></div>""", unsafe_allow_html=True)


# ============================================================
# TAB 3: DATA PIPELINE
# ============================================================
with tab3:
    st.markdown("""
    <div style="margin-bottom:22px;">
        <div class="page-title">Data Pipeline <span class="tag">ETL Process</span></div>
        <div class="page-desc">Visualisasi alur pemrosesan data dari sumber mentah hingga siap analisis — Extract, Transform, Load.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── PIPELINE FLOW DIAGRAM ──
    st.markdown('<div class="section-title">Pipeline Architecture</div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    .pipe-flow {
        display: flex; align-items: center; justify-content: center;
        gap: 0; flex-wrap: wrap; margin-bottom: 28px;
    }
    .pipe-node {
        background: rgba(14, 30, 65, 0.7);
        border-radius: 12px; padding: 16px 20px;
        text-align: center; min-width: 140px;
        transition: border-color 0.25s, transform 0.2s;
    }
    .pipe-node:hover { transform: translateY(-3px); }
    .pipe-node-extract { border: 1.5px solid #4dc3ff; }
    .pipe-node-transform { border: 1.5px solid #b84dff; }
    .pipe-node-load { border: 1.5px solid #39ff14; }
    .pipe-node-analyze { border: 1.5px solid #ff4da6; }
    .pipe-label {
        font-size: 9px; font-weight: 700; letter-spacing: 1.2px;
        text-transform: uppercase; margin-bottom: 6px;
    }
    .pipe-label-blue { color: #4dc3ff; }
    .pipe-label-purple { color: #b84dff; }
    .pipe-label-green { color: #39ff14; }
    .pipe-label-pink { color: #ff4da6; }
    .pipe-icon { font-size: 22px; margin-bottom: 6px; }
    .pipe-desc { font-size: 11px; color: #aabdd8; line-height: 1.4; }
    .pipe-arrow {
        font-size: 20px; color: #7a9abf; padding: 0 8px;
        animation: arrowPulse 1.5s ease-in-out infinite;
    }
    @keyframes arrowPulse { 0%,100%{opacity:0.4} 50%{opacity:1} }
    </style>

    <div class="pipe-flow">
        <div class="pipe-node pipe-node-extract">
            <div class="pipe-label pipe-label-blue">Extract</div>
            <div class="pipe-icon">📂</div>
            <div class="pipe-desc">4 file CSV<br>sumber data mentah</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-transform">
            <div class="pipe-label pipe-label-purple">Clean</div>
            <div class="pipe-icon">🧹</div>
            <div class="pipe-desc">Parsing harga,<br>konversi tipe data</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-transform">
            <div class="pipe-label pipe-label-purple">Merge</div>
            <div class="pipe-icon">🔗</div>
            <div class="pipe-desc">Join tabel via<br>Product_ID & Store_ID</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-load">
            <div class="pipe-label pipe-label-green">Engineer</div>
            <div class="pipe-icon">⚙️</div>
            <div class="pipe-desc">Revenue, Profit,<br>Margin, DoS</div>
        </div>
        <div class="pipe-arrow">→</div>
        <div class="pipe-node pipe-node-analyze">
            <div class="pipe-label pipe-label-pink">Analyze</div>
            <div class="pipe-icon">📊</div>
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
        <td class="td-name">📄 {fname}</td>
        <td>{desc}</td>
        <td style="color:#4dc3ff;font-weight:700;">{rows:,}</td>
        <td>{cols}</td>
        <td style="font-size:11px;color:#7a9abf;">{columns}</td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:10px;">
    <table class="custom-table"><thead><tr>
    <th>File</th><th>Deskripsi</th><th>Baris</th><th>Kolom</th><th>Kolom Utama</th>
    </tr></thead><tbody>{src_rows}</tbody></table></div></div>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-box insight-blue" style="margin-top:12px;">
        <div class="ins-title ins-title-blue">Ringkasan Extract</div>
        Total <span class="hl">{total_raw_rows:,}</span> baris data mentah dari <span class="hl">4 file CSV</span>.
        Dataset utama adalah <span class="hl">merged_sales_data.csv</span> ({len(df):,} baris) yang sudah di-pre-merge.
        Sumber data asli: <span class="hl">Maven Analytics — Maven Toys Dataset (Kaggle)</span>.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 2: TRANSFORM (CLEAN) ──
    st.markdown('<div class="section-title">Step 2 — Transform (Pembersihan Data)</div>', unsafe_allow_html=True)

    clean_steps = [
        ("1", "Parsing Harga", "Menghapus simbol <code>$</code> dan spasi dari kolom Product_Cost & Product_Price",
         "<code>'$9.99 ' → 9.99</code>", "#ff4da6"),
        ("2", "Konversi Tanggal", "Mengubah kolom Date dari string ke tipe datetime",
         "<code>'2022-01-01' → Timestamp</code>", "#b84dff"),
        ("3", "Handling Missing", "Mengecek dan menangani nilai null pada semua kolom",
         f"<code>Null count: {df.isnull().sum().sum()}</code>", "#4dc3ff"),
        ("4", "Validasi Tipe Data", "Memastikan kolom numerik bertipe float/int, kategorikal bertipe object",
         "<code>Units: int64, Revenue: float64</code>", "#39ff14"),
    ]

    for step_num, title, desc, example, color in clean_steps:
        st.markdown(f"""
        <div class="chart-card" style="padding:14px 20px; margin-bottom:10px; border-left: 3px solid {color};">
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="min-width:32px;height:32px;border-radius:8px;background:{color}22;
                     display:flex;align-items:center;justify-content:center;
                     font-weight:800;color:{color};font-size:14px;border:1px solid {color}55;">{step_num}</div>
                <div style="flex:1;">
                    <div style="font-size:13px;font-weight:700;color:#dce8ff;margin-bottom:2px;">{title}</div>
                    <div style="font-size:11.5px;color:#aabdd8;">{desc}</div>
                </div>
                <div style="font-size:11px;color:#7a9abf;text-align:right;">{example}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 3: MERGE / JOIN ──
    st.markdown('<div class="section-title">Step 3 — Merge (Penggabungan Tabel)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card" style="text-align:center; padding:24px;">
        <div style="display:flex; align-items:center; justify-content:center; gap:12px; flex-wrap:wrap;">
            <div style="background:#4dc3ff15; border:1px solid #4dc3ff44; border-radius:10px; padding:14px 20px;">
                <div style="font-size:10px;color:#4dc3ff;font-weight:700;letter-spacing:1px;">SALES</div>
                <div style="font-size:18px;font-weight:800;color:#dce8ff;">829K rows</div>
                <div style="font-size:10px;color:#7a9abf;">Sale_ID, Date, Store_ID, Product_ID, Units</div>
            </div>
            <div style="font-size:14px;color:#b84dff;font-weight:700;">⟕<br><span style="font-size:9px;">LEFT JOIN<br>Product_ID</span></div>
            <div style="background:#b84dff15; border:1px solid #b84dff44; border-radius:10px; padding:14px 20px;">
                <div style="font-size:10px;color:#b84dff;font-weight:700;letter-spacing:1px;">PRODUCTS</div>
                <div style="font-size:18px;font-weight:800;color:#dce8ff;">35 rows</div>
                <div style="font-size:10px;color:#7a9abf;">Product_Name, Category, Cost, Price</div>
            </div>
            <div style="font-size:14px;color:#b84dff;font-weight:700;">⟕<br><span style="font-size:9px;">LEFT JOIN<br>Store_ID</span></div>
            <div style="background:#39ff1415; border:1px solid #39ff1444; border-radius:10px; padding:14px 20px;">
                <div style="font-size:10px;color:#39ff14;font-weight:700;letter-spacing:1px;">STORES</div>
                <div style="font-size:18px;font-weight:800;color:#dce8ff;">50 rows</div>
                <div style="font-size:10px;color:#7a9abf;">Store_Name, City, Location</div>
            </div>
            <div style="font-size:20px;color:#ff4da6;padding:0 10px;">→</div>
            <div style="background:#ff4da615; border:1px solid #ff4da644; border-radius:10px; padding:14px 20px;">
                <div style="font-size:10px;color:#ff4da6;font-weight:700;letter-spacing:1px;">MERGED DATASET</div>
                <div style="font-size:18px;font-weight:800;color:#dce8ff;">829K rows × 14 cols</div>
                <div style="font-size:10px;color:#7a9abf;">merged_sales_data.csv</div>
            </div>
        </div>
        <div style="margin-top:16px; font-size:11px; color:#7a9abf;">
            Pipeline inventori terpisah: <span style="color:#4dc3ff;">inventory.csv</span> ⟕ products ⟕ stores → 
            <span style="color:#39ff14;">inv DataFrame</span> (1,593 baris)
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ── STEP 4: FEATURE ENGINEERING ──
    st.markdown('<div class="section-title">Step 4 — Feature Engineering (Kolom Turunan)</div>', unsafe_allow_html=True)

    features = [
        ("Revenue", "Units × Product_Price", "Pendapatan per transaksi", "float64", "#ff4da6"),
        ("Profit", "Units × (Product_Price − Product_Cost)", "Laba kotor per transaksi", "float64", "#b84dff"),
        ("Year", "Date.dt.year", "Tahun transaksi", "int64", "#4dc3ff"),
        ("Month", "Date.dt.month", "Bulan transaksi (1-12)", "int64", "#4dc3ff"),
        ("Quarter", "Date.dt.quarter", "Kuartal transaksi (1-4)", "int64", "#4dc3ff"),
        ("YearMonth", "Date.dt.to_period('M')", "Periode bulanan (2022-01)", "str", "#4dc3ff"),
        ("Inv_Value", "Stock_On_Hand × Product_Cost", "Nilai inventori at cost", "float64", "#39ff14"),
        ("Avg_Daily_Sales", "Total_Units / Period_Days", "Rata-rata penjualan harian", "float64", "#39ff14"),
        ("Days_of_Supply", "Stock_On_Hand / Avg_Daily_Sales", "Ketahanan stok (hari)", "float64", "#ffaa00"),
    ]

    feat_rows = ""
    for name, formula, desc, dtype, color in features:
        feat_rows += f"""<tr>
        <td class="td-name" style="color:{color};">{name}</td>
        <td style="font-family:monospace;font-size:11px;color:#aabdd8;">{formula}</td>
        <td>{desc}</td>
        <td><span class="td-badge" style="background:{color}15;color:{color};border:1px solid {color}44;">{dtype}</span></td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:10px;">
    <table class="custom-table"><thead><tr>
    <th>Kolom Baru</th><th>Formula</th><th>Deskripsi</th><th>Tipe</th>
    </tr></thead><tbody>{feat_rows}</tbody></table></div></div>""", unsafe_allow_html=True)

    st.write("")

    # ── STEP 5: DATA QUALITY ──
    st.markdown('<div class="section-title">Step 5 — Data Quality Check</div>', unsafe_allow_html=True)

    # Compute quality metrics
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
            ("Null Values", f"{null_count}", "✅ Bersih" if null_count == 0 else f"⚠️ {null_count} null", "#39ff14" if null_count == 0 else "#ff4da6"),
            ("Duplikat Sale_ID", f"{dup_count}", "✅ Tidak ada duplikat" if dup_count == 0 else f"⚠️ {dup_count} duplikat", "#39ff14" if dup_count == 0 else "#ffaa00"),
            ("Revenue Negatif", f"{neg_revenue}", "✅ Tidak ada" if neg_revenue == 0 else f"⚠️ {neg_revenue} baris", "#39ff14" if neg_revenue == 0 else "#ff4da6"),
            ("Profit Negatif", f"{neg_profit}", "✅ Tidak ada" if neg_profit == 0 else f"ℹ️ {neg_profit} baris (wajar)", "#39ff14" if neg_profit == 0 else "#4dc3ff"),
        ]

        for check_name, value, status, color in checks:
            st.markdown(f"""
            <div class="chart-card" style="padding:12px 18px; margin-bottom:8px; border-left:3px solid {color};">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-size:12px;font-weight:600;color:#dce8ff;">{check_name}</span>
                        <span style="font-size:11px;color:#7a9abf;margin-left:8px;">({value})</span>
                    </div>
                    <span style="font-size:11px;color:{color};font-weight:600;">{status}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with qc2:
        st.markdown(f"""
        <div class="chart-card" style="padding:18px;">
            <div class="chart-title" style="margin-bottom:14px;">Dataset Summary</div>
            <table style="width:100%;font-size:12px;color:#aabdd8;">
            <tr><td style="padding:6px 0;">📅 Periode Data</td>
                <td style="text-align:right;color:#dce8ff;font-weight:600;">{date_min} → {date_max}</td></tr>
            <tr><td style="padding:6px 0;">📆 Total Hari</td>
                <td style="text-align:right;color:#4dc3ff;font-weight:700;">{period_days_val:,} hari</td></tr>
            <tr><td style="padding:6px 0;">🧾 Total Transaksi</td>
                <td style="text-align:right;color:#ff4da6;font-weight:700;">{len(df):,}</td></tr>
            <tr><td style="padding:6px 0;">🏬 Jumlah Toko</td>
                <td style="text-align:right;color:#b84dff;font-weight:700;">{n_stores}</td></tr>
            <tr><td style="padding:6px 0;">🎲 Jumlah Produk</td>
                <td style="text-align:right;color:#39ff14;font-weight:700;">{n_products}</td></tr>
            <tr><td style="padding:6px 0;">🌆 Jumlah Kota</td>
                <td style="text-align:right;color:#ffaa00;font-weight:700;">{n_cities}</td></tr>
            <tr><td style="padding:6px 0;">📦 Kombinasi Inventori</td>
                <td style="text-align:right;color:#4dc3ff;font-weight:700;">{len(inventory):,}</td></tr>
            <tr style="border-top:1px solid rgba(77,195,255,0.15);">
                <td style="padding:8px 0;font-weight:600;color:#dce8ff;">📐 Kolom Final</td>
                <td style="text-align:right;color:#dce8ff;font-weight:700;">{len(df.columns)} kolom</td></tr>
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
        if len(sample_val) > 40:
            sample_val = sample_val[:40] + "..."
        null_pct = df[col].isnull().mean() * 100
        unique_count = df[col].nunique()

        dtype_color = "#4dc3ff" if "int" in dtype_str else ("#ff4da6" if "float" in dtype_str else ("#b84dff" if "datetime" in dtype_str else "#7a9abf"))

        schema_rows += f"""<tr>
        <td style="color:#7a9abf;font-size:11px;">{i+1}</td>
        <td class="td-name">{col}</td>
        <td><span class="td-badge" style="background:{dtype_color}15;color:{dtype_color};border:1px solid {dtype_color}44;">{dtype_str}</span></td>
        <td style="font-family:monospace;font-size:11px;color:#aabdd8;">{sample_val}</td>
        <td style="color:#39ff14;">{unique_count:,}</td>
        <td style="color:{'#39ff14' if null_pct == 0 else '#ff4da6'};">{null_pct:.1f}%</td>
        </tr>"""

    st.markdown(f"""<div class="chart-card" style="padding:0;overflow:hidden;">
    <div style="overflow-x:auto;border-radius:10px;">
    <table class="custom-table"><thead><tr>
    <th>#</th><th>Kolom</th><th>Tipe Data</th><th>Contoh Nilai</th><th>Unik</th><th>Null %</th>
    </tr></thead><tbody>{schema_rows}</tbody></table></div></div>""", unsafe_allow_html=True)
