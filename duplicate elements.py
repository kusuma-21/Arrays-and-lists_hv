array = list(map(int,input().split()))
l = []
k = []
for i in array:
    if i not in l:
        l.append(i)
for i in l:
    if array.count(i) > 1:
        k.append(i)
print(*k,sep= ' ')



