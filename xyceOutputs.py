import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from math import pi as pi 

def getThresholdIndex(vgs,vth,initial,final):
    i = 0 
    while vgs[i] < vth[i]:
        i += 1 
    return i 

def getParameters(fileName,initial,final):
    data_ = pd.read_csv(fileName) 

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

def plot ():
    fig,ax = plt.subplots(2,3)
    
    ax[0][0].plot(vgs,id)
    ax[0][0].set_title('vgs vs id')
    ax[0][0].set_xlabel('vgs')
    ax[0][0].set_ylabel('id')
    ax[0][0].grid()

    ax[0][1].plot(vgs,vov)
    ax[0][1].set_title('vgs vs vov')
    ax[0][1].set_xlabel('vgs')
    ax[0][1].set_ylabel('vov')
    ax[0][1].grid()

    ax[0][2].plot(vgs,gmid)
    ax[0][2].set_title('vgs vs gm/id')
    ax[0][2].set_xlabel('vgs')
    ax[0][2].set_ylabel('gm/id')
    ax[0][2].grid()

    ax[1][0].plot(gmid,ft)
    ax[1][0].set_title('gm/id vs ft')
    ax[1][0].set_xlabel('gm/id')
    ax[1][0].set_ylabel('ft')
    ax[1][0].grid()

    ax[1][1].plot(gmid,gmro)
    ax[1][1].set_title('gm/id vs gm/gds')
    ax[1][1].set_xlabel('gm/id')
    ax[1][1].set_ylabel('gm/gds')
    ax[1][1].grid()

    ax[1][2].plot(gmid,ft_gmid)
    ax[1][2].set_title('gm/id vs ft*gm/id')
    ax[1][2].set_xlabel('gm/id')
    ax[1][2].set_ylabel('ft*gm/id')
    ax[1][2].grid()


vgs, id, vov, gmro, ft, gmid, ft_gmid, idw = getParameters('xyceNet.sp.csv')

plot()
plt.tight_layout()
plt.show()



