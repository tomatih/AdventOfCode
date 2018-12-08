parts = {chr(x).upper():[] for x in range(97,123)}#23)}
with open("Day7/Input.txt",'r') as f:
    for line in f.readlines():
        req = line[5:6]
        part = line[36:37]
        parts[part].append(req)

statuses = {chr(x).upper():0 for x in range(97,123)}#23)}
workers = [[] for x in range(0,5)]
to_do=[]
time_spent=0
while True:
    for i,w in enumerate(workers):
        if w!=[] and w[1] == 0:
            statuses[w[0]]+=1
            workers[i] = []
    
    for part in parts:
        if parts[part] != []:
            for req in parts[part]:
                if statuses[req] == 2:
                    parts[part].remove(req)
        if parts[part] == [] and statuses[part] == 0 and not part in to_do:
            to_do.append(part)

    if  to_do == [] and workers == [[] for x in range(0,5)]:
        break

    to_do.sort()
    for i,w in enumerate(workers):
        if w == [] and to_do != []:
            tmp = to_do[0]
            statuses[tmp]+=1
            workers[i] = [tmp, ord(tmp)-4]
            to_do.remove(tmp)
        if workers[i] != []:
            workers[i][1]-=1        
    time_spent+=1
print(time_spent)