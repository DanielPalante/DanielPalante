import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x_data_0 =np.array([49,53,56,57,59,60,61,62,63,65,66,68,69,70])/100
y_data_0 =np.array([5,16,30,45,64,88,110,137,173,226,302,399,498,672])/100000


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