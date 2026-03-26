n = int(input("input n:"))

def prima(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(n-1, 1, -1):
    if prima(i):
        print(f"maka prima terdekat<{n} adalah {i}")
        break