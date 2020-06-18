import calVI as te
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def cal_series_of_parallel(s,p):
    v=[]
    ic=[]
    w=[]
    plt.clf()
    for i in range (2,100):
        t = te.batcal(i)
        ic.append((t.calculate_s_of_p(s,p)[0])/100)
        v.append(t.calculate_s_of_p(s,p)[1])
        w.append(t.calculate_s_of_p(s,p)[2])
    pldf=pd.DataFrame({'x': range(2,100)})
    pldf['Current mA'] = ic
    pldf['voltage'] = v
    pldf['Watt'] =   w
    plt.title( ( str(s) + 'Series  of '+ str(p) +'in parllel // '+ str(s*p) +' TEG'))
    plt.xlabel('temperature diiff', fontsize=10)
    plt.ylabel('v in volts current in 100mA and watts vA', fontsize=10)
    plt.plot( 'x', 'Current mA', data=pldf, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.plot( 'x', 'voltage', data=pldf, marker='', color='olive', linewidth=2)
    plt.plot( 'x', 'Watt', data=pldf, marker='', color='olive', linewidth=2, linestyle='dashed', label="watt")
    plt.savefig(str(s)+str(p)+str(s*p)+'reportsp.png')
    plt.legend()
    plt.show()
def cal_parallel_of_series(p,s):
    v=[]
    ic=[]
    w=[]
    plt.clf()
    for i in range (2,100):
        t = te.batcal(i)
        ic.append((t.calculate_p_of_s(p,s)[0])/100)
        v.append(t.calculate_p_of_s(p,s)[1])
        w.append(t.calculate_p_of_s(p,s)[2])
    pldf=pd.DataFrame({'x': range(2,100)})
    pldf['Current mA'] = ic
    pldf['voltage'] = v
    pldf['Watt'] =   w
    plt.title( ( str(p) + 'parallel  of '+ str(s) +'in series // '+ str(s*p) +' TEG'))
    plt.xlabel('temperature diiff', fontsize=10)
    plt.ylabel('v in volts current in 100mA and watts vA', fontsize=10)
    plt.plot( 'x', 'Current mA', data=pldf, marker='', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    plt.plot( 'x', 'voltage', data=pldf, marker='', color='olive', linewidth=2)
    plt.plot( 'x', 'Watt', data=pldf, marker='', color='olive', linewidth=2, linestyle='dashed', label="watt")
    plt.savefig(str(s)+str(p)+str(s*p)+'reportps.png')
    plt.legend()
    plt.show()
