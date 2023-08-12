import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Somesh Basak")
    content1 = """
    Hi, I am Somesh Basak, I am a Full Stack Developer Traiee at Nxtwave. 
    My skills are Html, CSS, JS, Figma, Bootstrap, Tailwind, Javascript, 
    React JS, Node JS, MySql, Sqlite, Github,
    """
    st.info(content1)

content2 = """
Below you can find some of the apps i built in Python. Feel free to me!."""
st.write(content2)