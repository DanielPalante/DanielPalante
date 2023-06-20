
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

# Importar los datos desde el archivo Excel
data = pd.read_excel(r'C:\Users\julik\Desktop\Datos franck hertz\Neon\Neon 4.xlsx', sheet_name='Neon 4')

# Obtener las columnas que deseas graficar
x = data['voltaje']
y = data['corriente']
x_min =[0,0,0]
x_max =[0,0,0]
promedio_x = [0,0,0]
error_x = [0,0,0]
# Crear la gráfica
plt.plot(x, y)
plt.title('Voltaje vs corriente')
plt.xlabel('Voltaje de aceleración (V)')
plt.ylabel('Intensidad de corriente (nA)')



x_min[0] = 30.9 # Valor mínimo de X
x_max[0] = 32.9# Valor máximo de X

x_min[1] = 48.0 # Valor mínimo de X
x_max[1] = 49.6# Valor máximo de X

x_min[2] = 66.3 # Valor mínimo de X
x_max[2] = 68.3# Valor máximo de X

for i in range(len(x_min)):
    # Definir el rango de valores de X
    

    # Filtrar los datos en el rango de X
    filtered_x = x[(x >= x_min[i]) & (x <= x_max[i])]
    filtered_y = y[(x >= x_min[i]) & (x <= x_max[i])]

   

    # Encontrar los máximos locales en el rango filtrado de X

    filtered_x = filtered_x.reset_index(drop=True)
    filtered_y = filtered_y.reset_index(drop=True)

    # Mostrar los máximos locales en la gráfica
    plt.plot(filtered_x, filtered_y, color='red', label='Máximos locales')
    x_values = filtered_x.values
    
    std_deviation = np.std(x_values)
    error_x[i] = std_deviation/np.sqrt(len(x_values))
    promedio_x[i]= np.mean(filtered_x)
   

promedio_1 = 0
promedio_2 = 0

for j in range(len(x_min)-1):

    print("La energía de excitación",j+1,"es",promedio_x[j+1]-promedio_x[j], "+/-" ,(error_x[j]+error_x[j+1]))
    promedio_1 =  (promedio_x[j+1]-promedio_x[j])/(error_x[j]+error_x[j+1])**2 + promedio_1
    



for j in range(len(x_min)-1):
    
    promedio_2 =  1/(error_x[j]+error_x[j+1])**2 + promedio_2

energia_promedio = promedio_1/promedio_2
error_promedio = 1/np.sqrt(promedio_2)
######################## 
print("La energía de excitación promedio es:", energia_promedio, "+/-", error_promedio)
plt.legend()
plt.xticks(np.arange(0, 100+1, 5))



#plt.show()
