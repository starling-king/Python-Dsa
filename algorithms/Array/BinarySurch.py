arr=[87,382,37,87,23,55,38,94,11,6,2,5,6,67,43,40]

arr.sort();
print(*arr)
print(len(arr))
target=87

def binarysurch(target,arr):
    left,right=0,len(arr)-1

    while left<=right:
        
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid+1
    return -1

print(binarysurch(target,arr))