from easibex_utils import *

def i_Cdefaultunarycontractor(X_p, function_p):

    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("intervalx_adapt.dll")
    
    size_X_p = len(X_p)
    
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
    pX_p = i_intervalreshapetopointer(X_p, nb, n, m)

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_double), ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
    hApiParams = (1, "pX_p", 0), (1, "nb", 0), (1, "n", 0), (1, "m", 0),
    function_call = hApiProto((function_p, hDll), hApiParams)

    function_call(pX_p, ctypes.c_uint(nb), ctypes.c_uint(n), ctypes.c_uint(m))
    
    # Conversions to human-readable format.
    X = i_intervalreshapefrompointer(pX_p, nb, n, m)

    return X
