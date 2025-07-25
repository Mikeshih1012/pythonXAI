import streamlit as st
import openai
import base64

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI圖片解析")

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="以上傳圖片", width=300)

    # 將圖片直接轉為 base64 字串
    base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")

    prompt = st.chat_input("請輸入想對畫的訊息")
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )
        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
