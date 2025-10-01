# this code explains the merge sorting algorithm with help of leetcode problem number 912

def merge(nums, l, mid, r):  # function for merging sub arrays
    a = []
    b = []
    for i in range(l, mid+1):  # itetrate from 0 to mid elements of nums(array) and add into a
        a.append(nums[i])
    for i in range(mid+1, r+1):  # itetrate from  mid+1 to end  elements of nums(array) and add into b
        b.append(nums[i])
    i, j, k = 0, 0, l  # creating pointers

    while (k <= r):   # merging a and b into nums
        if j == len(b):
            nums[k] = a[i]
            i += 1
            k += 1
        elif i == len(a):
            nums[k] == b[j]
            j += 1
            k += 1
        elif a[i] < b[j]:
            nums[k] = a[i]
            i += 1
            k += 1
        else:
            nums[k] = b[j]
            j += 1
            k += 1


def mergesort(nums, l, r):  # functions that break problem into subproblems(recursion)
    # base case
    if l >= r:
        return
    # recursive case
    mid = (l+r)//2
    mergesort(nums, l, mid)
    mergesort(nums, mid+1, r)
    merge(nums, l, mid, r)


def sortary(nums):  # main function
    n = len(nums)-1
    mergesort(nums, 0, n)
    return nums


# calling a main function
print(sortary([3, 53, 25, 4, 25, 66, 4, 4, 3, 5, 6, 42, 55, 3245,]))
