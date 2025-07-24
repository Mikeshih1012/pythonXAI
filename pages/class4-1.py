d1 = {}
d2 = {"apple": "蘋果"}
d3 = {1: "one", 2: "two", 3: "three"}

print(d3[2])
print(d2["apple"])


print("=" * 20)

for key in d3.keys():
    print(key)

print("-" * 20)

for value in d3.values():
    print(value)

print("-" * 20)

for key, value in d3.items():
    print(f"{key}:{value}")

print("-" * 20)

d3[2] = "二"
print(d3)
d3[4] = "four"
print(d3)
v = d3.pop(1)
print(d3)
print(f"刪除的值:{v}")
v = d3.pop(5, "不存在的鍵")
print(f"刪除的值:{v}")
print("d3的長度", len(d3))

print("-" * 20)

print(2 in d3)
print(1 in d3)
print("three" in d3)

print("-" * 20)

fruit = ["apple", "bannana", "cherry"]
print("bannana" in fruit)
print("orange" in fruit)
