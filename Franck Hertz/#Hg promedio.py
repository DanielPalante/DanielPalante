#Hg promedio
import numpy as np
energia_hg = [4.945318612776634,4.902282138339193,4.83471776749278,4.802026193383761,4.815970966472533,4.846943346386359,4.894534165182933,5.034425194586665,4.933132247368222,4.881152709329021]
error_hg =[0.1031090015930094,0.10673557641404255,0.11025531117905917,0.07523287030159416,0.13409110560593443,0.036851726133972404,0.12420257370903888,0.04950563029569164,0.11005428719145798,0.1086356241380734]
promedio_1 = 0
promedio_2 = 0
for i in range(10):
    promedio_1 = energia_hg[i]/error_hg[i]**2 + promedio_1

for i in range(10):
    promedio_2 = 1/error_hg[i]**2 + promedio_2
    
promedio_energia_hg = promedio_1 / promedio_2
print("Energía promedio de excitación total: ", promedio_energia_hg ,"+/-", 1/np.sqrt(promedio_2) )