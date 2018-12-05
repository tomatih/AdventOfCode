with open("Day5/Input.txt",'r') as f:
    data = f.read()

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

print(len(data)-1)