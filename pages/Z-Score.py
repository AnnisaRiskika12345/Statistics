import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def main():
    st.title("Aplikasi distribusi normal dan Tabel distribusi normal standar")
    st.subheader("Cara memakai kalkulator Z-Score")
    st.write("- Masukkan x pada kolom pertama (X)")
    st.write("- Masukkan rata-rata pada kolom kedua (μ)")
    st.write("- Masukkan standar deviasi pada kolom ketiga (σ)")
    st.write("- Rumus yang digunakan adalah (x - mean) / std_dev")
    st.write("- Hasil yang muncul sama dengan pada tabel distribusi normal standard")
    # Memasukkan data
    x = st.number_input("X")
    mean = st.number_input("μ")
    std_dev = st.number_input("σ")

    # Memastikan bahwa standar deviasi tidak pada nilai 0
    if std_dev != 0:
        # Penghitungan Z-score
        z_score = (x - mean) / std_dev

        # Tampilan hasil
        st.subheader("Z-Score")
        st.write("Z-Score:", z_score)
        st.write("Probabilitas (X <= x):", norm.cdf(z_score))
        st.write("Probabilitas (X > x):", 1 - norm.cdf(z_score))

        # Membuat data untuk plot distribusi
        x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
        y_values = norm.pdf(x_values, mean, std_dev)
        
        # Plot distribusi normal 
        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        ax.fill_between(x_values, y_values, 0, where=(x_values <= x), color='blue', alpha=0.5)
        ax.fill_between(x_values, y_values, 0, where=(x_values > x), color='orange', alpha=0.5)
        ax.set_xlabel('X')
        ax.set_ylabel('Probabilitas')
        ax.set_title('Distribusi Normal')
        st.pyplot(fig)

    else:
        st.write("Error: Standar deviasi (σ) tidak boleh 0")

if __name__ == '__main__':
    main()
