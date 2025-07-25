import streamlit as st

st.chat_message("user").write("使用者訊息")
st.chat_message("assistant").write("AI回應")

history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你到底有什麼問題"},
    {"role": "user", "content": "st.chat_message()怎麼用"},
    {"role": "assistant", "content": "自己查阿 不會喔?"},
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪱").write(message["content"])

    else:
        st.chat_message("assistant", avatar="🫠").write(message["content"])
