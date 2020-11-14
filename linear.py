# For example,you have to check if x which is int in arr which is array.
# At first, you'll use linear search.

def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


print("Hello! Please enter your favorite number!! if your entered number in array,this program would return index.if not, return -1.")
x = int(input())
arr = [20,30,4,50,10,3,4,5,6,7,3,8]

linearSearch(x,arr)