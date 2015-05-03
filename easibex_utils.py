from __future__ import print_function
import ctypes

def i_error(*objs):
    print(*objs, file=sys.stderr)

def i_createpointer(nb, n, m, s, t):
    if (nb == 1):
        if (n > 1): 
            if (m > 1): 
                pX = (t*(s*n*m))()
            else:
                pX = (t*(s*n))()
        else:
            pX = (t*s)()
    else:
        if (n > 1): 
            pX = (t*(s*n*nb))()
        else:
            pX = (t*(s*nb))()
    return pX

def i_reshapefrompointer(pX, nb):
    X = []
    for k in range(nb):
        X.append(pX[k])
    return tuple(X)

def i_boolreshapefrompointer(pX, nb):
    X = []
    for k in range(nb):
        X.append(bool(pX[k]))
    return tuple(X)

def i_intervalreshapetopointer(X, nb, n, m):
    if (nb == 1):
        if (n > 1): 
            if (m > 1): 
                pX = (ctypes.c_double*(2*n*m))()
                for i in range(n):
                    for j in range(m):
                        index = 2*(n*j+i)
                        pX[index] = X[j][i][0]
                        pX[index+1] = X[j][i][1]
            else:
                pX = (ctypes.c_double*(2*n))()
                for i in range(n):
                    index = 2*i
                    pX[index] = X[i][0]
                    pX[index+1] = X[i][1]
        else:
            pX = (ctypes.c_double*2)()
            pX[0] = X[0]
            pX[1] = X[1]
    else:
        if (n > 1): 
            pX = (ctypes.c_double*(2*n*nb))()
            for i in range(n):
                for k in range(nb):
                    index = 2*(n*k+i)
                    pX[index] = X[k][i][0]
                    pX[index+1] = X[k][i][1]
        else:
            pX = (ctypes.c_double*(2*nb))()
            for k in range(nb):
                index = 2*k
                pX[index] = X[k][0]
                pX[index+1] = X[k][1]
    return pX

def i_intervalreshapefrompointer(pX, nb, n, m):
    if (nb == 1):
        if (n > 1): 
            if (m > 1): 
                X = []
                for j in range(m):
                    X_j = []
                    for i in range(n):
                        index = 2*(n*j+i)
                        X_j.append([pX[index],pX[index+1]])
                    X.append(X_j)
            else:
                X = []
                for i in range(n):
                    index = 2*i
                    X.append([pX[index],pX[index+1]])
        else:
            X = [pX[0],pX[1]]
    else:
        if (n > 1): 
            X = []
            for k in range(nb):
                X_k = []
                for i in range(n):
                    index = 2*(n*k+i)
                    X_k.append([pX[index],pX[index+1]])
                X.append(X_k)
        else:
            X = []
            for k in range(nb):
                index = 2*k
                X.append([pX[index],pX[index+1]])
        X = tuple(X)
    return X
