arr=[]
n = int(input())
#take array when user input as 2 3 4 5 4 format and not user enter input in separate line formats
# converted to list to perform sort

arr = list(map(int, input().split(' ')))
arr.sort()
# remove duplicates from the list hence convert to dictionary, dictionary don't maintain duplicate keys

arr = list(dict.fromkeys(arr))
length=len(arr)

#the index points to runner up of the index one less than highest number stored

for i in range(0,length):
    if(i==(length-2)):
        runner_score=arr[i]
print(runner_score)
