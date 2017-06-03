# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from matplotlib import rcParams
from numpy import *

rcParams.update({'font.size':12,'font.family':'sans','text.usetex':False})
x=linspace(0,5,10)

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(x, x**2, x, x**3, lw=2)

ax.set_title("scientific notation")
#set_xticks 与 set_yticks 方法可以显示地设置标号的位置，

#set_xticklabels 与 set_yticklabels 为每一个标号设置符号：

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)


yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels
#使用科学计数法
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
ax.yaxis.set_major_formatter(formatter) 


fig