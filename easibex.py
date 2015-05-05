from i_Cdefaultunarycontractor import *
from i_Cdefaultbinarycontractor import *
from i_Cdefaultternarycontractor import *
from i_Cdefaultquaternarycontractor import *
from i_Cdefaultquinarycontractor import *
from i_defaultboolfn1arg import *
from i_defaultboolfn2arg import *
from i_defaultdoublefn1arg import *
from i_defaultdoublefn2arg import *
from i_defaultfn1arg import *
from i_defaultfn2arg import *
from i_defaultibooleanfn2arg import *
from i_defaultintervalfn2arg import *
from i_defaultintfn1arg import *
from i_Bisect import *


# Should use NumPy arrays...?
# http://wiki.scipy.org/NumPy_for_Matlab_Users


# To define an interval :
# x = [-2,2]
# x[1] would be 2.
# Empty : 
# x = [NaN,NaN]
# Infinity : 
# x = [-Inf,Inf]

# To define a box :
# x = [[-2,2],[2,4],[-4,1]]

# To define an imatrix :
# x = [[[-2,2],[2,4],[-4,1]],[[-1,5],[-5,8],[-7,2]],[[-1,1],[0,2],[1,2]],[[-2,2],[2,8],[-1,2]]]

# To define a vector<interval> :
# x = ([-2,2],[2,4],[-4,1])
# This will be represented by a Python tuple.

# To define a vector<box> :
# x = ([[-2,2],[2,4],[-4,1]],[[-1,5],[-5,8],[-7,2]],[[-1,1],[0,2],[1,2]],[[-2,2],[2,8],[-1,2]])
# This will be represented by a Python tuple.

# iboolean : itrue -> [1,1], ifalse -> [0,0], iperhaps -> [0,1].

# Z = i_Add([0,2], [-1,2])
# Z = i_Add([[0,1],[0,10],[0,10]], [[-1,0],[2,5],[-1,0]])
# X = [[[-2,2],[2,4],[-4,1]],[[-1,5],[-5,8],[-7,2]],[[-1,1],[0,2],[1,2]],[[-2,2],[2,8],[-1,2]]]
# Y = [[[-4,1],[1,2],[-3,2]],[[-5,1],[-4,7],[-4,1]],[[-3,2],[2,2],[-1,0]],[[0,1],[-2,0],[-3,1]]]
# Z = i_Add(X,Y)
# X = ([[-2,2],[2,4],[-4,1]],[[-1,5],[-5,8],[-7,2]],[[-1,1],[0,2],[1,2]],[[-2,2],[2,8],[-1,2]])
# Y = ([[-4,1],[1,2],[-3,2]],[[-5,1],[-4,7],[-4,1]],[[-3,2],[2,2],[-1,0]],[[0,1],[-2,0],[-3,1]])
# Z = i_Add(X,Y)

# Z, X, Y = i_Cadd([-10,1], [0,2], [-1,2])
# Z, X, Y = i_Cadd([[-10,10],[2,10],[10,11]], [[0,1],[0,10],[0,10]], [[-1,0],[2,5],[-1,0]])

NaN = float('NaN')
Inf = float('Inf')

#----------------------------------------------------------------------
# Operators
#----------------------------------------------------------------------

