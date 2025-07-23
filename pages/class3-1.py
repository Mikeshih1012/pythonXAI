print(len([]))
print(len(["蘋果"]))
print(len("a" "b"))
print(len([1, 2, 3]))

print(("-" * 20))

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])

print(("-" * 20))

for element in l:
    print(element)

l[0] = "A"
l[2] = "c"
print(l)

print(("-" * 20))

a = [10, 20, 30]
b = a
b[1] = 100
print(a)

print("-" * 20)
c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)

print("-" * 20)

l1 = [1, 2, 3]
l1.append(4)
print(l1)

print("-" * 20)

l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")
print(l2)

print("-" * 20)

l3 = [1, 2, 3]
l3.pop()
print(l3)

print("-" * 20)

l4 = [1, 2, 3]
l4.pop(1)
print(l4)

print("-" * 20)

l5 = [3, 1, 5, 3.3, 4, 2]
l5.sort()
print(l5)

l6 = ["banana", "apple", "orange"]
l6.sort()
print(l6)
