from easibex_utils import *

# X1, X2 = i_Bisect([[-10,10],[2,10],[10,11]])
def i_Bisect(X_p):

    # Put DLL in global and load elsewhere?

    # Load DLL into memory.
    hDll = ctypes.CDLL("intervalx_adapt.dll")

    size_X_p = len(X_p)

    if (type(X_p) is list):
        # interval or box.
        if (type(X_p[1]) is list):
            n = len(X_p) # Box dimension.
        else:
            n = 1 # Box dimension (should be 1 for interval).
    else:
        i_error('Error : Unhandled argument type.')

    # Shape conversions suitable for the pointers to send to the library.
    pX_p = i_intervalreshapetopointer(X_p, 1, n, 1)
    pX1 = i_createpointer(1, n, 1, 2, ctypes.c_double)
    pX2 = i_createpointer(1, n, 1, 2, ctypes.c_double)

    hApiProto = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_uint)
    hApiParams = (1, "pX_p", 0), (1, "pX1", 0), (1, "pX2", 0), (1, "n", 0),
    function_call = hApiProto(('Bisectx', hDll), hApiParams)

    function_call(pX_p, pX1, pX2, ctypes.c_uint(n))
    
    # Conversions to human-readable format.
    X1 = i_intervalreshapefrompointer(pX1, 1, n, 1)
    X2 = i_intervalreshapefrompointer(pX2, 1, n, 1)
    return X1, X2
