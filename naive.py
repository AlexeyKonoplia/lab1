def naive(line = '', findLine = ''):
    lenLine = len(line)
    lenFindline = len(findLine)
    counter = 0
    for i in range(lenLine - lenFindline + 1):
        flag = True
        for j in range(lenFindline):
            if line[i+j] != findLine[j]:
                flag = False
                
                break
            
                
        if flag == True:        
            counter += 1

    return counter

#def RabinCarp(line = '', findLine = ''):