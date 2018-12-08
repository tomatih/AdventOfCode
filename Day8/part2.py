with open("Day8/Input.txt",'r') as f:
    data = f.read()

data = [int(x) for x in data.split(" ")]

def get_node(start_i):
    childernL = data[start_i]
    metadataL = data[start_i+1]
    meta=0
    metaS = start_i+2
    vals=[]
    if childernL != 0:
        for a in range(0,childernL):
            v,metaS = get_node(metaS)
            vals.append(v)
    if childernL  == 0:
        for a in range(0,metadataL):
            meta+=(data[a+metaS])
    else:
        for a in range(0,metadataL):
            v = data[a+metaS]
            if v <= childernL:
                meta+=vals[v-1]
    return [meta,metaS+metadataL]
        


out,a =get_node(0)

print(out)