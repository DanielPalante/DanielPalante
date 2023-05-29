import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data_0 =np.array([20,24,26,27,28,28,29,29,30,30,30,30])/100
y_data_0 =np.array([5,20,36,57,79,96,120,135,147,169,178,194])/100000

x_data = x_data_0
y_data = np.log(y_data_0)

x_error = x_data*0.005+0.01

y_error_0 = y_data_0*0.01+0.02/1000

y_error = (1/y_data_0)*(y_error_0)

def f(x, a, b):
    return a*x+b


params, params_covariance = curve_fit(f, x_data, y_data)


plt.errorbar(x_data, y_data,xerr=x_error, yerr=y_error, fmt='o', markeredgecolor='black', label='Datos con errores', markersize = 0.5)
plt.scatter(x_data, y_data, s = 3, label='Datos', c = "black")
plt.plot(x_data, f(x_data, params[0], params[1]), label='Curva ajustada', color='red', lw = 0.5)
plt.legend(loc='best')

eta =  1.6/(params[0]*1.38*298)*10**4

eta_text = r'$\eta = {:.2f}$'.format(eta)
plt.text(0.24 ,-6.7, eta_text, fontsize=10)
equation_text = r'$ln(I) = {:.2f}V + {:.2f}$'.format(params[0], params[1])
plt.text(0.24, -6.2, equation_text, fontsize=10)

plt.xlabel('Voltaje (V)')
plt.ylabel('ln(I)')
plt.show()
