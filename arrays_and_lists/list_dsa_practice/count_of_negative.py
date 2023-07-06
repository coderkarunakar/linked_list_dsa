#count of negative no with out inbuit
arr=[-1,-2,-3,-4,-8]
negative_count=0
for index in range(len(arr)):
    if arr[index]<0:
        negative_count+=1
print(negative_count)

