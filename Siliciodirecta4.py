import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data_0 =np.array([0.50, 0.53, 0.56, 0.57, 0.59, 0.60, 0.61, 0.61, 0.62, 0.62, 0.63, 0.64, 0.64, 0.65, 0.65,0.65,0.66,0.66])
y_data_0 =np.array([0.08, 0.17, 0.31, 0.43, 0.58, 0.75, 0.88, 1.00, 1.18, 1.33, 1.56, 1.72, 1.92, 2.17, 2.33,2.56,2.85,3.07])/1000

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
plt.text(0.56, -6.5, eta_text, fontsize=10)
equation_text = r'$ln(I) = {:.2f}V + {:.2f}$'.format(params[0], params[1])
plt.text(0.56, -6, equation_text, fontsize=10)

plt.xlabel('Voltaje (V)')
plt.ylabel('ln(I)')
plt.show()


#print(f(x_data,params[0]))