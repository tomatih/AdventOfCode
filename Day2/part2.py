with open("Day2/Input.txt",'r') as f:
    data=f.read()
data=data.split('\n')

for i,a in enumerate(data):
    for b in range(i+1,len(data)):
        sim=0
        out=''
        for c in range(0,len(a)):
            if a[c]==data[b][c]:
                sim+=1
                out+=a[c]
        if sim==len(a)-1:
            print(out)
