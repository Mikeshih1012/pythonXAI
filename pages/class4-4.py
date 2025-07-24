def hello():
    print("hello")


def hello2(name):
    print("hello" + name)


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi


hello()
hello2("Mike")
print(my_max(10, 20))
print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.14159, 2))

print("-" * 20)

length = 5
area = 123


def calculate_square_area():
    area = length**2
    print("面積是", area)


def calculate_square_area2():
    area = length**2
    return area


def calculate_square_area3():
    global area
    area = length**2


length = 10
calculate_square_area()
print(calculate_square_area2())
calculate_square_area3()
print(area)

print("-" * 20)

x1 = input("x1:")
y1 = input("y1:")
x2 = input("x2:")
y2 = input("y2:")
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)


def distance():
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dis


print(distance())

print("-" * 20)
