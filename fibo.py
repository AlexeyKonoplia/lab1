def fibonacci1(n):
    a, b = 1, 0
    arr = []

    for i in range(n):
        a, b = b, a + b
        arr.append(a)
    return arr
def fibonacci(n):
    mainLine = ''
    arr = fibonacci1(n)
    for i in range(len(arr)):
        mainLine += str(arr[i])
    return mainLine