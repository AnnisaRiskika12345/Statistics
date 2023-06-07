import streamlit as st
import numpy as np
from scipy.stats import binom

def main():
    st.title("Distribusi Binomial")
    st.subheader("Cara memakai aplikasi distribusi binomial")
    st.write("- Masukkan angka pada kolom banyaknya percobaan(n)")
    st.write("- Masukkan angka pada kolom peluang percobaan sukses(p)")
    st.write("- Masukkan angka pada kolom angka kesuksesan (k/x)")
    st.write("- Hasil akan muncul dengan model peluang (x) keberhasilan dari (n) percobaan : peluang distribusi binomial")
    # masukkan angka yang akan diolah 
    n = st.number_input("Banyaknya percobaan (n)", value=10, min_value=1, step=1)
    p = st.number_input("Peluang percobaan sukses (p)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    k = st.number_input("Angka kesuksesan (k/x))", value=5, min_value=0, step=1)

    # penghitung peluang binomial
    binom_prob = binom.pmf(k, n, p)

    # Tampilan hasil
    st.subheader("Distribusi Binomial")
    st.write("Peluang", k, "keberhasilan dari", n, "percobaan:", binom_prob)

    # distribusi binomial yang dihasilkan
    x = np.arange(0, n+1)
    binom_dist = binom.pmf(x, n, p)

    # tampilan plotnya
    st.subheader("Plot Distribusi Binomial")
    st.line_chart(binom_dist)

if __name__ == '__main__':
    main()