def i_Add(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Addx')
    return Z

def i_Sub(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Subx')
    return Z

def i_Mul(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Mulx')
    return Z

def i_Div(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Divx')
    return Z

#----------------------------------------------------------------------
# Functions
#----------------------------------------------------------------------

def i_Min(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Minx')
    return Z

def i_Max(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Maxx')
    return Z

def i_Abs(X_p):
    Y = i_defaultfn1arg(X_p, 'Absx')
    return Y

def i_Sqr(X_p):
    Y = i_defaultfn1arg(X_p, 'Sqrx')
    return Y

def i_Sqrt(X_p):
    Y = i_defaultfn1arg(X_p, 'Sqrtx')
    return Y

def i_Exp(X_p):
    Y = i_defaultfn1arg(X_p, 'Expx')
    return Y

def i_Log(X_p):
    Y = i_defaultfn1arg(X_p, 'Logx')
    return Y

def i_Cos(X_p):
    Y = i_defaultfn1arg(X_p, 'Cosx')
    return Y

def i_Sin(X_p):
    Y = i_defaultfn1arg(X_p, 'Sinx')
    return Y

def i_Tan(X_p):
    Y = i_defaultfn1arg(X_p, 'Tanx')
    return Y

def i_Acos(X_p):
    Y = i_defaultfn1arg(X_p, 'Acosx')
    return Y

def i_Asin(X_p):
    Y = i_defaultfn1arg(X_p, 'Asinx')
    return Y

def i_Atan(X_p):
    Y = i_defaultfn1arg(X_p, 'Atanx')
    return Y

def i_Transpose(X_p):
    Y = i_defaultfn1arg(X_p, 'Transposex')
    return Y

def i_Concat(X_p, Y_p):
    Z = i_defaultfn2arg(X_p, Y_p, 'Concatx')
    return Z

def i_Size(X_p):
    r = i_defaultintfn1arg(X_p, 'Sizex')
    return r

def i_Inf(X_p):
    y = i_defaultfn1arg(X_p, 'Infx')
    return y

def i_Sup(X_p):
    y = i_defaultfn1arg(X_p, 'Supx')
    return y

def i_Center(X_p):
    y = i_defaultfn1arg(X_p, 'Centerx')
    return y

def i_Width(X_p):
    r = i_defaultdoublefn1arg(X_p, 'Widthx')
    return r

def i_Volume(X_p):
    r = i_defaultdoublefn1arg(X_p, 'Volumex')
    return r

# r = i_In([[10,15],[10,15]], [[11,12],[11,12]])
# iboolean : itrue -> [1,1], ifalse -> [0,0], iperhaps -> [0,1].
# Return an iboolean.
def i_In(X_p, Y_p):
    r = i_defaultibooleanfn2arg(X_p, Y_p, 'Inx')
    return r

#----------------------------------------------------------------------
# Contractors
#----------------------------------------------------------------------

def i_Cabs(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cabsx')
    return Y, X

def i_Cadd(Z_p, X_p, Y_p):
    [Z, X, Y] = i_Cdefaultternarycontractor(Z_p, X_p, Y_p, 'Caddx')
    return Z, X, Y

def i_Cantisym(X_p):
    X = i_Cdefaultunarycontractor(X_p, 'Cantisymx')
    return X

def i_Catan(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Catanx')
    return Y, X

def i_Cboolean(X_p):
    X = i_Cdefaultunarycontractor(X_p, 'Cbooleanx')
    return X

def i_Ccos(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Ccosx')
    return Y, X

def i_Cdet(Z_p, V_p, W_p, X_p, Y_p):
    [Z, V, W, X, Y] = i_Cdefaultquinarycontractor(Z_p, V_p, W_p, X_p, Y_p, 'Cdetx')
    return Z, V, W, X, Y

def i_Cdist(Z_p, V_p, W_p, X_p, Y_p):
    [Z, V, W, X, Y] = i_Cdefaultquinarycontractor(Z_p, V_p, W_p, X_p, Y_p, 'Cdistx')
    return Z, V, W, X, Y

def i_Cdiv(Z_p, X_p, Y_p):
    [Z, X, Y] = i_Cdefaultternarycontractor(Z_p, X_p, Y_p, 'Cdivx')
    return Z, X, Y

def i_Cequal(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cequalx')
    return Y, X

def i_Cexp(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cexpx')
    return Y, X

def i_Cgeq(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cgeqx')
    return Y, X

def i_Cinteger(X_p):
    X = i_Cdefaultunarycontractor(X_p, 'Cintegerx')
    return X

def i_Cmax(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cmaxx')
    return Y, X

def i_Cmin(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cminx')
    return Y, X

def i_Cmul(Z_p, X_p, Y_p):
    [Z, X, Y] = i_Cdefaultternarycontractor(Z_p, X_p, Y_p, 'Cmulx')
    return Z, X, Y

def i_Cnorm(N_p, X_p, Y_p):
    [N, X, Y] = i_Cdefaultternarycontractor(N_p, X_p, Y_p, 'Cnormx')
    return N, X, Y

def i_Cnorm3D(N_p, X_p, Y_p, Z_p):
    [N, X, Y, Z] = i_Cdefaultquaternarycontractor(N_p, X_p, Y_p, Z_p, 'Cnormx')
    return N, X, Y, Z

def i_Cnotin(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Cnotinx')
    return Y, X

def i_Cortho(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Corthox')
    return Y, X

def i_Crot(X_p):
    X = i_Cdefaultunarycontractor(X_p, 'Crotx')
    return X

def i_Cscal(Z_p, V_p, W_p, X_p, Y_p):
    [Z, V, W, X, Y] = i_Cdefaultquinarycontractor(Z_p, V_p, W_p, X_p, Y_p, 'Cscalx')
    return Z, V, W, X, Y

def i_Csign(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Csignx')
    return Y, X

def i_Csin(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Csinx')
    return Y, X

def i_Csqr(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Csqrx')
    return Y, X

def i_Csub(Z_p, X_p, Y_p):
    [Z, X, Y] = i_Cdefaultternarycontractor(Z_p, X_p, Y_p, 'Csubx')
    return Z, X, Y

def i_Ctan(Y_p, X_p):
    [Y, X] = i_Cdefaultbinarycontractor(Y_p, X_p, 'Ctanx')
    return Y, X
