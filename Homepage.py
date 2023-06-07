import streamlit as st
st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Home")
st.sidebar.success("Pilihlah Halaman")

import streamlit as st

def main():
    st.subheader("Tentang Aplikasi")
    st.write("Selamat datang di Statistic App by Annisa!")
    st.write("Aplikasi ini dirancang untuk memberikan kemudahan dalam mencari probabilitas yang ada di Statistika")
    st.subheader("Fitur dalam Aplikasi")
    st.write("Aplikasi ini memiliki beberapa fitur, antara lain:")
    
    st.write("- App 1: Distribusi Binomial")
    st.write("- App 2: Chi-Square (Tabel nilai kritis Chi-Square)")
    st.write("- App 3: F-Distribution(Tabel distribusi F)")
    st.write("- App 4: T-test (Tabel distribusi T)")
    st.write("- App 5: Distribusi normal dan Tabel distribusi normal standar")

    
if __name__ == '__main__':
    main()
