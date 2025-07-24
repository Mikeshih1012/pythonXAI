"""
5
6
7
"""

# 單行註解

# print("Hello World")

print(6438)  # 輸出整數
print(3.14)  # 輸出浮點數
print(True)  # 輸出布林值
print(False)  # 輸出布林值
print("Hello World")  # 輸出字串
print("y" + "e" * 100)

a = 10  # 建立變數
print(a)
a = 20
print(a)  # 重新賦值
a = "aplle"  # 變更為字串
print(a)

x = 4
x = x + 3
print(x)
x = x * 2
print(x)

print(7 + 3)  # 加法
print(7 - 3)  # 減法
print(7 * 3)  # 乘法
print(7 / 3)  # 除法
print(7 // 3)  # 整數除法
print(7 % 3)  # 取餘數
print(2**3)  # 指數運算

v1 = 0.1
v2 = 0.2
print(v1 + v2)

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2  # 字串連接
print(s1 + s2)
print(s3)
print(s1 + s2 * 3)

name = "Python"
age = 31
new_str = f"我是{name}, 今年{age}歲"
print(new_str)

print(len(""))
print(len("Hello"))

print(type(True))  # 布林職類型
print(type(123))  # 整數類型
print(type(123.0))  # 浮點數類型
print(type("Hello"))  # 字串類型

print(int(True))
print(int(123))
# print(int("hello"))
print(int(3.14))

print(float(True))
print(float(123))
# print(float(hello))

print(bool(0))
print(bool(1))
print(bool(-2))
print(bool("hello"))
print(bool(""))

print(str(True))
print(str(1000))
print(str("yes"))

# get= input()
get = input("請輸入數字: ")
print(get)
print(type(get))

get = input("請輸入半徑長度")
get = int(get)
area = 3.14 * get**2
# print(get**2 * 3.14)
print(f"圓的面積為: {area}")
