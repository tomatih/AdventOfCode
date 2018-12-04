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
            tmp.append([sleep_start,a.minute])
            guards[on_shift] = tmp
        except Exception as e:
            guards[on_shift] = [[sleep_start,a.minute]]
    else:
        print("Something went horribly wrong")
del(on_shift)
del(sleep_start)
del(data)

# get sleep frequencies for each minute
minutes=[]
for minute in range(0,60):
    most_frequent=None
    most_frequent_nr = 0
    for guard in guards:
        l=0
        for sleep in guards[guard]:
            if(minute>=sleep[0] and minute<sleep[1]):
                l+=1
        if l>most_frequent_nr:
            most_frequent_nr = l
            most_frequent = guard
    minutes.append([most_frequent,most_frequent_nr])

#find which minute was slept on the most and by who
longest=0
ids=None
minute = 0
for i,score in enumerate(minutes):
    if(score[1]>longest):
        longest=score[1]
        ids=score[0]
        minute=i

#print output
print(minute*ids)
