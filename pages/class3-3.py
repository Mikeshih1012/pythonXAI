import streamlit as st

st.title("點餐機")

col1, col2 = st.columns([9, 1])
food = col1.text_input("請輸入餐點")
if col2.button("加入", key="add"):
    st.session_state.order.append(food)

if "order" not in st.session_state:
    st.session_state.order = []

st.write("購物籃")
for i in range(len(st.session_state.order)):
    col3, col4 = st.columns([9, 1])
    col3.write(st.session_state.order[i])
    if col4.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
