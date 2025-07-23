當然可以！以下是幫你整理好的《Python 第三堂課》的筆記，用簡單的國小用詞來說明，希望你看得開心又學得懂 😊

---

# 🐍 Python 第三堂課 簡單筆記 ✨

---

## 🧮 第 3-1 節：學習清單（list）和一些好用的功能

### 🔢 `len()` 是什麼？

可以幫我們「算有幾個東西」

```python
print(len([]))           # 空的，長度是 0
print(len(["蘋果"]))     # 裡面有一個蘋果，長度是 1
print(len("a" "b"))      # 這是兩個字合起來，是 "ab"，長度是 2
print(len([1, 2, 3]))    # 有三個數字，長度是 3
```

---

### 🔁 用 `for` 走訪清單裡的每個東西

```python
l = [1, 2, 3]

# 方法一：用索引（位置）
for i in range(len(l)):
    print(l[i])

# 方法二：直接拿出來用
for element in l:
    print(element)
```

---

### ✏️ 修改清單裡的東西

```python
l[0] = "A"  # 把第1個改成 A
l[2] = "c"  # 把第3個改成 c
print(l)
```

---

### 📋 清單的複製要注意

```python
a = [10, 20, 30]
b = a
b[1] = 100
print(a)  # a 也被改了，因為 a 和 b 是同一個東西

c = [40, 50, 60]
d = c[:]  # 複製一份新的
d[1] = 500
print(c)  # c 不會被改
```

---

### ➕ ➖ 加東西、刪東西

```python
l1 = [1, 2, 3]
l1.append(4)  # 加到最後面
print(l1)

l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")  # 移除第一個 b
print(l2)

l3 = [1, 2, 3]
l3.pop()  # 拿掉最後一個
print(l3)

l4 = [1, 2, 3]
l4.pop(1)  # 拿掉第2個
print(l4)
```

---

### 🔢 排順序 `.sort()`

```python
l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort()
print(l5)  # 數字從小排到大

l6 = ["banana", "apple", "orange"]
l6.sort()
print(l6)  # 字母順序
```

---

## 🌈 第 3-2 節：Streamlit 畫面設計

### 📄 加欄位和按鈕

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

可以把畫面分成左右兩欄，放不同的按鈕。

---

### 💬 文字輸入

```python
text = st.text_input("請輸入文字")
st.write(f"你輸入的文字是: {text}")
```

---

### 📦 session state（記得變數）

```python
if "var1" not in st.session_state:
    st.session_state.var1 = 1

if st.button("add 1 to var1"):
    st.session_state.var1 += 1
    st.rerun()  # 重新整理讓畫面更新
```

---

## 🍔 第 3-3 節：做出簡單點餐機

### 🛒 點餐 + 購物籃 + 刪除功能

```python
if "order" not in st.session_state:
    st.session_state.order = []

food = st.text_input("請輸入餐點")
if st.button("加入"):
    st.session_state.order.append(food)

# 顯示購物籃
for i in range(len(st.session_state.order)):
    st.write(st.session_state.order[i])
    if st.button("刪除", key=i):
        st.session_state.order.pop(i)
        st.rerun()
```

---

## 🔁 第 3-4 節：`while` 跟 `for` 迴圈

### 🌀 while 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

可以重複做事直到條件不成立。

---

### 🛑 break：跳出迴圈

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

### 🎲 random 隨機產生數字

```python
import random
print(random.randrange(1, 1111))
print(random.randint(10, 20))
```

---

### 🎲🎲 抽籤練習

```python
count1 = 0
count2 = 0
count3 = 0

for i in range(100):
    n = random.randrange(1, 4)
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    else:
        count3 += 1
    print(n)

print(f"1的次數: {count1}, 2的次數: {count2}, 3的次數: {count3}")
```

---

## 🎯 第 3-5 節：猜數字遊戲

```python
target = random.randint(1, 100)

while True:
    guess = int(input("請輸入數字"))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜中了")
        break
```

---

## 🎁 第 3-6 節：抽一番賞遊戲

```python
table = [0] * 100
target = random.randint(1, 100)
table[target - 1] = 1

count = 0
while True:
    pick = random.randint(1, 100)
    if table[pick - 1] == 2:
        print("已經被抽過了")
    elif table[pick - 1] == 1:
        print("恭喜你抽到一番賞")
        break
    else:
        print("沒中獎, 繼續")
    table[pick - 1] = 2
    count += 1

print(f"總共抽了{count}次, 花了{count*200}元")
```

---

希望這份筆記幫助你把今天上課的東西記得更清楚！有不懂的也可以再問我唷 😊📘✨
