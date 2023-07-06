#count of even and odd no in the list

arr=[2,1,5,4,6,8,18]
#initialilzing even count and oddd count as 0 and increasing even count after getting it
even_count=0
odd_count=0
for index in range(len(arr)):
    if arr[index]%2==0:
        even_count+=1

    if arr[index]%2!=0:
        odd_count+=1
print(even_count)
print(odd_count)