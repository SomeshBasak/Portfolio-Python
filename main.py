import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Somesh Basak")
    content = """
    Hi, I am Somesh Basak, I am a Full Stack Developer Traiee at Nxtwave. 
    My skills are Html, CSS, JS, Figma, Bootstrap, Tailwind, Javascript, 
    React JS, Node JS, MySql, Sqlite, Github,
    """
    st.info(content)