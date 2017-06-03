# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:24:23 2017

@author: fangxu
"""
#设置图片一颜色，线宽 线型
import matplotlib.pyplot as plt

from matplotlib import rcParams
from numpy import *

rcParams.update({'font.size':12,'font.family':'sans','text.usetex':False})
x=linspace(0,5,10)

fig,ax=plt.subplots()

ax.plot(x,x**2,'b.-')
ax.plot(x,x**3,'g--')

#fig

fig1,ax1=plt.subplots(figsize=(12,6))

ax1.plot(x,x+1,color="blue",linewidth=0.25)
ax1.plot(x,x+3,color="blue",linewidth=1)

ax1.plot(x,x+5,color="red",lw=1,ls='-')
ax1.plot(x,x+7,color="red",lw=2,ls='-.')
 
line,=ax1.plot(x,x+8,color="black",lw=1.50)
line.set_dashes([5,10,15,10])

ax1.plot(x,x+9,color="green",lw=2,ls='*',marker='+')
ax1.plot(x,x+10,color="green",lw=2,ls='*',marker='o')

ax1.plot(x,x+10,color="green",lw=2,ls='*',marker='o',markersize=4)

ax1.plot(x,x+12,color="purple",lw=2,ls='-',marker='s',markersize=6,markerfacecolor="yellow",markeredgewidth=2,markeredgecolor="blue")

#fig1

#控制坐标轴样式
fig3,axes3=plt.subplots(1,3,figsize=(12,4))

axes3[0].plot(x,x**2,x,x**3)
axes3[0].set_title("default axes ranges")

axes3[1].plot(x,x**2,x,x**3)
axes3[1].axis('tight')

axes3[1].set_title("tight axes")

axes3[2].plot(x,x**2,x,x**3)
axes3[2].set_ylim([0,60])
axes3[2].set_xlim([2,5])

axes3[2].set_title("custom axes range")

fig3

fig4,axes4=plt.subplots(1,2,figsize=(10,4))
axes4[0].plot(x,x**2,x,exp(x))
axes4[0].set_title("normal scale")

axes4[1].plot(x,x**2,x,exp(x))
axes4[1].set_yscale("log")
axes4[1].set_title("Logarithmic scale (y)")

fig4











