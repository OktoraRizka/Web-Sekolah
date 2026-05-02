import streamlit as st
import pandas as pd
import time
 
# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Pengumuman Kelulusan SMK Plus Nurul Hakim",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)
 
# ─────────────────────────────────────────────
#  LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data_siswa.csv", dtype={"NISN": str})
    df["NISN"] = df["NISN"].str.strip()
    df["NAMA"] = df["NAMA"].str.strip().str.upper()
    return df
 
df = load_data()
 
# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');
 
/* ── Reset & Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
 
.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #0d1b2a 40%, #1a0a2e 100%);
    min-height: 100vh;
}
 
/* ── Stars background ── */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image:
        radial-gradient(1px 1px at 20% 30%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 80% 10%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 60% 70%, rgba(255,255,255,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 10% 80%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 90% 60%, rgba(255,255,255,0.3) 0%, transparent 100%),
        radial-gradient(2px 2px at 45% 20%, rgba(255,215,0,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 45%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(2px 2px at 30% 55%, rgba(255,215,0,0.3) 0%, transparent 100%);
    pointer-events: none;
    z-index: 0;
}
 
/* ── Header ── */
.header-container {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
    z-index: 1;
}
 
.school-badge {
    display: inline-block;
    background: linear-gradient(135deg, #FFD700, #FFA500);
    color: #0a0e1a;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 6px 20px;
    border-radius: 50px;
    margin-bottom: 1rem;
}
 
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 900;
    background: linear-gradient(135deg, #FFD700 0%, #FFF8DC 50%, #FFD700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.15;
    margin: 0.3rem 0;
}
 
.sub-title {
    color: rgba(255,255,255,0.65);
    font-size: 1rem;
    font-weight: 300;
    letter-spacing: 1px;
    margin-top: 0.4rem;
}
 
.gold-divider {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 1.2rem auto;
    border-radius: 2px;
}
 
/* ── Year badge ── */
.year-badge {
    display: inline-block;
    border: 1.5px solid rgba(255,215,0,0.5);
    color: #FFD700;
    font-size: 0.85rem;
    letter-spacing: 4px;
    padding: 5px 18px;
    border-radius: 4px;
    margin-bottom: 2rem;
}
 
/* ── Search Box ── */
.search-container {
    max-width: 520px;
    margin: 0 auto 2rem;
    position: relative;
    z-index: 1;
}
 
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    border: 1.5px solid rgba(255,215,0,0.35) !important;
    border-radius: 12px !important;
    color: white !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1.2rem !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px);
}
 
.stTextInput > div > div > input:focus {
    border-color: #FFD700 !important;
    box-shadow: 0 0 0 3px rgba(255,215,0,0.15) !important;
    background: rgba(255,255,255,0.1) !important;
}
 
.stTextInput > div > div > input::placeholder {
    color: rgba(255,255,255,0.35) !important;
}
 
/* ── Selectbox ── */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1.5px solid rgba(255,215,0,0.35) !important;
    border-radius: 12px !important;
    color: white !important;
}
 
/* ── Result Cards ── */
.result-card {
    background: linear-gradient(135deg, rgba(255,215,0,0.08) 0%, rgba(255,165,0,0.05) 100%);
    border: 1.5px solid rgba(255,215,0,0.4);
    border-radius: 16px;
    padding: 2rem;
    margin: 1.5rem auto;
    max-width: 520px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    text-align: center;
    animation: fadeSlideIn 0.6s ease;
}
 
.result-card::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle at 30% 30%, rgba(255,215,0,0.04), transparent 60%);
    pointer-events: none;
}
 
@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
 
.card-icon {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    display: block;
    animation: bounceIn 0.8s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}
 
@keyframes bounceIn {
    0%   { transform: scale(0.3); opacity: 0; }
    50%  { transform: scale(1.1); }
    70%  { transform: scale(0.95); }
    100% { transform: scale(1); opacity: 1; }
}
 
