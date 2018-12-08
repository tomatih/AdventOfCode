with open("Day8/Input.txt",'r') as f:
    data = f.read()

data = [int(x) for x in data.split(" ")]
allMeta =[]

def get_node(start_i):
    childernL = data[start_i]
    metadataL = data[start_i+1]
    meta=[]
    metaS = start_i+2
    if childernL != 0:
        for a in range(0,childernL):
            metaS = get_node(metaS)
    for a in range(0,metadataL):
        meta.append(data[a+metaS])
    allMeta.append(meta)
    return metaS+metadataL

out=0
get_node(0)
for meta in allMeta:
    out+=sum(meta)

print(out)