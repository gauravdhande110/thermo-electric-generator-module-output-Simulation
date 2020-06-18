def_t_diff = [20,40,60,80,100]
OP_voltage = [0.97,1.8,2.4,3.6,4.8]
Current = [225,368,469,558,669]

import numpy
import matplotlib.pyplot as plt
def calculateVI(tempd):
    mymodel = numpy.poly1d(numpy.polyfit(def_t_diff, OP_voltage, 3))
    myline = numpy.linspace(1, 130, 150)
    #plt.clf()
    #plt.scatter(def_t_diff,OP_voltage)
    #plt.plot(myline, mymodel(myline))
    #plt.scatter(tempd,mymodel(tempd))
    #plt.show()
    mymodelc = numpy.poly1d(numpy.polyfit(def_t_diff, Current, 3))
    mylinec = numpy.linspace(1, 130, 150)
    #plt.clf()
    #plt.scatter(def_t_diff,Current)
    #plt.plot(mylinec, mymodelc(mylinec))
    #plt.scatter(tempd,mymodelc(tempd))
    #plt.show()
    return mymodel(tempd),mymodelc(tempd)
#calculateVI(50)
