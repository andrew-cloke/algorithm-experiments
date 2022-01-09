# Print the first 'n' ugly numbers

def remove_factor(n,a):
    while (n % a)==0:
        n=n/a
    return n

def is_ugly(n):
    if n==1:
        return True

    n=remove_factor(n,2)
    if n==1:
        return True
    
    n=remove_factor(n,3)
    if n==1:
        return True

    n=remove_factor(n,5)
    if n==1:
        return True

    return False

def print_first_n_ugly_nums(n):
    cnt=0
    i=0
    while cnt<n:
        i+=1
        if is_ugly(i):
            print(i," ",end="")
            cnt+=1
    print("\n")

print_first_n_ugly_nums(20)
