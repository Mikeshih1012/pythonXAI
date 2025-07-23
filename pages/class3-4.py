i = 0
while i < 5:
    print(i)
    i += 1

print("-" * 20)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

print("-" * 20)

for i in range(5):
    if i == 3:
        break
    print(i)

print("-" * 20)

import random

count1 = 0
count2 = 0
count3 = 0
for i in range(100):
    n = random.randrange(1, 4)  # 產生1到3的隨機整數
    if n == 1:
        count1 += 1
    elif n == 2:
        count2 += 1
    else:
        count3 += 1

    print(n)
print(f"1的次數: {count1}, 2的次數: {count2}, 3的次數: {count3}")

print("-" * 20)

print(random.randrange(1, 1111))
print(random.randint(10, 20))
