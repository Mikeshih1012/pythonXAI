import streamlit as st
import os

file_path = "markdown"
files = os.listdir(file_path)
files.sort()
for file in files:
    if file.endswith(".md"):
        with open(f"{file_path}/{file}", "r", encoding="utf-8") as f:
            content = f.read()
        with st.expander(file[:-3] + "課堂筆記"):
            st.write(content)
