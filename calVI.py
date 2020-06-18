import matplotlib.pyplot as pt
import pandas as pd
import predictor as p
class batcal:
    V = 1
    I = 1
    t1 = 0
    t2 = 0

    def __init__ (self,set_a):
        self.V,self.I = p.calculateVI(set_a)
    def calculate_s_of_p(self,cnt_s,cnt_p):
        return cnt_p*self.I,cnt_s*self.V,cnt_p*self.I*cnt_s*self.V/1000
    def calculate_p_of_s(self,cnt_p,cnt_s):
        return cnt_p*self.I,cnt_s*self.V,cnt_p*self.I*cnt_s*self.V/1000
    def getcurcuit(self,vol,cur):
        x = vol/self.V
        y = cur*1000/self.I
        if x < round(x):
            x=round(x)
        else:
            x=round(x)+1;
        if y < round(y):
            y=round(y)
        else:
            y = round(y)+1;
        return x,y

#test = batcal(50)
#print(test.calculate_s_of_p(2,3))
#print(test.calculate_p_of_s(2,3))
#print(test.calculate_p_of_s(1,6))
#print(p.calculateVI(45))
