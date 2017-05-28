# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:49:59 2017

@author: shiyanlou
"""
from numpy import *

b=array([n for n in range(5)])
print b

a=array([[n+m*10 for n in range(5)] for m in range(5)])
#print a
#
diag(a,-2)

v2=arange(-3,3)
#v2
row_indices=[1,3,5]
print v2[row_indices]
print v2.take(row_indices)
#take 可以用在list 和其他对象上面
print take([-3,-2,-1,-0,1,2],row_indices)

#2 线性代数
v1=arange(0,5)
print v1*2
print v1+2
a1=a*2 ;a2=a+2
#Element-wise(逐项乘) 数组－数组 运算
print a1*a2
#矩阵乘法 dot
one=ones((2,2))
#print one.astype('int64') 强制类型转换
num=array([[1,2],[3,4]])

print dot(num,one)

m=matrix(a)
v=m.T
print m*m

print mean(m[:,3])

print std(m[:,3]),var(m[:,3])
print m[:,3].min(),m[:,3].max(),m.max()

d=arange(0,5)
print sum(d),prod(d+1),cumsum(d),cumprod(d+1)

print trace(a)