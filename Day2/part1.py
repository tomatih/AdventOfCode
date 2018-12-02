with open("Day2/Input.txt",'r') as f:
    data=f.read()
data=data.split('\n')

alphabet = [chr(x) for x in range(97,123)]

two=0
three=0
for a in data:
    tw=False
    th=False
    for b in alphabet:
        c = a.count(b)
        if c==2:
            tw=True
        elif c==3:
            th=True
    if tw:
        two+=1
    if th:
        three+=1

print(two*three)