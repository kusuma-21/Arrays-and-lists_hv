frequency = list(map(int,input().split()))
k = 0
number = frequency
for i in frequency:
    value = frequency.count(i)
    if(value> k):
        k = value
        number = i
 
print(number)
 
