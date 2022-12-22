def fibonacci(n):
    i, x, y = 0, 0, 1
    if n == 0:
        return str(x)
    if 2>=n>=1 :
        return str(y)
    while i < n:
        z = x+y
        x = y
        y = z
        i += 1
    return str(x)


def lucas(n):
    i, x, y = 0, 2, 1
    if n == 0:
        return str(x)
    if 2>=n>=1 :
        return str(y)
    while i < n:
        z = x+y
        x = y
        y = z
        i += 1
    return str(x)

def sum_series(n,num1,num2):
    if num1:
        x = num1
    else:
        x = 0
    if num2:
        y = num2
    else:
        y = 1
    if n == 0:
        return str(x)
    if 2>=n>=1 :
        return str(y)
    i = 0
    while i < n:
        z = x+y
        x = y
        y = z
        i += 1
    return str(x)

