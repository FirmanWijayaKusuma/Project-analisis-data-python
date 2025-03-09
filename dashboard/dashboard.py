import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset yang sudah diproses
df_day = pd.read_csv("dashboard/day_processed.csv")
df_hour = pd.read_csv("dashboard/hour_processed.csv")

# Sidebar untuk navigasi
st.sidebar.title("Dashboard Bike Sharing Firman Wijaya Kusuma")
menu = st.sidebar.radio("Pilih Analisis", ["Overview", "Tren Bulanan & Musiman", "Pengaruh Cuaca", "Waktu Sibuk", "Tipe Pengguna"])

# 1 Overview
if menu == "Overview":
    st.title("Overview Dataset")
    st.write("Dataset ini berisi informasi tentang peminjaman sepeda berdasarkan faktor waktu dan cuaca.")
    st.write(df_day.head())

# 2 Tren Bulanan & Musiman
elif menu == "Tren Bulanan & Musiman":
    st.title("Tren Peminjaman Sepeda per Bulan & Musim")
    
    # Visualisasi peminjaman sepeda per bulan
    monthly_trend = df_day.groupby("mnth")["cnt"].mean()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=monthly_trend.index, y=monthly_trend.values, palette="Blues", ax=ax)
    ax.set_title("Rata-rata Peminjaman Sepeda per Bulan")
    st.pyplot(fig)

    # Visualisasi peminjaman sepeda per musim
    season_trend = df_day.groupby("season")["cnt"].mean()
    season_labels = {"Spring": "Musim Semi", "Summer": "Musim Panas", "Fall": "Musim Gugur", "Winter": "Musim Dingin"}
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=season_trend.index, y=season_trend.values, palette="coolwarm", ax=ax)
    ax.set_xticklabels([season_labels[i] for i in season_trend.index], rotation=30)
    ax.set_title("Rata-rata Peminjaman Sepeda per Musim")
    st.pyplot(fig)

# 3 Pengaruh Cuaca
elif menu == "Pengaruh Cuaca":
    st.title("Pengaruh Cuaca terhadap Peminjaman Sepeda")

    # Visualisasi peminjaman berdasarkan kondisi cuaca
    weather_trend = df_day.groupby("weathersit")["cnt"].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=weather_trend.index, y=weather_trend.values, palette="viridis", ax=ax)
    ax.set_title("Rata-rata Peminjaman Sepeda berdasarkan Kondisi Cuaca")
    st.pyplot(fig)

# 4 Waktu Sibuk
elif menu == "Waktu Sibuk":
    st.title("Tren Peminjaman Berdasarkan Waktu")

    # Visualisasi peminjaman sepeda berdasarkan jam
    hourly_trend = df_hour.groupby("hr")["cnt"].mean()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x=hourly_trend.index, y=hourly_trend.values, marker="o", color="crimson", ax=ax)
    ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Jam dalam Sehari")
    st.pyplot(fig)

# 5 Tipe Pengguna
elif menu == "Tipe Pengguna":
    st.title("Perbandingan Pengguna Kasual vs. Terdaftar")

    # Visualisasi perbandingan pengguna kasual dan terdaftar
    user_type_trend = df_day[["casual", "registered"]].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=user_type_trend.index, y=user_type_trend.values, palette="Set2", ax=ax)
    ax.set_title("Perbandingan Pengguna Kasual vs. Terdaftar")
    st.pyplot(fig)
