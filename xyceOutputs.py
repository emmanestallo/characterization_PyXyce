import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from math import pi as pi 
from matplotlib.widgets import Cursor

def getThresholdIndex(vgs,vth):
    i = 0 
    while vgs[i] < vth[i]:
        i += 1 
    return i 

def getParameters(data_):
    cols = ["N(MN0:GM)","N(MN0:VTH)","N(MN0:CGD)","N(MN0:CGS)","N(MN0:GDS)","I(VD)","VG"]

    vth = data_[[cols[1]]].to_numpy()
    vgs = data_[[cols[6]]].to_numpy() 

    idx = getThresholdIndex(vgs,vth) 

    vgs = vgs[idx:]
    vth = vth[idx:]

    gm = data_[[cols[0]]].to_numpy()[idx:]
    cgd = -1*data_[[cols[2]]].to_numpy()[idx:]
    cgs = -1*data_[[cols[3]]].to_numpy()[idx:]
    gds = data_[[cols[4]]].to_numpy()[idx:]
    id = -1*data_[[cols[5]]].to_numpy()[idx:]

    cgg = cgs + cgd 

    vov = vgs - vth 
    gmro = np.divide(gm,gds)
    ft = np.divide(gm,2*pi*cgg)
    gmid = gm/id 
    ft_gmid = np.multiply(ft,gmid) 
    idw = id/1e-6 

    return vgs, id, vov, gmro, ft, gmid, ft_gmid, idw  


def plot (fig,ax,lengthValue,initialLength=0):
    ax[0][0].plot(vgs,id,label=f'length={initialLength+lengthValue}nm')
    ax[0][0].set_title('vgs vs id')
    ax[0][0].set_xlabel('vgs')
    ax[0][0].set_ylabel('id')

    ax[0][1].plot(vgs,vov,label=f'length={initialLength+lengthValue}nm')
    ax[0][1].set_title('vgs vs vov')
    ax[0][1].set_xlabel('vgs')
    ax[0][1].set_ylabel('vov')

    ax[0][2].plot(vgs,gmid,label=f'length={initialLength+lengthValue}nm')
    ax[0][2].set_title('vgs vs gm/id')
    ax[0][2].set_xlabel('vgs')
    ax[0][2].set_ylabel('gm/id')

    ax[1][0].plot(gmid,ft,label=f'length={initialLength+lengthValue}nm')
    ax[1][0].set_title('gm/id vs ft')
    ax[1][0].set_xlabel('gm/id')
    ax[1][0].set_ylabel('ft')

    ax[1][1].plot(gmid,gmro,label=f'length={initialLength+lengthValue}nm')
    ax[1][1].set_title('gm/id vs gm/gds')
    ax[1][1].set_xlabel('gm/id')
    ax[1][1].set_ylabel('gm/gds')

    ax[1][2].plot(gmid,idw,label=f'length={initialLength+lengthValue}nm')
    ax[1][2].set_title('gm/id vs id/w')
    ax[1][2].set_xlabel('gm/id')
    ax[1][2].set_ylabel('id/w')

def showGrid():
    ax[0][0].grid(linestyle='--')
    ax[0][1].grid(linestyle='--')
    ax[0][2].grid(linestyle='--')
    ax[1][0].grid(linestyle='--')
    ax[1][1].grid(linestyle='--')
    ax[1][2].grid(linestyle='--')

data_ = pd.read_csv('xyceNet.sp.csv')
nSweeps = int(input('Enter number of steps: '))
length = int(input('Enter step size: '))
initialLength=int(input('Enter initial length: '))

sweepInterval = int(len(data_)/nSweeps)

fig,ax = plt.subplots(2,3)

for i in range(nSweeps): 
    toProcess = data_[sweepInterval*i:sweepInterval*(i+1)]
    vgs, id, vov, gmro, ft, gmid, ft_gmid, idw = getParameters(toProcess)
    plot(fig,ax,(i+1)*length,initialLength)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
fig.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(0.01, 0.5), loc='center left')

showGrid()

cursor_00 = Cursor(ax[0][0], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)
cursor_01 = Cursor(ax[0][1], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)                
cursor_02 = Cursor(ax[0][2], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)
cursor_10 = Cursor(ax[1][0], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)
cursor_11 = Cursor(ax[1][1], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)
cursor_12 = Cursor(ax[1][2], horizOn = True, vertOn=True, color='black', linewidth=1, 
                useblit=True)


fig.tight_layout()
plt.show()