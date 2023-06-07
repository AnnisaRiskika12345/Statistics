import streamlit as st
import numpy as np
from scipy.stats import f

def main():
    st.title("Aplikasi Distribusi F")

    st.subheader("Cara memakai Aplikasi distribusi F")
    st.write("- Masukkan angka pada kolom derajat bebas pertama (V1)")
    st.write("- Masukkan angka pada kolom derajat bebas kedua (V2)")
    st.write("- Hasil akan muncul dalam beberapa taraf signifikansi yang diminta")
    st.write("- Hasil yang muncul sama dengan pada tabel distribusi F")
    # Derajat bebas (df)
    degrees_of_freedom1 = st.number_input("Masukkan derajat bebas 1 (V1)", min_value=1, step=1)
    degrees_of_freedom2 = st.number_input("Masukkan derajat bebas 2 (V2)", min_value=1, step=1)
    p = st.number_input("alpha")
    
    # Perhitungan F-hitung
    f_value = f.ppf(p, degrees_of_freedom1, degrees_of_freedom2)
    
    # Tampilan Hasil
    st.subheader('Hasil')
    st.write('F-Value dari (α={}):'.format(p), f_value)
    
    # Plot Distribusi F
    x = np.linspace(0, 10, 500)
    y = f.pdf(x, degrees_of_freedom1, degrees_of_freedom2)
    
    st.subheader("Plot Distribusi F")
    st.line_chart(data={'x': x, 'y': y})

if __name__ == '__main__':
    main()
