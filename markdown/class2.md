# 🐍 我學到的 Python 小筆記 ✨

## 🧠 認識比大小和真假比較

這些是用來比較兩個數字的指令，看看哪個大、哪個小，或者是不是一樣：

```python
print(1 == 2)   # 一樣嗎？（False）
print(1 != 2)   # 不一樣嗎？（True）
print(1 >= 2)   # 大於或等於嗎？（False）
print(1 <= 2)   # 小於或等於嗎？（True）
print(1 > 2)    # 大於嗎？（False）
print(1 < 2)    # 小於嗎？（True）
```

### ✅ 判斷真假（布林值）

```python
print(not True)     # 把 True 變 False
print(not False)    # 把 False 變 True
```

```python
print(False and True)   # 兩個都要是 True 才會是 True，否則就是 False
print(True or False)    # 只要有一個是 True，就會是 True
```

| 指令              | 結果  |
| ----------------- | ----- |
| `False and False` | False |
| `True and True`   | True  |
| `False or True`   | True  |
| `False or False`  | False |

---

## 🔐 密碼檢查

### 檢查密碼是否正確：

```python
password = input("請輸入密碼: ")

if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")
```

### 多種密碼對應不同人：

```python
if password == "1234":
    print("歡迎Ray")
elif password == "5678":
    print("歡迎Mike")
elif password == "abcd":
    print("歡迎Alice")
else:
    print("密碼錯誤")
```

---

## 🗓️ 判斷是不是閏年

閏年是什麼呢？有的年份會多一天（2 月有 29 天），這段程式會告訴你：

```python
year = input("請輸入年份: ")
year = int(year)
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}年是閏年")
else:
    print(f"{year}年不是閏年")
```

---

## 🖥️ Streamlit 超酷互動畫面（做成網頁）

```python
import streamlit as st
```

### 💡 輸入一個數字：

```python
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=60)
st.write(f"你輸入的數字是: {number}")
```

### 🎓 根據成績給你一個等級：

```python
number = st.number_input("請輸入成績", min_value=0, max_value=100, value=60)
number = int(number)

if number >= 90:
    st.write("你的等級為A")
elif number >= 80:
    st.write("你的等級為B")
elif number >= 70:
    st.write("你的等級為C")
elif number >= 60:
    st.write("你的等級為D")
else:
    st.write("你的等級為E")
```

### 🎉 點按鈕會放煙火或下雪！

```python
if st.button("**點我**"):
    st.snow()

if st.button("點我", key="unique_key"):
    st.balloons()
```

---

## 🔁 重複做事情（用 `for` 迴圈）

```python
for i in range(10):
    print(i)  # 從 0 數到 9

for i in range(2, 6):
    print(i)  # 從 2 數到 5

for i in range(2, 10, 2):
    print(i)  # 從 2 開始，每次加 2，一直到 8
```

---

## 🏯 做出金字塔

### 數字金字塔：

```python
st.title("數字金字塔")
number = st.number_input("請輸入整數(1到9)", min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(str(i) * i)
```

如果輸入 3，就會顯示：

```
1
22
333
```

### 星星箭頭金字塔：

```python
st.title("箭頭金字塔")
num2 = st.number_input("請輸入箭頭的層數", step=1, min_value=1)

arrow = ""
for i in range(1, num2 + 1):
    arrow += " " * (num2 - i) + "*" * (i * 2 - 1) + "\n"

for i in range(num2):
    arrow += " " * (num2 - 1) + "*" + "\n"

st.write(f"""
        # 箭頭金字塔:
        # {arrow}
        """)
```

---

📘 **結語小提醒：**

- `if` 是在做選擇。
- `for` 是在做重複的事。
- `print()` 和 `st.write()` 都是讓東西顯示出來。
- 用 `==` 是「等於」，而不是把東西設成一樣喔（那是 `=`）。
