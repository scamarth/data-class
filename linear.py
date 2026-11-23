#Linear Search is a searching technique in which we check each element one by one until we find the required element.
arr = list(map(int,input("ENTER THE NUMBERS - ").split()))
key = int(input())
if key in arr:
    print("key exist")
for i in range(0,len(arr)):
    if arr[i] == key:
        print("key exist")
    else:
        print("doesn't exist")