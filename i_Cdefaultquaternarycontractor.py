from easibex_utils import *

def i_Cdefaultquaternarycontractor(Z_p, W_p, X_p, Y_p, function_p):

    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("intervalx_adapt.dll")
    
    size_Z_p = len(Z_p)
    size_W_p = len(W_p)
    size_X_p = len(X_p)
    size_Y_p = len(Y_p)
    if ((size_Z_p != size_X_p) | (size_X_p != size_Y_p) | (size_X_p != size_W_p)):
        i_error('Error : Sizes must match.')
    
    if (type(X_p) is tuple):
        # vector<interval> or vector<box>.
        nb = len(X_p)
        m = 1 # Number of columns in the imatrix (should be 1 for interval and box, vector<imatrix> unsupported).
        if (type(X_p[1]) is list):
            if (type(X_p[1][1]) is list):
                if (type(X_p[1][1][1]) is list):
                    i_error('Error : Unhandled argument type.')
                else:
                    n = len(X_p[1]) # Box dimension.
            else:
                n = 1 # Box dimension (should be 1 for interval).
        else:
            i_error('Error : Unhandled argument type.')
    elif (type(X_p) is list):
        # interval, box or imatrix.
        nb = 1
        if (type(X_p[1]) is list):
            if (type(X_p[1][1]) is list):
                if (type(X_p[1][1][1]) is list):
                    i_error('Error : Unhandled argument type.')
                else:
                    # imatrix.
                    n = len(X_p[1]) # Box dimension.
                    m = len(X_p)
            else:
                n = len(X_p) # Box dimension.
                m = 1 # interval or box
        else:
            n = 1 # Box dimension (should be 1 for interval).
            m = 1 # interval or box
    else:
        i_error('Error : Unhandled argument type.')
    
    # Shape conversions suitable for the pointers to send to the library.
    pZ_p = i_intervalreshapetopointer(Z_p, nb, n, m)
    pW_p = i_intervalreshapetopointer(W_p, nb, n, m)
    pX_p = i_intervalreshapetopointer(X_p, nb, n, m)
    pY_p = i_intervalreshapetopointer(Y_p, nb, n, m)

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
    hApiParams = (1, "pZ_p", 0), (1, "pW_p", 0), (1, "pX_p", 0), (1, "pY_p", 0), (1, "nb", 0), (1, "n", 0), (1, "m", 0),
    function_call = hApiProto((function_p, hDll), hApiParams)

    function_call(pZ_p, pW_p, pX_p, pY_p, ctypes.c_uint(nb), ctypes.c_uint(n), ctypes.c_uint(m))
    
    # Conversions to human-readable format.
    Z = i_intervalreshapefrompointer(pZ_p, nb, n, m)
    W = i_intervalreshapefrompointer(pW_p, nb, n, m)
    X = i_intervalreshapefrompointer(pX_p, nb, n, m)
    Y = i_intervalreshapefrompointer(pY_p, nb, n, m)

    return Z, W, X, Y
