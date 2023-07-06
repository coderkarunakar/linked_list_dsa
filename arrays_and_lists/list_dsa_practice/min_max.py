# #min vs max in an list

# #1st approach

# arr = [10, 89, 9, 56, 4, 80, 8]
# #assigned 0th index as our mini  and maxi first
# mini=arr[0]
# maxi=arr[0]
# #a loop to traverse over the array
# for i in range(len(arr)):
#     #if our array index element is less than our created mini then change it same with maxi 
#     if arr[i]<mini:
#         mini=arr[i]
#     if arr[i]>maxi:
#         maxi=arr[i]
# print(mini)
# print(maxi)



# #2nd approach after sort we can use list indexing
# arr=[9,8,7,6,1]
# arr.sort()
# print(arr[-1],"max value in the list")
# print(arr[0],"min value in the list")

#3rd approach using min max built in function

#3rd approach using inbuilt max and min and finding its index with inbuilt index
arr=[9,8,7,6,1]
#it shows just min value index and max value index
print(arr.index(min(arr)))
print(arr.index(max(arr)))