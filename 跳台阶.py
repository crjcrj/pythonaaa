def method(n):
    if n<=2:
        return n
    return method(n-1)+method(n-2)
print(method(4))