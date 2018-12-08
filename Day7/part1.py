instr = {chr(x).upper():[] for x in range(97,123)}
with open("Day7/Input.txt",'r') as f:
    for line in f.readlines():
        one = line[5:6]
        two = line[36:37]
        instr[two].append(one)

to_do=[]
out=""
last=''

while True:
    for a in instr:
        if last in instr[a]:
            instr[a].remove(last)
        if instr[a] == [] and not a in out:
            instr[a] = ()
            to_do.append(a)
    to_do.sort()
    tmp = to_do[0]
    to_do.remove(tmp)
    out+=tmp
    last=tmp
    if len(out) == len(instr):
        break
print(out)
