res=0
data=None
with open("Day1/Input.txt",'r') as f:
    data=f.read()
data=data.split('\n')

cases=[]
flag=True
while flag:
    for a in data:
        res = eval("res"+a)
        if res in cases:
            print(res)
            flag=False
            break
        else:
            cases.append(res)

#print(res)