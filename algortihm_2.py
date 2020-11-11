#program to get summation of an array using a function

def sumOfArray(ar):
    sum=0
    for i in range(ar_count):
        sum=sum+ar[i]
    return sum

    
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
res=sumOfArray(ar)
print(res)
