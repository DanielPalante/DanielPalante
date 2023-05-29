import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data_0 =np.array([1348,1388,1424,1441,1485,1560,1592,1636,1667,1686,1718,1734,1753,1765,1780,1790,1801,1817])/10
y_data_0 =np.array([8,9,10,11,12,16,19,22,25,28,32,35,38,40,43,46,48,52])/10000000
#y_error = y_data*0.008+3*0.1
x_data = 1/(x_data_0+273.2)
y_data = np.log(y_data_0)

x_error_0 = (x_data_0)*0.03+0.1

x_error = (1/(x_data_0+273.2)**2)*(x_error_0)

y_error_0 = y_data_0*0.01+0.02/1000000

y_error = (1/y_data_0)*(y_error_0)

def f(x, a, b):
    return a*x+b


params, params_covariance = curve_fit(f, x_data, y_data)



plt.errorbar(x_data, y_data,xerr=x_error, yerr=y_error, fmt='o', markeredgecolor='black', label='Datos con errores', markersize = 0.5)
plt.scatter(x_data, y_data, s = 3, label='Datos', c = "black")
plt.plot(x_data, f(x_data, params[0], params[1]), label='Curva ajustada', color='red', lw = 0.5)
plt.legend(loc='best')
gap =  -params[0]*1.71*1.38*6.24*10**(-5)

gap_text = r'$E_g= {:.2f}$'.format(gap)
plt.text(0.00221 ,-13.7, gap_text, fontsize=10)
equation_text = r'$ln(I_0) = {:.2f}(1/T) + {:.2f}$'.format(params[0], params[1])
plt.text(0.00221 , -13.5, equation_text, fontsize=10)

plt.xticks(fontsize=8)
plt.xlabel('1/T K^(-1)')
plt.ylabel('ln(I_0)')
plt.show()
