import calVI as cal
x = int(input("Enter tempdiff : "))
t = cal.batcal(x)
print(' type  Series of parallel Enter   2 :')
Vol = int(input("Enter voltage : "))
Cr = int(input("Enter  Current : "))
print(t.getcurcuit(Vol,Cr))
