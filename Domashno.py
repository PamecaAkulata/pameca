import math
import time

total=[]
sum=0
print("Vuvedete informaciq za izbranite stoki")
print("Vuvedete koda na stoka 00 za krai na vuvejdaneto")
def format_stoka (x, y, z):
    s="%.2f"% (y*z)
    line="{x} ... x {z} ... {s} lv.".format(x=x,z=z,s=s)
    return line
def resto(y,x):
    return y-x
while True:
    cod=input("Vuvedete kod na stoka: ")
    if cod=="00":
        break
cena=float(input("Vuvedete cena na stokata: "))
broi=int(input("Vuvedete broi stoki: "))
total.append(format_stoka(cod,cena,broi))
sum+=cena*broi
print()
print("KASOVA BELEJKA:" .center(35))
print("="*35)
for i in range(0,len(total)):
    print(total[i].rjust(35))
    s="%.2f"% (sum)
    sl="OBSHTA SUMA: ..... {s} lv.".format(s=s)
print(sl.rjust(35))
print("\t","BROI STOKI: ..... ",broi)
print(time.strftime("%d.%m.%Y %H:%M:%S").rjust(35))
print("="*35)
print()
r=float(input("Vuvedete predostavenata suma pari: "))
ost=resto(r,sum)
if ost!=0:
    if ost>0:
        s="%.2f"% (ost)
        print(f"Resto: {s} lv.")
    else:
        print("Sumata ne e dostatuchna!")
        s="%.2f"% math.fabs(ost)
        print(f"Ne dostigat {s} lv.")
else:
    print("Tochna suma. Nqma resto!")
