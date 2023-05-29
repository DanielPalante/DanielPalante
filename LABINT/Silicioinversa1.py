import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data_0 =np.array([110.0, 120.0, 130.0, 140.0, 150.0, 153.9, 158.2, 160.0, 162.9, 164.3, 167.0, 168.2, 170.0, 172.8, 180])
y_data_0 =np.array([0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.9, 3.9])/1000000

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
plt.text(0.00222 ,-15.3, gap_text, fontsize=10)
equation_text = r'$ln(I_0) = {:.2f}(1/T) + {:.2f}$'.format(params[0], params[1])
plt.text(0.00222 , -15, equation_text, fontsize=10)

plt.xticks(fontsize=8)
plt.xlabel('1/T K^(-1)')
plt.ylabel('ln(I_0)')
plt.show()
