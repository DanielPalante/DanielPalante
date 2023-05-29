import statistics

def calcular_desviacion_estandar(datos):
    try:
        promedio = statistics.mean(datos)
        desviacion = statistics.stdev(datos)
        return promedio, desviacion
    except statistics.StatisticsError as e:
        print("Ha ocurrido un error al calcular la desviación estándar:", str(e))
        return None, None

# Ejemplo de uso

conjunto_datos = [0.79, 0.81, 0.81, 0.85, 0.92]
promedio, desviacion_estandar = calcular_desviacion_estandar(conjunto_datos)
print("El promedio es:", promedio)
print("La desviación estándar es:", desviacion_estandar)
print("El valor del gap es:", promedio," + -", desviacion_estandar)



