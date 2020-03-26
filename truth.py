n = int(input())
arr=[]
for i in range(n):
    line = map(int, input().split())
    line = list(line)
    arr.append(line)
#print(arr)

def func(n):
    for i in range(n,0,-1):
        # check if i is the number
        count = 0
        for tup in arr:
            if tup[0] <= i <= tup[1] :
                count += 1
        if i == count:
            return i
    return -1

print(func(n))