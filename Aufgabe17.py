# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import maabara as ma
import numpy as np
import scipy as sp
import sympy as sym
import matplotlib as mpl 
import matplotlib.pyplot as plt
import math
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
mpl.rcParams['text.usetex']=True
mpl.rcParams['text.latex.unicode']=True
mpl.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

plt.clf()
plt.figure()
ax=plt.subplot(111)
x=np.linspace(0,0.1,1000)
a=(1.5**2-(2*1.5+1)*1+(1.5+2)/1.5)/(32.*(1.5-1.)**2)
ax.plot(x,((x**4*np.pi*a)/(4.*800e-9))**(1/3.))

ax.set_title('Brennweite in Abhängigkeit des Strahldurchmessers')
ax.legend(numpoints=1, markerscale=1.5, fontsize=10,ncol=3,fancybox=True, shadow=True, loc=0)
ax.set_ylabel('Brennweite $f$ [m]')
ax.set_xlabel('Strahldurchmesser $D$ [m]')
ax.grid(True)

plt.savefig("plot1.pdf",transparent=True,format="pdf",bbox_inches='tight')

plt.clf()
plt.figure()
plt.ticklabel_format(style='sci', scilimits=(0,0))
ax2=plt.subplot(111)
x=np.linspace(0,2,1000)
b=((4*(800e-9)**3*0.1)/(np.pi)**3)**(1/4.)
n=1.5
ax2.plot(x,b*((n**2-(2*n+1)*x+(n+2)/n*x**2)/(32.*(n-1.)**2))**(1/4.),'b-',label='$n=1,5$')
n=1.7
ax2.plot(x,b*((n**2-(2*n+1)*x+(n+2)/n*x**2)/(32.*(n-1.)**2))**(1/4.),'g-',label='$n=1,7$')
n=1.9
ax2.plot(x,b*((n**2-(2*n+1)*x+(n+2)/n*x**2)/(32.*(n-1.)**2))**(1/4.),'r-',label='$n=1,9$')

ax2.set_xlabel('Formfaktor $K$')
ax2.set_ylabel('minimaler Radius $w_0\'$ [m]')
ax2.grid(True)
ax2.legend(loc=2)
ax2.set_xticks(np.arange(0, 2, 0.1))
plt.savefig("plot2.pdf",transparent=True,format="pdf",bbox_inches='tight')

# <codecell>


