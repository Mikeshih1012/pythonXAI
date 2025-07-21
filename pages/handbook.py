import streamlit as st

st.write("""

class1

1. 註解 (Comment)
   在程式中，# 後面的部分叫做「註解」，它不會執行，只是給程式設計師做說明使用。

# 這是單行註解

# print("Hello World") # 這行程式不會執行

2. 基本資料類型
   Python 有不同的資料類型，你可以使用它們來處理不同的資訊：

整數 (Integer)：像 6438 這樣的數字。
print(6438)
浮點數 (Float)：像 3.14 這樣的小數。
print(3.14)
布林值 (Boolean)：True 或 False，可以用來表示「對」或「錯」。
print(True)
print(False)
字串 (String)：像 "Hello World" 這樣的文字。
print("Hello World")

3. 變數 (Variable)
   變數就像是一個裝東西的箱子，你可以把數字、文字等東西放進去，並且改變它們的內容：

創建一個變數並賦值：

a = 10 # a 是一個變數，現在它裡面放著數字 10
print(a)
你可以隨時重新賦值給變數：

a = 20 # a 現在變成 20 了
print(a)
你也可以把變數的內容改成不同的資料類型：

a = "apple" # a 變成了字串 "apple"
print(a) 4. 數學運算
Python 可以進行很多數學運算：

加法 (+)、減法 (-)、乘法 (\*)、除法 (/)：

print(7 + 3) # 加法
print(7 - 3) # 減法
print(7 \* 3) # 乘法
print(7 / 3) # 除法
整數除法 (//) 和餘數 (%):

print(7 // 3) # 只取整數部分
print(7 % 3) # 取餘數
指數運算 (\*\*):

print(2 \*\* 3) # 2 的 3 次方，結果是 8 5. 字串操作
Python 可以做很多有趣的字串處理：

連接兩個字串：

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2 # 將 s1 和 s2 用空格連接起來
print(s3) # 結果是 "Hello World"
重複字串：

print("y" + "e" \* 100) # 把 "e" 重複 100 次，然後和 "y" 連接
使用 f-string 快速插入變數到字串裡：

name = "Python"
age = 31
new_str = f"我是{name}, 今年{age}歲"
print(new_str) # 結果是 "我是 Python, 今年 31 歲" 6. 變數類型 (Data Types)
你可以檢查變數的類型，看看它是整數、字串，還是其他類型：

檢查類型：

print(type(True)) # 布林值
print(type(123)) # 整數
print(type(123.0)) # 浮點數
print(type("Hello")) # 字串 7. 型態轉換 (Type Conversion)
你可以把一個類型的資料轉換成另一個類型：

整數轉換：

print(int(True)) # True 轉換成 1
print(int(3.14)) # 3.14 轉換成 3
浮點數轉換：

print(float(123)) # 123 變成 123.0
布林值轉換：

print(bool(0)) # 0 變成 False
print(bool(1)) # 1 變成 True
print(bool("")) # 空字串變成 False
print(bool("Hello")) # 非空字串變成 True
字串轉換：

print(str(True)) # True 變成字串 "True" 8. 使用 input() 函數
input() 函數讓我們能夠從使用者那裡接收資料。你可以提示使用者輸入資料，並將它存到一個變數裡：

讓使用者輸入資料：

get = input("請輸入數字: ") # 提示使用者輸入數字
print(get) # 顯示使用者輸入的資料
print(type(get)) # 顯示資料的類型，會是字串
將使用者輸入的資料轉換成數字來計算：

get = input("請輸入半徑長度") # 請使用者輸入半徑
get = int(get) # 把輸入的字串轉成整數
area = 3.14 \* get \*\* 2 # 計算圓的面積
print(f"圓的面積為: {area}") # 顯示圓的面積

class2

1. 標題 (st.title())
   使用 st.title() 來設定頁面的標題，這個標題會顯示在網頁的最上方。

python
複製
編輯
st.title("這是標題") # 設定頁面標題 2. 顯示文字 (st.write())
st.write() 是一個通用的函數，可以顯示文字、數字、圖像等資料。

python
複製
編輯
st.write("這是 write 寫的內容") # 顯示一般的文字 3. 顯示純文字 (st.text())
如果你只想顯示純文字，可以使用 st.text()，它會顯示一段單純的文字，不會有任何格式化。

python
複製
編輯
st.text("這是 text 寫的內容") # 顯示純文字 4. Markdown 格式 (st.markdown())
Markdown 是一種簡單的文字格式語言，透過它，我們可以做出各種格式化效果。比如說，粗體、斜體、標題、列表、程式碼區塊等。你可以使用 st.markdown() 來顯示 Markdown 格式的文字。

python
複製
編輯
st.markdown(
"""
這是 markdown 寫的字串
_ **粗體字** # 這會顯示粗體
_ _斜體字_ # 這會顯示斜體 \* [連結](https://www.example.com) # 這是超連結
`python
    print("Hello World")  # 這是程式碼區塊
    ` # 這是標題 1 ## 這是標題 2 ### 這是標題 3 #### 這是標題 4
"""
)
在這段程式碼裡，我們用 Markdown 語法來格式化一些文字：

粗體字：用 \*\* 包住文字，會讓文字變成粗體。

斜體字：用 \* 包住文字，會讓文字變成斜體。

連結：使用 [文字](網址) 的格式來創建一個超連結。

程式碼區塊：用三個反引號 ``` 包住程式碼，這樣會顯示成程式碼樣式。

標題：用 # 來創建不同層級的標題，# 是最大標題，#### 是最小標題。

總結：
st.title() 讓你設置頁面標題。

st.write() 用來顯示一般的文字。

st.text() 用來顯示純文字。

st.markdown() 讓你使用 Markdown 格式，讓頁面變得更加有層次和有趣。

         
         """)