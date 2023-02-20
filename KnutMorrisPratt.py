def piarr(line):
    pi = [0]
    j, i = 0, 1
    lenght = len(line)
    while i < lenght:
        if line[i] != line[j]:
            if j == 0:
                pi.append(0)
                i += 1
            else:
                j = pi[j - 1]
        else:
            pi.append(j + 1)
            i += 1
            j += 1
    return pi

def KnutMorissPratt(line, pattern):
    p, l = len(pattern), len(line)
    i, j = 0, 0
    counter = 0 
    pi = piarr(pattern)
    while i < l:
        if line[i] == pattern[j]:
            i += 1
            j += 1
            if j == p:
                counter += 1
                j = 0
        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1

    return counter