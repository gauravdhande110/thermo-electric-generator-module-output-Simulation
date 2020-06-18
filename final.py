import flow as fl
import calVI as cal
#fl.cal_parallel_of_series(2,4)
#fl.cal_series_of_parallel(3,4)
print(' type  parrallel of series Enter     1 :')
print(' type  Series of parallel Enter      2 :')
print(' type  get best for VI input Enter   3 :')
g = int(input("Enter your type cal : "))
if g == 1 :
     m = int(input("parallel cnt:"))
     n = int(input("Series   cnt:"))
     fl.cal_parallel_of_series(m,n)
elif g==2 :
    m = int(input("Series   cnt:"))
    n = int(input("Parallel cnt:"))
    fl.cal_series_of_parallel(m,n)
else :
    x = int(input("Enter tempdiff : "))
    t = cal.batcal(x)
    print(' type  Series of parallel Enter   2 :')
    Vol = int(input("Enter voltage : "))
    Cr = int(input("Enter  Current : "))
    print(t.getcurcuit(Vol,Cr))
