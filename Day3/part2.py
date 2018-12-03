canvas = {x:{y:0 for y in range(0,1000)} for x in range(0,1000)}

data=[]

with open("Day3/Input.txt",'r') as f:
    while True:
        a = f.readline()
        if not a:
            break
        a = a.strip()
        a = a.split()
        x,y = [int(b) for b in a[2].replace(":","").split(',')]
        w,h = [int(b) for b in a[3].split('x')]
        cid = int(a[0][1:])
        data.append((cid,x,y,w,h))
        for b in range(x,w+x):
            for c in range(y,h+y):
                if canvas[b][c]==0:
                    canvas[b][c]=cid
                else:
                    canvas[b][c]='X'


for i,x,y,w,h in data:
    over=0
    for b in range(x,w+x):
        for c in range(y,h+y):
            if canvas[b][c] =='X':
                over+=1
    if not over:
        print(i)