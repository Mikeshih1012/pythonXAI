以下是幫你整理的 Python 筆記，用國小程度的方式說明今天你學到的內容，讓你看得更清楚、更容易懂！

---

## 🧠 今天學到的 Python 小知識筆記

### 一、用電腦來聊天的程式（像 ChatGPT 一樣！）

我們可以讓 Python 幫我們跟 AI 說話，像這樣：

#### 🔑 使用 OpenAI（讓 AI 能幫你）

```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 幫我們把祕密金鑰載進來
openai.api_key = os.getenv("OPENAI_API_KEY")  # 取得 OpenAI 的祕密鑰匙
```

#### 💬 一直聊天的方式（打「exit」或「quit」就能結束）

```python
while True:
    user_input = input("你:")  # 請使用者輸入內容
    if user_input.lower() in ["exit", "quit"]:
        break  # 如果打 exit 就結束聊天

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "請用繁體中文進行後續對話"},
            {"role": "user", "content": user_input},
        ],
    )
    assistant_message = response.choices[0].message.content
    print(f"AI:{assistant_message}")
```

---

### 二、把對話記住的 AI 聊天（記住前面說過的話）

```python
messages = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

while True:
    user_input = input("你:")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})
    print(f"AI:{assistant_message}")
```

---

### 三、用 Streamlit 做聊天畫面

Streamlit 是一種能做漂亮網頁的小工具，我們用它做了聊天畫面！

#### ✨ 最簡單的聊天畫面

```python
import streamlit as st

st.chat_message("user").write("使用者訊息")
st.chat_message("assistant").write("AI回應")
```

#### 📜 顯示聊天歷史紀錄（加上可愛圖示）

```python
history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你到底有什麼問題"},
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪱").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🫠").write(message["content"])
```

#### 💬 可以打字輸入的聊天

```python
if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    st.chat_message("user", avatar="📍").write(message["content"])

prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()
```

---

### 四、有選單、清除按鈕、聊天記錄的完整 AI 聊天室

可以切換模型、清空訊息、記住聊天內容！

```python
import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

# 預設設定
if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"
if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"
if "message" not in st.session_state:
    st.session_state.message = []

# 顯示模型選單與清除按鈕
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    st.session_state.system_message = st.text_input("系統訊息", st.session_state.system_message)
with col2:
    st.session_state.model = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])
with col3:
    if st.button("🗑️"):
        st.session_state.message = []
        st.rerun()

# 顯示訊息
for message in st.session_state.message:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪱").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🫠").write(message["content"])

# 處理新的輸入
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[{"role": "system", "content": st.session_state.system_message}] + st.session_state.message,
    )
    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
```

---

### 五、圖片也能聊天！📸🤖

可以上傳圖片，然後問 AI 圖片裡的東西！

```python
import streamlit as st
import openai
import base64

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI圖片解析")

uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="以上傳圖片", width=300)
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
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                    ],
                }
            ],
        )
        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
```

---

### 六、海龜湯遊戲（AI 當主持人！）

海龜湯是一種推理遊戲，AI 會出題，我們要猜發生什麼事～

```python
import streamlit as st
import openai
import json
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

# 載入題目
with open("question/quizzes.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    if "pick" not in st.session_state:
        st.session_state.pick = random.randrange(len(data))
    quiz = data[st.session_state.pick]

# 預設值
if "system_message" not in st.session_state:
    st.session_state.system_message = f"你是海龜湯遊戲主持人\n你要先說題目\n你不能說出答案只能在答對時說對答錯時說錯如果答案很接近正解時輸出遊戲結束並說出完整答案\n題目:{quiz['title']}\n正解:{quiz['answer']}"

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"
if "message" not in st.session_state:
    st.session_state.message = []

# 選模型、清除訊息
st.title("海龜湯")
col1, col2 = st.columns([4, 1])
with col1:
    st.session_state.model = st.selectbox("AI模型", ["gpt-4o-mini", "gpt-4o"])
with col2:
    if st.button("🗑️"):
        st.session_state.message = []
        st.rerun()

# 顯示題目與對話
st.chat_message("assistant", avatar="🫠").write(f"題目:{quiz['title']}")
for message in st.session_state.message:
    if message["role"] == "user":
        st.chat_message("user", avatar="🪱").write(message["content"])
    else:
        st.chat_message("assistant", avatar="🫠").write(message["content"])

# 玩家輸入猜測
prompt = st.chat_input("請輸入訊息")
if prompt:
    st.session_state.message.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        messages=[{"role": "system", "content": st.session_state.system_message}] + st.session_state.message,
    )
    assistant_message = response.choices[0].message.content
    st.session_state.message.append({"role": "assistant", "content": assistant_message})
    st.rerun()
```

---

## 🎉 小結

今天你學到的 Python 技能很厲害：

- 跟 AI 對話
- 做出自己的聊天程式
- 做成網頁畫面
- 加入圖片
- 做成推理遊戲！

只要持續練習，你一定可以變成小小程式高手！💪

如果你想把這些筆記變成 PDF 或網頁，我也可以幫你製作喔！想要嗎？
