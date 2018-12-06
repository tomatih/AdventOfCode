from pprint import pprint

data = []
with open("Day6/Input.txt",'r') as f:
    for line in f.readlines():
        data.append([int(x) for x in reversed(line.strip().replace("\n",'').split(","))])

size = 400
field = [['.' for x in range(0,size)] for y in range(0,size)]

ans = 0

for rowI,row in enumerate(field):
    for pointI,point in enumerate(row):
        total = 0
        for d in data:
            total += abs(rowI-d[0]) + abs(pointI-d[1])
        if total < 10000:
            ans+=1

print(ans)
