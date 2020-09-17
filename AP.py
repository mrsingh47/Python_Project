def checkIsAP(arr, n):
    if (n == 1): return True

    arr.sort()
    d = arr[1] - arr[0]
    for i in range(2, n):
        if (arr[i] - arr[i - 1] != d):
            return False

    return True
arr = []
b = int(input("Enter number of elements : "))
for i in range(0, b):
    ele = int(input())
    arr.append(ele)
n = len(arr)
print("Yes, Given series is an AP") if (checkIsAP(arr, n)) else print("No, given series is not an AP")
d=arr[1] - arr[0]
last = arr[0]+((n-1) * d)
print("The nth term is",last) if (checkIsAP(arr, n)) else print("This is not AP")
sum = (n/2)*(arr[0] + last)
print('the sum of n terms are',sum) if (checkIsAP(arr, n)) else print("This is not AP")