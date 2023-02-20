def BoyerMeow(line='', findline=''):
    lenLine = len(line)
    lenFindLine = len(findline)
    counter = 0
    type = 0
    for i in range(0,lenLine-(lenFindLine-1)):
        if type > 0:
            type -= 1
            continue
        a = line[i:i+lenFindLine]
        error,type = predproc(a,findline)
        if error == True: counter += 1
        #if error == -1: counter += 1  #ser = a[len(pref):].find(findline[:len(pref)+1])

    i = 0
    return counter

def predproc(a,b):
    if a:
        #print(a,b)
        if a[-1] == b[-1]:
            t = predproc(a[:-1],b[:-1])
            if t[0] == False:
                return False,t[1]
            else:
                return True,t[1]
        else: return False,b.rfind(a[-1])
    return True, 0