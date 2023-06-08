import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Definir la función trigonométrica para el ajuste
def trigonometric_func(x, a):
    return  a* np.cos(np.deg2rad(x))**2

# Datos
x_data_0 = np.array([-90,-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])
x_data = x_data_0
y_data = np.array([70,105,185,327,513,744,950,1287,1594,1980,2270,2586,2805,3180,3404,3427,3539,3780,3804,3737,3670,3534,3303,3053,2824,2503,2188,1875,1549,1249,942,692,470,289,157,91,77])/100

x_error = 0.5

y_error = y_data*0.005+0.1

# Realizar el ajuste
p0 = [0]  # Valores iniciales para los parámetros
params, cov = curve_fit(trigonometric_func, x_data, y_data, p0=p0)

errors = np.sqrt(np.diag(cov))

# Obtener los valores ajustados
y_fit = trigonometric_func(x_data, *params)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Plotear los datos originales y el ajuste
plt.errorbar(x_data, y_data,xerr=x_error, yerr=y_error, fmt='o', markeredgecolor='black', label='Datos con errores', markersize = 1)
ax.scatter(x_data, y_data, c='black', s=2, label='Datos')
ax.plot(x_data, y_fit, 'r-', label='Ajuste',lw=0.4)

# Ajustar los ejes para tener la misma escala

# Etiquetas de los ejes y leyenda
ax.set_xlabel(r'$\varphi$(°)')
ax.set_ylabel('Intensidad de luz (mA)')
ax.legend()
print(params[0])
print(errors)

eqn2 = r'$\sigma_a = {:.2f}$'.format(errors[0])

eqn1 = r'$y =   {:.2f} \cos^2(x)$'.format(params[0])
ax.text(0.2, 0.15, eqn1, transform=ax.transAxes, fontsize=8, verticalalignment='top')
ax.text(0.2, 0.10, eqn2, transform=ax.transAxes, fontsize=8, verticalalignment='top')
# Mostrar el gráfico
plt.show()