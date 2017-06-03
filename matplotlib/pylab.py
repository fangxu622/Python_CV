# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:59:34 2017

@author: shiyanlou
"""

from pylab import *

from numpy import *
x=linspace(0,5,10)
y=x **2

figure()

plot(x,y,'r')

xlabel('x')

ylabel('y')

title('title')

show()

subplot(1,2,1)

plot(x,y,'r--')

subplot(1,2,2)

plot(y,x,'g*-')









