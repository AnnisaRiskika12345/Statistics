import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

def main():
    st.title("Aplikasi T-Test (Tabel nilai kritis distribusi T)")
    st.subheader("Cara memakai aplikasi T-Test (Tabel nilai kritis distribusi T)")
    st.write("- Masukkan angka pada kolom derajat bebas (df)")
    st.write("- Masukkan angka pada kolom tingkat signifikansi(α)")
    st.write("- Nilai kritis distribusi T akan muncul berdasarkan df dan taraf signifikansi yang dimasukkan")
    st.write("- Hasil akan muncul sama dengan tabel nilai kritis distribusi T" )
    # Nilai derajat bebas (df)
    df = st.number_input("Derajat bebas(df)")

    # Tingkat signifikansi (α)
    alpha = st.number_input("Tingkat signifikansi (α)")

    # Hitung nilai kritis
    critical_value = t.ppf(1-alpha, df)

    # Tampilan hasil
    st.subheader("Nilai Kritis Distribusi T")
    st.write("Nilai kritis (α={:.3f}):".format(alpha), critical_value)

    # Membuat data untuk plot distribusi
    x_values = np.linspace(-5, 5, 500)
    y_values = t.pdf(x_values, df)

    # Plot Distribusi T
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    ax.fill_between(x_values, y_values, 0, where=(x_values >= critical_value), color='red', alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Sebaran Probabilitas')
    ax.set_title('Distribusi T (df={})'.format(df))
    st.pyplot(fig)

if __name__ == '__main__':
    main()
