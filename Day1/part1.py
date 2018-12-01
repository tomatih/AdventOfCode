res=0
data=None
with open("Day1/Input.txt",'r') as f:
    data=f.read()
data=data.split('\n')

for a in data:
    res = eval("res"+a)

print(res)