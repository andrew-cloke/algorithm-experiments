# Fibonacci Numers

def fibonacci(n):
    if n<2:
        return n
    
    a=0
    b=1
    for i in range(n-1):
        next=a+b
        a=b
        b=next
    return b

print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(9))

