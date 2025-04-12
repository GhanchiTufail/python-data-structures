def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot =arr[0]
    left = []
    right = []

    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
        
    return quick_sort(left) + [pivot] + quick_sort(right)
    

arr = [1,2,5,3,5,8,5,3,2,6,85,3,2,4,5]
print(quick_sort(arr))