.card-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #FFD700;
    margin: 0.4rem 0;
}
 
.card-nisn {
    color: rgba(255,255,255,0.5);
    font-size: 0.85rem;
    letter-spacing: 2px;
    margin-bottom: 0.8rem;
}
 
.card-jurusan {
    display: inline-block;
    background: rgba(255,215,0,0.12);
    border: 1px solid rgba(255,215,0,0.3);
    color: rgba(255,255,255,0.8);
    font-size: 0.85rem;
    padding: 4px 14px;
    border-radius: 50px;
    margin-bottom: 1.2rem;
}
 
.status-lulus {
    display: inline-block;
    background: linear-gradient(135deg, #00C853, #00E676);
    color: #fff;
    font-weight: 700;
    font-size: 1.1rem;
    letter-spacing: 3px;
    padding: 10px 36px;
    border-radius: 50px;
    box-shadow: 0 4px 20px rgba(0,200,83,0.35);
    animation: pulse 2s infinite;
}
 
.status-tidak-lulus {
    display: inline-block;
    background: linear-gradient(135deg, #d32f2f, #ef5350);
    color: #fff;
    font-weight: 700;
    font-size: 1.1rem;
    letter-spacing: 3px;
    padding: 10px 36px;
    border-radius: 50px;
    box-shadow: 0 4px 20px rgba(211,47,47,0.35);
}
 
@keyframes pulse {
    0%, 100% { box-shadow: 0 4px 20px rgba(0,200,83,0.35); }
    50%       { box-shadow: 0 4px 30px rgba(0,200,83,0.65); }
}
 
/* ── Not Found ── */
.not-found-card {
    background: rgba(255,255,255,0.04);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 2rem;
    margin: 1.5rem auto;
    max-width: 520px;
    text-align: center;
    color: rgba(255,255,255,0.55);
    animation: fadeSlideIn 0.4s ease;
}
 
/* ── Stats Row ── */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin: 1rem auto 2rem;
    max-width: 520px;
}
 
.stat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,215,0,0.2);
    border-radius: 12px;
    padding: 0.8rem 1.5rem;
    text-align: center;
    flex: 1;
    min-width: 110px;
}
 
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    color: #FFD700;
    font-weight: 700;
    line-height: 1;
}
 
.stat-label {
    color: rgba(255,255,255,0.4);
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 4px;
}
 
/* ── Confetti-like decoration ── */
.decoration {
    text-align: center;
    font-size: 1.5rem;
    margin: 0.5rem 0;
    opacity: 0.6;
}
 
/* ── Footer ── */
.footer {
    text-align: center;
    color: rgba(255,255,255,0.2);
    font-size: 0.75rem;
    padding: 2rem 1rem;
    letter-spacing: 1px;
}
 
