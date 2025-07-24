太棒了！你今天學了很多 Python 的內容，從字典、函式、使用 `Streamlit` 做小網站，到丟骰子遊戲的統計分析！
我幫你整理成一篇簡單又適合國小學生的學習筆記 👇

---

# 🐍 Python 程式筆記（簡單易懂版）

## ✨ 一、字典（Dictionary）

字典就像一本字典或表格，一個「關鍵字」對應一個「值」：

```python
d2 = {"apple": "蘋果"}
d3 = {1: "one", 2: "two", 3: "three"}
```

你可以：

- 查詢資料：

  ```python
  print(d3[2])  # 顯示 two
  print(d2["apple"])  # 顯示 蘋果
  ```

- 用 `for` 印出所有資料：

  ```python
  for key in d3:  # 印出每個關鍵字
      print(key)

  for value in d3.values():  # 印出每個值
      print(value)

  for key, value in d3.items():  # 同時印出關鍵字和值
      print(f"{key}:{value}")
  ```

- 加資料 / 改資料：

  ```python
  d3[4] = "four"  # 新增
  d3[2] = "二"  # 修改
  ```

- 刪資料：

  ```python
  v = d3.pop(1)
  print(f"刪除的值:{v}")
  ```

- 檢查資料是否存在：

  ```python
  print(2 in d3)  # True
  print("three" in d3)  # False，這是值不是鍵
  ```

---

## 🖼️ 二、做一個小小購物網站（用 Streamlit）

你學會做一個網頁程式，功能有：

1. 顯示所有商品圖片
2. 顯示商品名稱、價格、庫存
3. 點按鈕就能購買（庫存會減少）
4. 可以增加庫存數量

這個用的是 `streamlit` 工具，也會用到檔案處理（顯示圖片）、按鈕互動、存資料的方式（用 `session_state`）👍

---

## 🧮 三、自訂的函式（Function）

函式就是一段你自己命名的小程式，會幫你做某件事：

```python
def hello():
    print("hello")

def hello2(name):
    print("hello" + name)

hello()  # 顯示 hello
hello2("Mike")  # 顯示 helloMike
```

還有可以回傳結果的函式：

```python
def my_max(a, b):
    if a > b:
        return a
    else:
        return b

print(my_max(10, 20))  # 顯示 20
```

---

## 🔘 四、圓形與正方形的面積計算

你寫了可以算面積的函式：

```python
def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi
```

```python
print(calculate_circle_area(10))  # 算一個半徑 10 的圓面積
```

還有算正方形面積的方法：

```python
def calculate_square_area():
    area = length**2
    print("面積是", area)

length = 10
calculate_square_area()  # 印出面積
```

---

## 🧭 五、兩點距離計算

你寫了一個函式，輸入兩點的 (x, y) 座標，就能算出距離：

```python
def distance():
    dis = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return dis
```

這個用到了數學裡的距離公式，非常厲害！

---

## 🎲 六、丟骰子統計遊戲

這是一個會丟很多次骰子的程式，然後統計出現幾次：

```python
import random

def roll_dice(n):
    save = []
    for i in range(n):
        number = random.randint(1, 6)
        save.append(number)
    return save

outcome = roll_dice(5)  # 丟 5 次
print(outcome)
```

然後你還寫了程式來計算每個點數出現幾次：

```python
# 如果出現的是 1，n1 加 1
if num == 1:
    n1 += 1
```

---

## 📚 總結一下你今天學了：

✅ 字典的用法（新增、查詢、刪除、改）
✅ 自訂函式
✅ 圓與正方形面積計算
✅ 使用 `Streamlit` 製作購物網頁
✅ 丟骰子統計分析遊戲
✅ 會用 `input()` 讀取使用者輸入
✅ 學會怎麼用變數儲存資料、重複執行（用 `for`）

---

你真的學了好多東西，超級棒！👏
如果你想要我幫你做成可列印的 PDF 筆記或加上圖片，也可以跟我說喔～
