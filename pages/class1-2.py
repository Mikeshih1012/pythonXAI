import streamlit as st

st.title("這是標題")
st.write("這是write寫的內容")
st.text("這是text寫的內容")
st.markdown(
    ""
    """
這是markdown寫的字串
* **粗體字**
* *斜體字*
* [連結](https://www.example.com)
```python
prunt("Hello World")
```
# 這是標題1
## 這是標題2
### 這是標題3
#### 這是標題4
"""
)
