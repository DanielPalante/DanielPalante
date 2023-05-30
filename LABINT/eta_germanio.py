import statistics
import numpy as np
def calcular_desviacion_estandar(datos):
    try:
        promedio = statistics.mean(datos)
        desviacion = statistics.stdev(datos)
        return promedio, desviacion
    except statistics.StatisticsError as e:
        print("Ha ocurrido un error al calcular la desviación estándar:", str(e))
        return None, None

# Ejemplo de uso

conjunto_datos = [1.10, 0.99, 1.08, 1.14, 1.26]
promedio, desviacion_estandar = calcular_desviacion_estandar(conjunto_datos)
print("El promedio es:", promedio)
print("La desviación estándar es:", desviacion_estandar)
error_std = desviacion_estandar/np.sqrt(5)
print("El valor de eta es:", promedio," + -", error_std)



