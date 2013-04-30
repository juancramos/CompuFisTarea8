import string
import numpy
import scipy
from pylab import *
from scipy.optimize import curve_fit
from scipy.linalg import *

for i in range(10):
    
    #prepara los archivos uno a uno para ser leidos
    dibujar = numpy.loadtxt(str(i)+'Data.dat')
    x = dibujar[:,0]
    y = dibujar[:,1]
    
    #grafica x vs y
    plot(x, y)
    xlabel('x')
    ylabel('function')
    title(str(i)+'Plano_x,f_2')
    savefig(str(i)+'Plano_x,f_2.pdf')
    close()
    