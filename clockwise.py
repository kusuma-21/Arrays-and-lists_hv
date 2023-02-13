def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis
 
 
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    d = int(input("enter a number:"))
    N = len(arr)
 
    # Function call
    arr = rotate(arr, d, N)
    for i in arr:
        print(i, end=" ")