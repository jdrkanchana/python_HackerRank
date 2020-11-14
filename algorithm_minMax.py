
sum=0
# here the user input taken as array, or list
arr = list(map(int, input().rstrip().split()))
min=arr[0]
max=arr[0]

#taken sum of all user input
for i in range(len(arr)):
    sum=sum+arr[i]
    
#find the miniumum number in user input, and maximum number in user input
for x in range(len(arr)):
    if (arr[x]>max):
        max=arr[x]
    if (arr[x]<min):
        min=arr[x]
    
max_sum=sum-min
min_sum=sum-max

print(min_sum,max_sum)
