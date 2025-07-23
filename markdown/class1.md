### Python 程式設計入門筆記（適合國小學生）

#### 一、基本數字與資料型態

1. **數字輸出**
   你可以直接輸出數字，像這樣：

   ```python
   print(6438)  # 顯示數字6438
   print(3.14)  # 顯示小數3.14
   ```

2. **布林值**
   布林值是對或錯，通常是 `True`（對） 或 `False`（錯）：

   ```python
   print(True)   # 顯示 True
   print(False)  # 顯示 False
   ```

3. **字串輸出**
   字串是由文字組成的內容，像是名字或是一句話：

   ```python
   print("Hello World")  # 顯示文字
   print("y" + "e" * 100)  # 顯示 y 之後跟著100個 e
   ```

#### 二、變數和運算

1. **變數**
   變數就像是一個盒子，可以放進任何資料。可以隨時改變盒子裡面的東西：

   ```python
   a = 10  # 把10放進變數a
   print(a)  # 顯示a的內容：10
   a = 20  # 把20放進a
   print(a)  # 顯示a的內容：20
   a = "apple"  # 把字串"apple"放進a
   print(a)  # 顯示a的內容：apple
   ```

2. **數學運算**
   Python 支援基本的數學運算：

   ```python
   print(7 + 3)  # 加法
   print(7 - 3)  # 減法
   print(7 * 3)  # 乘法
   print(7 / 3)  # 除法
   print(7 // 3)  # 整數除法
   print(7 % 3)  # 取餘數
   print(2**3)  # 指數運算，2的3次方
   ```

3. **字串連接**
   字串可以相加，像這樣：

   ```python
   s1 = "Hello"
   s2 = "World"
   s3 = s1 + " " + s2  # 把s1和s2用空格連接起來
   print(s3)  # 顯示: Hello World
   ```

#### 三、型態轉換

1. **從一種型態轉換為另一種型態**

   - **從布林值到數字**：

     ```python
     print(int(True))  # 顯示 1
     print(int(False)) # 顯示 0
     ```

   - **從數字到字串**：

     ```python
     print(str(1000))  # 把1000變成字串："1000"
     ```

2. **從數字到浮點數**：

   ```python
   print(float(123))  # 123會變成123.0
   ```

#### 四、使用 `input` 讓使用者輸入資料

1. **接收使用者的輸入**
   你可以讓使用者輸入資料，然後程式會處理這些資料：

   ```python
   get = input("請輸入數字: ")
   print(get)  # 顯示使用者輸入的內容
   print(type(get))  # 顯示輸入的型態（字串）
   ```

2. **計算圓的面積**
   使用者可以輸入圓的半徑，然後計算圓的面積：

   ```python
   get = input("請輸入半徑長度: ")
   get = int(get)  # 把輸入的內容變成整數
   area = 3.14 * get**2  # 圓的面積公式
   print(f"圓的面積為: {area}")  # 顯示面積
   ```

#### 五、進階：用 Streamlit 顯示網頁

1. **簡單顯示標題與內容**
   使用 `Streamlit` 可以快速顯示網頁內容，像這樣：

   ```python
   import streamlit as st

   st.title("這是標題")  # 顯示大標題
   st.write("這是write寫的內容")  # 顯示文字
   st.text("這是text寫的內容")  # 顯示文字，會跟 `write` 不同
   ```

2. **Markdown 語法**
   可以使用 `Markdown` 語法來顯示更豐富的內容：

   ````python
   st.markdown(
       """
       這是markdown寫的字串
       * **粗體字**
       * *斜體字*
       * [連結](https://www.example.com)
       ```python
       print("Hello World")
       ```
       # 這是標題1
       ## 這是標題2
       ### 這是標題3
       #### 這是標題4
       """
   )
   ````

---

### 小結

今天我們學習了很多關於 Python 的基本知識，從數字運算、變數，到讓使用者輸入資料，還有簡單的網頁顯示！繼續練習，慢慢你會發現 Python 是一個非常有趣的語言，能做很多事情哦！
