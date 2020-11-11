def sumOfArray(alice_ar,bob_ar):
    alice_sum=0
    bob_sum=0
    ar_len=len(alice_ar)
    for i in range(ar_len):
        if alice_ar[i]>bob_ar[i]:
            alice_sum=alice_sum+1
        elif bob_ar[i]>alice_ar[i]:
            bob_sum=bob_sum+1
        mark_comparison=[alice_sum,bob_sum]
    return mark_comparison
    
    

alice_ar = list(map(int, input().rstrip().split()))
bob_ar = list(map(int, input().rstrip().split()))
result=sumOfArray(alice_ar,bob_ar)
print(result[0],result[1])
