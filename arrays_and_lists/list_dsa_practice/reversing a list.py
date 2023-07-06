# 16. Write a python program to find reverse of an list.
arr=[1,2,3,4,5]
print(arr[::-1])

#2nd using reverse()
arr.reverse()
print(arr)

#2 pointer approach
# Reversing a list using two-pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
 
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))