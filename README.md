# 🎓 Aplikasi Pengumuman Kelulusan
**SMK Plus Nurul Hakim Kediri** — Dibuat dengan Python & Streamlit

---

## 📁 Struktur File

```
kelulusan/
├── app.py            ← Aplikasi utama Streamlit
├── data_siswa.csv    ← Data siswa (bisa diganti/diupload)
├── requirements.txt  ← Dependensi Python
└── README.md
```

---

## 🚀 Cara Menjalankan Lokal

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Jalankan aplikasi
```bash
streamlit run app.py
```

### 3. Buka di browser
```
http://localhost:8501
```

---

## 📊 Format Data Siswa (data_siswa.csv)

File CSV harus memiliki kolom berikut:

| Kolom    | Keterangan                  | Contoh                         |
|----------|-----------------------------|--------------------------------|
| NO       | Nomor urut                  | 1                              |
| NISN     | 10 digit NISN siswa         | 0012345601                     |
| NAMA     | Nama lengkap (huruf besar)  | AHMAD FAUZI                    |
| JURUSAN  | Program keahlian            | Teknik Komputer dan Jaringan   |
| STATUS   | Hasil kelulusan             | LULUS / TIDAK LULUS            |

**Contoh isi CSV:**
```csv
NO,NISN,NAMA,JURUSAN,STATUS
1,0012345601,AHMAD FAUZI,Teknik Komputer dan Jaringan,LULUS
2,0012345602,SITI AMINAH,Akuntansi,LULUS
```

---

## ☁️ Deploy ke Streamlit Cloud (Gratis)

1. **Push ke GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Aplikasi pengumuman kelulusan"
   git remote add origin https://github.com/username/repo-name.git
   git push -u origin main
   ```

2. **Deploy di Streamlit Cloud:**
   - Buka [share.streamlit.io](https://share.streamlit.io)
   - Login dengan akun GitHub
   - Klik **"New app"**
   - Pilih repository dan file `app.py`
   - Klik **Deploy**

3. Aplikasi akan otomatis online dengan URL:
   `https://username-repo-name.streamlit.app`

---

## ✨ Fitur Aplikasi

- 🔍 **Pencarian by NISN** — input NISN 10 digit
- 🔍 **Pencarian by Nama** — partial search (sebagian nama)
- 🎉 **Animasi konfeti** untuk siswa yang lulus
- 📊 **Statistik kelulusan** (total siswa, jumlah lulus, persentase)
- 📱 **Responsive** — bisa diakses dari HP maupun PC
- 🌙 **Tema gelap** elegan dengan aksen emas
- ℹ️ **Petunjuk & kontak** sekolah terintegrasi

---

## ⚙️ Kustomisasi

### Ganti nama/info sekolah
Edit bagian ini di `app.py`:
```python
# Di bagian HEADER
"SMK Plus Nurul Hakim Kediri"
"Tahun Pelajaran 2024 / 2025"
"KELAS XII · 2025"
```

### Tambah data siswa massal
Gunakan Excel/Google Sheets, lalu export sebagai CSV dengan format yang sama.

---

## 📞 Kontak & Support

Untuk pertanyaan teknis, sesuaikan kontak sekolah di bagian expander "Kontak Sekolah" dalam `app.py`.
