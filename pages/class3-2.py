import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("欄位3")
    st.button("按鈕3")
with col4:
    st.write("欄位4")
    st.button("按鈕4")
with col5:
    st.write("欄位5")
    st.button("按鈕5")

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.write(f"你輸入的文字是: {text}")

st.title("session state")
ans = 1
st.write(f"ans={ans}")
if st.button("增加1"):
    ans = ans + 1
st.write(f"ans={ans}")

if "var1" not in st.session_state:
    st.session_state.var1 = 1
st.write(f"var1={st.session_state.var1}")
if st.button("add 1 to var1"):
    st.session_state.var1 = st.session_state.var1 + 1
    st.write(f"var1={st.session_state.var1}")
    st.rerun()
