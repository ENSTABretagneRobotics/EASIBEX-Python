from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def drawbox(X,colin,colout):
    x1=X[0][0]; x2=X[1][0]; 
    y1=X[0][1]; y2=X[1][1]; 
    fig,ax = plt.subplots()
    currentAxis = plt.gca()
    currentAxis.add_patch(Rectangle((x1, y1), x2-x1, y2-y1, facecolor=colin, edgecolor=colout, fill=True))#, linewidth=2.0, alpha=1))
    plt.show()