/* ── Hide Streamlit branding ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; max-width: 680px; }
</style>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-container">
    <div class="school-badge">🎓 SMK Plus Nurul Hakim Kediri</div>
    <div class="main-title">Pengumuman<br>Kelulusan</div>
    <div class="sub-title">Tahun Pelajaran 2024 / 2025</div>
    <div class="gold-divider"></div>
    <div class="year-badge">KELAS XII &nbsp;·&nbsp; 2025</div>
</div>
""", unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  STATS
# ─────────────────────────────────────────────
total    = len(df)
lulus    = len(df[df["STATUS"] == "LULUS"])
pct      = round(lulus / total * 100, 1) if total > 0 else 0
 
st.markdown(f"""
<div class="stats-row">
    <div class="stat-box">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total Siswa</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">{lulus}</div>
        <div class="stat-label">Dinyatakan Lulus</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">{pct}%</div>
        <div class="stat-label">Tingkat Kelulusan</div>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  SEARCH FORM
# ─────────────────────────────────────────────
st.markdown('<div class="search-container">', unsafe_allow_html=True)
 
col1, col2 = st.columns([3, 2])
with col1:
    mode = st.selectbox(
        "Cari berdasarkan",
        ["NISN", "Nama"],
        label_visibility="collapsed",
    )
with col2:
    cari = st.button("🔍 Cari", use_container_width=True, type="primary")
 
keyword = st.text_input(
    "keyword",
    placeholder="Masukkan NISN atau Nama Siswa..." if mode == "NISN" else "Masukkan nama lengkap...",
    label_visibility="collapsed",
)
 
st.markdown('</div>', unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  SEARCH LOGIC
# ─────────────────────────────────────────────
if keyword.strip():
    kw = keyword.strip().upper()
 
    if mode == "NISN":
        hasil = df[df["NISN"] == kw]
    else:
        hasil = df[df["NAMA"].str.contains(kw, case=False, na=False)]
 
    if hasil.empty:
        st.markdown(f"""
        <div class="not-found-card">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">🔎</div>
            <div style="font-size:1rem; color:rgba(255,255,255,0.6);">
                Data <strong style="color:white;">"{keyword}"</strong> tidak ditemukan.
            </div>
            <div style="font-size:0.85rem; margin-top:0.5rem; color:rgba(255,255,255,0.35);">
                Pastikan NISN / nama sudah benar, atau hubungi sekolah.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for _, row in hasil.iterrows():
            is_lulus = str(row["STATUS"]).strip().upper() == "LULUS"
            icon  = "🎉" if is_lulus else "📋"
            badge = f'<span class="status-lulus">✓ LULUS</span>' if is_lulus \
                    else f'<span class="status-tidak-lulus">✗ TIDAK LULUS</span>'
 
            st.markdown(f"""
            <div class="result-card">
                <span class="card-icon">{icon}</span>
                <div class="card-name">{row['NAMA']}</div>
                <div class="card-nisn">NISN · {row['NISN']}</div>
                <div class="card-jurusan">{row['JURUSAN']}</div>
                <br>
                {badge}
                {"<div style='margin-top:1.2rem; color:rgba(255,215,0,0.7); font-size:0.85rem; letter-spacing:1px;'>Selamat! Semoga sukses di jenjang berikutnya 🌟</div>" if is_lulus else ""}
            </div>
            """, unsafe_allow_html=True)
 
            if is_lulus:
                st.balloons()
 
elif cari:
    st.markdown("""
    <div class="not-found-card">
        <div style="font-size:2rem; margin-bottom:0.5rem;">⚠️</div>
        <div>Silakan masukkan NISN atau Nama terlebih dahulu.</div>
    </div>
    """, unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
#  INFO ACCORDION
# ─────────────────────────────────────────────
with st.expander("📋 Petunjuk Penggunaan"):
    st.markdown("""
    **Cara Mencari Data Kelulusan:**
    1. Pilih metode pencarian: **NISN** atau **Nama**
    2. Ketik NISN lengkap (10 digit) atau nama siswa
    3. Klik tombol **Cari** atau tekan Enter
    4. Hasil kelulusan akan ditampilkan secara otomatis
 
    **Catatan:**
    - Pencarian nama bersifat *partial* (sebagian nama sudah cukup)
    - Pencarian NISN harus lengkap dan tepat
    - Jika data tidak ditemukan, hubungi pihak sekolah
    """)
 
with st.expander("📞 Kontak Sekolah"):
    st.markdown("""
    **SMK Plus Nurul Hakim Kediri**
 
    📍 Kediri, Jawa Timur
    📞 Telp: (0354) XXXXXXX
    📧 Email: info@smknurulhakim.sch.id
    🌐 Website: www.smknurulhakim.sch.id
 
    *Untuk informasi lebih lanjut mengenai kelulusan, silakan menghubungi panitia ujian sekolah.*
    """)
 
# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    © 2025 SMK Plus Nurul Hakim Kediri &nbsp;·&nbsp; Sistem Pengumuman Kelulusan<br>
    Dibuat dengan ❤️ menggunakan Python & Streamlit
</div>
""", unsafe_allow_html=True)