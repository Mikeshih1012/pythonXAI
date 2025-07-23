import random

table = []

for i in range(100):
    table.append(0)

target = random.randint(1, 100)
table[target - 1] = 1

count = 0

while True:
    pick = random.randint(1, 100)
    count += 1
    if table[pick - 1] == 2:
        print(f"已經被抽過了")
        count -= 1
    elif table[pick - 1] == 1:
        print(f"恭喜你抽到一番賞")
        break
    else:
        print(f"沒中獎,繼續")
    table[pick - 1] = 2

print(f"總共抽了{count}次, 花費{count*200}元")
