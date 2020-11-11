#alice and bob are two students
#we enter alice marks as an array,enter bob marks as array, in respective consective order as per subject
#when for same subject if alice scores higher than bob,alice gets one mark
#when for same subject if bob scores higher than alice, bob gets one mark
#when both score same mark no score for both alice n bob
#print the final score alice and bob gets
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
#here printing the array gives wrong display in array form, therefor print respectively the elements in array
print(result[0],result[1])
