from __future__ import print_function
import ctypes

def error(*objs):
    print(*objs, file=sys.stderr)

def createpointer(nb, n, m):
    if (nb == 1):
        if (n > 1): 
            if (m > 1): 
                pX = (ctypes.c_double*(2*n*m))()
            else:
                pX = (ctypes.c_double*(2*n))()
        else:
            pX = (ctypes.c_double*2)()
    else:
        if (n > 1): 
            pX = (ctypes.c_double*(2*n*nb))()
        else:
            pX = (ctypes.c_double*(2*nb))()
    return pX

def reshapetopointer(X, nb, n, m):
    if (nb == 1):
        if (n > 1): 
            if (m > 1): 
                pX = (ctypes.c_double*(2*n*m))()
                for i in range(n):
                    for j in range(m):
                        index = 2*(n*j+i)
                        pX[index] = X[i][j][0]
                        pX[index+1] = X[i][j][1]
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
                    pX[index] = X[i][k][0]
                    pX[index+1] = X[i][k][1]
        else:
            pX = (ctypes.c_double*(2*nb))()
            for k in range(nb):
                index = 2*k
                pX[index] = X[k][0]
                pX[index+1] = X[k][1]
    return pX

def reshapefrompointer(pX, nb, n, m):
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
    return X
