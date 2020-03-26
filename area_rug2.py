[n, s] = map(int, input().split())
arr = []



for i in range(0,n):
    row =   input()
    arr.append(row)

ddict = dict()

dirtdict = dict()

def s_row(i,j): # number of dirt covered in row starting at (i,j)
    count = 0
    for k in range(j, j+s):
        if arr[i][k] == "D":
            count +=1
    return count

def s_col(i,j): # number of dirt covered in column starting at (i,j)
    count = 0
    for k in range(i, i+s):
        if arr[k][j] == "D":
            count +=1
    return count

# Top left placement:
d_covered = 0
for x in range(s):
    for y in range(s):
        if arr[x][y] == "D":
            d_covered += 1
ddict[d_covered] = 1
dirtdict[(0,0)] = d_covered

for x in range(0,n-s+1):
    for y in range(0, n-s+1):
        # print((x,y))
        if (x,y) not in dirtdict:
            num_dirty = dirtdict[(x,y-1)] + s_col(x,y-1+s) - s_col(x,y-1)
            dirtdict[(x,y)] = num_dirty 

            if num_dirty in ddict:
                ddict[num_dirty] +=1
            else:
                ddict[num_dirty] =1
    y = 0
    if x+1 <= n-s:
        num_dirty =  dirtdict[(x,y)] + s_row(x+s, y) - s_row(x,y)
        dirtdict[(x+1,y)] = num_dirty

        if num_dirty in ddict:
            ddict[num_dirty] +=1
        else:
            ddict[num_dirty] = 1

# print(dirtdict)

# print(len(dirtdict))

# print(ddict)

# print(s_row(1,0))
# print(s_col(0,1))

# i+1, j = i,j + s_row(i+s, j) - s_row(i,j)

# i, j+1 = i,j + s_col(i, j+s) - s_col(i,j)











output = []
for key in ddict:
    output.append([key, ddict[key]])
output.sort()
#print(output)

for i in output:
    print(str(i[0]) + " " + str(i[1]))
