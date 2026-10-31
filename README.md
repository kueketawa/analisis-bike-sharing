# Proyek Analisis Data: Peminjaman Sepeda (Bike Sharing)

Analisis data peminjaman sepeda Capital Bikeshare (Washington D.C.) periode 2011-2012, disertai dashboard interaktif dengan Streamlit.

## Pertanyaan Bisnis
1. Berapa rata-rata jumlah peminjaman sepeda per hari pada tiap kondisi cuaca (cerah, berkabut/berawan, hujan/salju ringan) sepanjang 2011-2012, dan pada kondisi mana peminjaman paling rendah sehingga jumlah armada bisa disesuaikan?
2. Berapa persentase kontribusi tiap musim terhadap total peminjaman sepeda sepanjang 2011-2012, dan musim mana yang paling rendah sehingga perlu strategi promosi atau penjadwalan perawatan?

## Dataset
Bike Sharing Dataset (`day.csv`, 731 baris data harian). Setelah proses cleaning tersisa 730 baris.

## Ringkasan Proses
- **Gathering:** memuat `day.csv` ke DataFrame.
- **Assessing:** tipe data `dteday` tidak sesuai (teks), satu baris dengan kelembapan (`hum`) bernilai 0 yang tidak masuk akal, dan pemetaan kode musim pada readme dataset tidak cocok dengan rentang tanggal pada data.
- **Cleaning:** mengubah `dteday` ke datetime, membuang satu baris `hum` = 0, serta memetakan kode musim dan cuaca ke label yang bermakna.
- **EDA dan visualisasi:** pengelompokan dan agregasi untuk menjawab kedua pertanyaan, divisualisasikan dengan bar chart (cuaca) dan pie chart (musim).
- **Analisis lanjutan:** binning suhu (manual grouping) menjadi tiga kategori.

## Temuan Utama
- Rata-rata peminjaman per hari: cerah sekitar 4.877, berkabut/berawan sekitar 4.036, dan hujan/salju ringan sekitar 1.862. Hari hujan/salju ringan paling rendah, tetapi hanya 20 hari sehingga perlu hati-hati menafsirkannya.
- Kontribusi musim: Musim Panas tertinggi (32,23%) dan Musim Dingin terendah (14,30%).
- Temuan ini berdasarkan perbandingan rata-rata dan persentase, bukan hubungan sebab-akibat.

## Struktur Folder
```
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   └───day.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## Setup Environment

### Anaconda
```
conda create --name main-ds python=3.12
conda activate main-ds
pip install -r requirements.txt
```

### Shell/Terminal (Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Di Mac/Linux, aktivasi dengan `source venv/bin/activate`.

## Menjalankan Dashboard
Jalankan dari folder utama proyek:
```
streamlit run dashboard/dashboard.py
```
Buka alamat yang muncul di terminal (biasanya http://localhost:8501).

## Dashboard Online
https://bike-sharing-dash-project.streamlit.app/

## Menjalankan Notebook
Buka `notebook.ipynb` dengan Jupyter Notebook, VS Code, atau Google Colab, lalu jalankan semua sel dari atas (Run All). Dataset dibaca dari folder `data/`.
