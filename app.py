import streamlit as st
import pandas as pd
from PIL import Image
import os

# Mengambil path folder saat ini
current_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
image_path = os.path.join(current_dir, "images.jpg")

# Load gambar logo sekali
try:
    logo = Image.open(image_path)
except FileNotFoundError:
    st.warning("Foto logo tidak ditemukan. Pastikan file bernama 'images.jpg' ada di folder yang sama.")
    logo = None

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Kelulusan SMK Plus Nurul Hakim",
    page_icon=logo,
    layout="centered",
)
# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("DATA_KELULUSAN_KELAS_XII_2026.xlsx", dtype={"NIS": str})
        if 'KETERANAGN' in df.columns:
            df = df.rename(columns={'KETERANAGN': 'KETERANGAN'})
            
        df["NIS"] = df["NIS"].str.strip()
        df["NAMA"] = df["NAMA"].str.strip().str.upper()
        df = df.drop_duplicates(subset="NIS")
        return df
    except Exception as e:
        st.error(f"Error detail: {e}") 
        return pd.DataFrame({
            "NIS": ["Masukkan NIS"],
            "NAMA": ["Masukkan Nama"],
            "JURUSAN": ["Masukkan Jurusan"],
            "KETERANGAN": [""]
        })

df = load_data()

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc !important;
    }
    

    .result-card {
        background-color: #ffffff;
        padding: 40px 30px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        text-align: center;
        margin: 25px 0;
    }

    .badge-lulus {
        background-color: #dcfce7;
        color: #166534;
        padding: 16px 40px;
        border-radius: 50px;
        font-weight: 800;
        font-size: 1.25rem;
        border: 2px solid #86efac;
        display: inline-block;
    }

    .btn-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-top: 25px;
    }

    .btn-download {
        background-color: #1e40af;
        padding: 14px 24px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 0.95rem;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 6px 15px rgba(30, 64, 175, 0.2);
        transition: all 0.3s ease;
    }

    .btn-skl {
        background-color: #059669; /* Green color for SKL */
        box-shadow: 0 6px 15px rgba(5, 150, 105, 0.2);
    }
    
    .btn-download:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        opacity: 0.95;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        padding: 50px 0 30px;
    }

    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────

with st.container():
    
    col1, col2, col3 = st.columns([1, 0.6, 1]) 
    
    with col2:
        try:
            current_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
            image_path = os.path.join(current_dir, "images.jpg")
            img = Image.open(image_path)
            
            st.image(img, use_container_width=True)
        except Exception:
            st.markdown('<div style="font-size: 4.2rem; margin-bottom: 12px;">🎓</div>', unsafe_allow_html=True)

    # Teks Header (Tetap Putih karena di dalam Box Biru)
    st.markdown("""
    <div style="text-align: center; width: 100%;">
        <div style="font-size: 2.1rem; font-weight: 800; margin-top: 15px; color: white !important;">
            SMK PLUS NURUL HAKIM
        </div>
        <div style="font-size: 1rem; opacity: 0.95; letter-spacing: 2px; text-transform: uppercase; color: white !important; margin-top: 5px;">
            PENGUMUMAN KELULUSAN TAHUN PELAJARAN 2024/2025
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SEARCH FORM
# ─────────────────────────────────────────────
# Judul dengan warna hitam yang dipaksakan
st.markdown('<h3 style="color: black !important; font-weight: bold;">🔍 Verifikasi Kelulusan</h3>', unsafe_allow_html=True)

# Teks instruksi dengan warna hitam yang dipaksakan
st.markdown('<div style="color: black !important; margin-bottom: 10px;">Masukkan Nomor Induk Siswa (NIS) Anda:</div>', unsafe_allow_html=True)

with st.form("search_form"):
    keyword = st.text_input(
        "NIS",
        placeholder="Masukkan NIS",
        max_chars=12,
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("🔎 Cek KETERANGAN Kelulusan", use_container_width=True)

# ─────────────────────────────────────────────
# LOGIKA PENCARIAN
# ─────────────────────────────────────────────
if submitted:
    NIS_input = keyword.strip()
    
    if not NIS_input:
        st.warning("⚠️ Mohon masukkan NIS Anda.")
    else:
        hasil = df[df["NIS"] == NIS_input]
        
        if not hasil.empty:
            row = hasil.iloc[0]
            is_lulus = str(row["KETERANGAN"]).strip().upper() == "LULUS"

            # Drive Links
            folder_pengumuman = "1_Zb4hoMt5TlxEBoRSD65BnN0hJcuzIUD"
            folder_skl = "1z5a8XOrEWF5ghDQhLTd3ImtH3kTxNs9Y"
            
            link_pengumuman = f"https://drive.google.com/drive/u/0/folders/{folder_pengumuman}?q={NIS_input}"
            link_skl = f"https://drive.google.com/drive/u/0/folders/{folder_skl}?q={NIS_input}"

            st.markdown(f"""
            <div class="result-card">
                <p style="margin-bottom:6px; color:#64748B; font-size: 0.9rem;">NAMA SISWA</p>
                <h2 style="margin: 8px 0 18px 0; color:#1e293b;">{row['NAMA']}</h2>
                <p style="color:#475569; font-size: 1.05rem; margin-bottom: 30px;">{row['JURUSAN']}</p>
                
                
                {'✅ DINYATAKAN LULUS' if is_lulus else '‼️ LULUS BERSYARAT'}
                
            """, unsafe_allow_html=True)

            if is_lulus:
                st.markdown(f"""
                <div style="margin-top: 35px;">
                    <p style="color:#166534; font-weight:600; font-size:1.1rem;">
                        Selamat atas keberhasilan Anda! 🌟
                    </p>
                    <div class="btn-container">
                        <a href="{link_pengumuman}" target="_blank" class="btn-download">
                            📥 Pengumuman (PDF)
                        </a>
                        <a href="{link_skl}" target="_blank" class="btn-download btn-skl">
                            📄 Unduh SKL (PDF)
                        </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div style="margin-top: 35px;">
                    <p style="color:#166534; font-weight:600; font-size:1.1rem;">
                        Harap Segera Menghubungi Uztadz Zohri (087765931993)!
                    </p>
                </div>
            """, unsafe_allow_html=True)
                st.balloons()
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("❌ Data dengan NIS tersebut tidak ditemukan. Pastikan NIS yang dimasukkan benar.")

# ─────────────────────────────────────────────
# INFORMASI
# ─────────────────────────────────────────────


st.markdown("""
<div class="footer">
    © 2025 SMK Plus Nurul Hakim Kediri<br>
    <span style="font-size:0.8rem;">Portal Pengumuman Kelulusan Digital</span>
</div>
""", unsafe_allow_html=True)