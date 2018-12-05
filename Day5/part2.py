with open("Day5/Input.txt",'r') as f:
    Odata = f.read()

alphabet = {chr(x):0 for x in range(97,123)}

for a in range(97,123):
    data = Odata.replace(chr(a),'').replace(chr(a).upper(),'')
    last_len = len(data)
    while True:
        for letter in range(97,123):
            x = chr(letter)
            data = data.replace(x+x.upper(),"")
            data = data.replace(x.upper()+x,"")
        if last_len == len(data):
            break
        else:
            last_len = len(data)
    alphabet[chr(a)] = len(data)

shortest=''
shortest_v=len(Odata)
for a in alphabet:
    if alphabet[a] < shortest_v:
        shortest_v = alphabet[a]
        shortest = a

print(shortest_v-1)