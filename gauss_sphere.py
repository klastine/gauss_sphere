import math
import time
def prm(lst):
    inst = {}
    s = 1
    pts = 0
    w = math.factorial(len(lst))
    for item in lst:
        if item != 0:
            pts += 1
        if item in inst:
            inst[item] +=1
        else:
            inst[item] = 1

    for item in inst:
        s = s * math.factorial(inst[item])

    return math.floor(w/s) * (2 ** pts)

def point(dim, rad):
    points = []
    point = [0] * dim
    
    while(point[0]<=(rad/math.sqrt(dim))):
        points.append(tuple(point))
        ptLen = len(point)-1
        len2 = ptLen
        myBool = True
        while myBool:
            point[len2] += 1
            if point[len2] > (rad/math.sqrt(dim-len2)):
                len2 = len2 - 1
                if len2 == -1:
                    break
            else:
                myBool = False
        len2 = len2 + 1
        len3 = len2 - 1
        while len2 <= ptLen:
            point[len2] = point[len3]
            len2 += 1
    return points
            
def gss(dim, rad):
    start_time = time.time()
    out = 0
    points = point(dim,rad)
    for ptLen in points:
        total = 0
        for counter in ptLen:
            total = (counter ** 2) + total
        if total <= (rad ** 2):
            out += prm(ptLen)

    print("Function took", (time.time()-start_time),"seconds to execute.")
    return out
