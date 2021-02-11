n = int(input("Number of terms: "))
a = 0
b = 1
count = 0
while count < n:
    print(a)
    r = a + b
    a = b
    b = r
    count += 1