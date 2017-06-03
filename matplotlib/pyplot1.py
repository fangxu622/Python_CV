# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:07:18 2017

@author: shiyanlou
"""

import matplotlib.pyplot as plt
from numpy import *
x=linspace(0,5,10)

fig =plt.figure()

axes1 =fig.add_axes([0.1,0.1,0.8,0.8])  #main axes

axes2=fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y,'r')

axes1.set_xlabel('x')

axes1.set_ylabel('y')

axes1.set_title('title1')

#insert
axes2.plot(y,x,'r')

axes2.set_xlabel('y')

axes2.set_ylabel('x')

axes2.set_title('insert title')

fig



fig0,ax0=plt.subplots()
ax0.plot(x,x**2,label=r"$y= \alpha^2$")
ax0.plot(x,x**3,label=r"$y= \alpha^3$")
ax0.legend(loc=2)# upper left corner

ax0.set_xlabel(r'$\alpha$',fontsize=18)
ax0.set_ylabel(r'$y$',fontsize=18)

ax0.set_title('title')
fig



