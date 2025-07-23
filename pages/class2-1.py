#


print(1 == 2)
print(1 != 2)
print(1 >= 2)
print(1 <= 2)
print(1 > 2)
print(1 < 2)

print(not True)
print(not False)

print(False and False)
print(False and True)
print(True and False)
print(True and True)

print(False or False)
print(False or True)
print(True or False)
print(True or True)  # True

# 練習: 密碼驗證
password = input("請輸入密碼: ")

if password == "1234":
    print("密碼正確")
else:
    print("密碼錯誤")

if password == "1234":
    print("歡迎Ray")
elif password == "5678":
    print("歡迎Mike")
elif password == "abcd":
    print("歡迎Alice")
else:
    print("密碼錯誤")

get = input("請輸入年份")
get = int(get)
if get % 4 == 0 and (get % 100 != 0 or get % 400 == 0):
    print(f"{get}年是閏年")
else:
    print(f"{get}年不是閏年")
