def hash(a=0,b=0,line=''):
    hashstr = ''
    for i in line[a:b]:
        hashstr += str(i)
    return int(hashstr)

def RabinKarp(line = '', findLine = ''):
    counter = 0
    lenLine = len(line)
    lenFindline = len(findLine)
    for i in range(lenLine-lenFindline+1):
        flag = True
        hashLine = hash(i,i+lenFindline,line)
        hashFind = hash(0,lenFindline,findLine)
        if hashLine == hashFind:
            for j in range(lenFindline):
                if line[i+j] != findLine[j]:
                    flag = False
                    break
            if flag == True:
                counter += 1
    return counter