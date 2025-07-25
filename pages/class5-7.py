import streamlit as st
import openai
import json
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(len(data))
    quiz = data[st.session_state.pick]
if "system_message" not in st.session_state:
    st.session_state.system_message = f"你是海龜湯遊戲主持人\n你要先說題目\n你不能說出答案只能在答對時說對答錯時說錯如果答案很接近正解時輸出遊戲結束並說出完整答案\n題目:{quiz['title']}\n正解:{quiz['answer']}"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if "message" not in st.session_state:
    st.session_state.message = []

st.title("海龜湯")

col1, col2 = st.columns([4, 1])

with col1:
    st.session_state.model = st.selectbox(
        "AI模型",
        ["gpt-4o-mini", "gpt-4o"],
        index=["gpt-4o-mini", "gpt-4o"].index(st.session_state.model),
    )
with col2:
    if st.button("🗑️"):
        st.session_state.message = []
        st.rerun()

st.chat_message("assistant", avatar="🫠").write(f"題目:{quiz['title']}")

for message in st.session_state.message:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪱").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🫠").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.message,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
