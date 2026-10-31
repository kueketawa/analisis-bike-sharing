import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pathlib import Path

df = pd.read_csv(Path(__file__).parent / "main_data.csv")

st.header('Dashboard Peminjaman Sepeda 2011-2012 🚴')

st.subheader("Rata-rata Peminjaman per Kondisi Cuaca")

urutan_cuaca = ['Cerah', 'Berkabut/Berawan', 'Hujan/Salju Ringan']
rata_cuaca = df.groupby('weathersit')['cnt'].mean().reindex(urutan_cuaca)

fig, ax = plt.subplots(figsize=(10, 5))
batang = ax.bar(rata_cuaca.index, rata_cuaca.values, color=['#72BCD4', '#72BCD4', '#D9534F'])
ax.bar_label(batang, fmt='%.0f', padding=3)
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-Rata Peminjaman per Hari')
st.pyplot(fig)

st.write("Hari hujan/salju ringan punya rata-rata peminjaman terendah, sekitar 62% di bawah hari cerah.")

st.subheader("Kontribusi Tiap Musim terhadap Total Peminjaman")

total_musim = df.groupby('season').agg({'cnt': 'sum'})
total_semua = df['cnt'].sum()
persen_musim = (total_musim / total_semua * 100).sort_values('cnt', ascending=False)

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(persen_musim['cnt'], labels=persen_musim.index, autopct='%1.1f%%',
       startangle=90, counterclock=False,
       colors=['#2C7FB8', '#72BCD4', '#A8D5E2', '#D9534F'],
       wedgeprops={'edgecolor': 'white'})
st.pyplot(fig)

st.write("Musim Panas menyumbang peminjaman terbanyak (32,23%), sedangkan Musim Dingin paling rendah (14,30%).")