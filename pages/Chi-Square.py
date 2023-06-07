import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

def main():
    st.title("Aplikasi Chi-Square (Tabel nilai kritis Chi-Square)")
    st.subheader("Cara memakai aplikasi Chi-Square")
    st.write("- Masukkan angka pada kolom derajat bebas(df)")
    st.write("- Masukkan angka pada kolom taraf signifikansi(α)")
    st.write("- Nilai kritis akan muncul berdasarkan nilai df dan α yang dimasukkan")
    st.write("- Nilai yang muncul sama dengan tabel nilai kritis distribusi chi-square")
    # memasukkan derajat bebas
    df = st.number_input("Derajat bebas(df)")
    p  = st.number_input("Taraf signifikansi (α)")
    # Hitung nilai kritis
    critical_value = chi2.ppf(1-p, df)

    # Tampilan hasil
    st.subheader("Nilai Kritis")
    st.write('Nilai kritis (α={}):'.format(p), critical_value)

    # Membuat data untuk plot distribusi
    x_values = np.linspace(0, critical_value * 1.5, 500)
    y_values = chi2.pdf(x_values, df)

    # Plot distribusi Chi-Square
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.fill_between(x_values, y_values, 0, where=(x_values >= critical_value), color='red', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Sebaran Probabilitas')
    ax.set_title('Distribusi chi-square (df={})'.format(df))
    st.pyplot(fig)

if __name__ == '__main__':
    main()
