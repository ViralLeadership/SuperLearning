import datetime
start = datetime.datetime.now()
a, b = 0, 1
while b < 100000000000000:
    print(b)
    a, b = b, a + b

end = datetime.datetime.now()
runtime = end - start
print(runtime)
