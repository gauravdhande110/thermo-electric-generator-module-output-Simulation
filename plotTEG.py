import calVI as te
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def TEG_graph(vol,cur):
    v=[]
    ic=[]
    w=[]
    plt.clf()
    for i in range (20,100):
        t = te.batcal(i)
        ic.append(t.getcurcuit(vol,cur)[0])
        v.append(t.getcurcuit(vol,cur)[1])
        w.append(t.getcurcuit(vol,cur)[0]*t.getcurcuit(vol,cur)[1])
    pldf=pd.DataFrame({'x': range(20,100)})
    pldf['Series'] = ic
    pldf['Parallel'] = v
    pldf['TEG'] =   w
    plt.title((str(vol)+'V'+str(cur)+'A Series parllel TEG'))
    plt.xlabel('temperature diiff', fontsize=10)
    plt.ylabel('No of TEG', fontsize=10)
    plt.xlim([20,100])
    plt.ylim([0,100])
    #plt.figure(figsize=(100,50))
    plt.plot( 'x', 'Series', data=pldf, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.plot( 'x', 'Parallel', data=pldf, marker='', color='olive', linewidth=2)
    plt.plot( 'x', 'TEG', data=pldf, marker='', color='red', linewidth=2, linestyle='dashed', label="TEGcount")
    plt.savefig(str(vol)+str(cur)+'reportTEGCNT.png')
    plt.legend()
    plt.show()
TEG_graph(12,1.5)
