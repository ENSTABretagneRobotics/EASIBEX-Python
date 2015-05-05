from easibex import *
from vibes import vibes
# Do not forget to launch VIBes-viewer.exe!
#------------------------------------------------------------------------
def inside(X):
    X1=X[0]; X2=X[1]
    Y=i_Add(i_Sqr(X1),i_Sqr(X2))
    b=i_In(Y,[1,2])
    return b
#------------------------------------------------------------------------
def Cout(X):
    X1=X[0]; X2=X[1]; c=[2,2]
    #X2,X1,c=i_Csub(X2,X1,c)
    X2,X1=i_Ctan(X2,X1)
    #X1,X2=i_CinRing(X1,X2,1,2,[1,1.5])
    #X1,X2=i_SinRing(X1,X2,1,2,[1,1.5],1)
    r=[X1,X2]
    return r
#------------------------------------------------------------------------
#def Cin(X):
    #X1=X[0]; X2=X[1];
    ##[Xa1,Xa2]=i_CinRing(X1,X2,1,2,[-1,1])
    ##[Xb1,Xb2]=i_CinRing(X1,X2,1,2,[1.5,Inf])
    ##r=i_Union({[Xa1;Xa2];[Xb1;Xb2]})
    #[X1,X2]=i_SinRing(X1,X2,1,2,[1,1.5],0)
    #r=[X1;X2]
    #return r
#------------------------------------------------------------------------
def sivia(X):
    X0 = X
    vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='black[blue]',figure='sivia_easibex_vibes')
    X = Cout(X)
    vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='magenta[red]',figure='sivia_easibex_vibes')
    #X = Cin(X)
    #b=inside(X);
    #if b==[1 1]: vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='magenta[red]',figure='sivia_easibex_vibes')
    #elif b==[0 0]: vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='black[blue]',figure='sivia_easibex_vibes')
    #elif (i_Width(X)<0.1): vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='yellow[yellow]',figure='sivia_easibex_vibes')
    if (i_Width(X) < 0.25): vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='yellow[yellow]',figure='sivia_easibex_vibes')
    #if (i_decrease(X,X0)<0.1): vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='yellow[yellow]',figure='sivia_easibex_vibes')
    else:
        X1,X2 = i_Bisect(X)
        sivia(X1)
        sivia(X2)
# ----------------------  main   ----------------------------
print(vibes.channel, vibes.current_fig)
vibes.beginDrawing()
vibes.newFigure("sivia_easibex_vibes")
X=[[-4,4],[-4,4]]
#X=[[-0.4,0.4],[-0.4,0.4]]
vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='g[black]',figure='sivia_easibex_vibes')
#X=[[0,0.4],[-0.4,0.4]]
#vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='yellow[yellow]',figure='sivia_easibex_vibes')
#X=[[-0.4,0],[-0.4,0.4]]
#vibes.drawBox(X[0][0],X[0][1],X[1][0],X[1][1],color='magenta[red]',figure='sivia_easibex_vibes')
sivia(X)
vibes.endDrawing()
