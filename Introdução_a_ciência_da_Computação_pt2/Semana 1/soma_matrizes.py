def soma_matrizes(m1,m2):
    if (len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
    else:
        return False