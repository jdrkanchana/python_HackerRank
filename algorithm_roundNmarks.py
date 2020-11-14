#grades is an array to store all the grades
#score a value between 0 to 100
#if value less than 40 fail
#if value difference between a five divisor like 55,75 or 80, or 90 is less than 3 round to nearest grade which is divisor  of 5
grades=[]
grades_count = int(input().strip())

for x in range(grades_count):
    grades_item = int(input().strip())
    last_digit= grades_item % 10
    if(grades_item>37):
        if (last_digit==4 or last_digit==9):
            grades_item=grades_item+1
        if (last_digit==3 or last_digit==8):
            grades_item=grades_item+2
    grades.append(grades_item)
    
for y in range(grades_count):
    print(grades[y])
