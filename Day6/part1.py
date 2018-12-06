from pprint import pprint

data = []
with open("Day6/Input.txt",'r') as f:
    for line in f.readlines():
        data.append([int(x) for x in reversed(line.strip().replace("\n",'').split(","))])

size = 400
field = [['.' for x in range(0,size)] for y in range(0,size)]

for i,point in enumerate(data):
    field[point[0]][point[1]] = i

for rowI,row in enumerate(field):
    for pointI,point in enumerate(row):
        if point==".":
            distances=[]
            minD=size*size*2
            for d in data:
                dis = abs(rowI-d[0])+abs(pointI-d[1])
                distances.append(dis)
                if dis< minD:
                    minD=dis
            if distances.count(minD) == 1:
                field[rowI][pointI] = distances.index(minD)

sizes={x:0 for x in range(0,len(data)+1)}

inf = set()

for rowI,row in enumerate(field):
    for pointI,point in enumerate(row):
        if point != '.':
            if rowI == 0 or rowI == len(field)-1 or pointI == 0 or pointI == len(row)-1:
                inf.add(point)
            sizes[point]+=1

maxS=0
for a in sizes:
    if sizes[a] > maxS and not a in inf:
        maxS = sizes[a]

print(maxS)
