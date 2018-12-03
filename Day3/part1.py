canvas = {x:{y:0 for y in range(0,1000)} for x in range(0,1000)}

out=0

with open("Day3/Input.txt",'r') as f:
    while True:
        a = f.readline()
        if not a:
            break
        a = a.strip()
        a = a.split()
        x,y = [int(b) for b in a[2].replace(":","").split(',')]
        w,h = [int(b) for b in a[3].split('x')]
        for b in range(x,w+x):
            for c in range(y,h+y):
                if canvas[b][c] == 1:
                    out+=1
                canvas[b][c]+=1

print(out)