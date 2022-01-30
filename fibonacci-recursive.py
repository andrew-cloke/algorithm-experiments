# Fibonacci Numers - recursive approach

def fibonacci(n2,n1,count):
    if count!=0:
        sum=n2+n1
        print(sum," ", end="")
        fibonacci(n1,sum,count-1)

print("1 1 ", end="")
fibonacci(1,1,10)
print("\n")
