from datetime import datetime

data={}
times=[]
guards={}

#get input an prase is
with open("Day4/Input.txt")as f:
    for a in f.readlines():
        b=datetime.strptime(a[1:17],'%Y-%m-%d %H:%M')
        times.append(b)
        data[b] = a[19:].replace("\n",'')

#sort input and generate a usable list
times = sorted(times)
on_shift = None
sleep_start=None
for a in times:
    b = data[a]
    if b[0] == 'G':
        on_shift = int(b.split(" ")[1].replace("#",''))
    elif b[0] == 'f':
        sleep_start = a.minute
    elif b[0] =='w':
        try:
            tmp=guards[on_shift]
            tmp.append([sleep_start,a.minute-sleep_start])
            guards[on_shift] = tmp
        except Exception as e:
            guards[on_shift] = [[sleep_start,a.minute-sleep_start]]
    else:
        print("Something went horribly wrong")
del(on_shift)
del(sleep_start)
del(data)

#find the sleepest guard
longest=0
longestID=None
for ids in guards:
    sleeps = guards[ids]
    dr=0
    for st,dur in sleeps:
        dr+=dur
    if dr>longest:
        longest=dr
        longestID = ids

del(longest)

#find the most slept minute
mins = []
for a in range(0,60):
    b=0
    for sleep in guards[longestID]:
        if(a>=sleep[0] and a<sleep[0]+sleep[1]):
            b+=1
    mins.append(b)

#print output
print(longestID*mins.index(max(mins)))
