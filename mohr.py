# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hqXe91QoXmw9cApufh1rzs-N7BzuWZak
"""

import numpy as np
import matplotlib.pyplot as plt

def mohr_circle(norm1,nrm2,shear):
    n1=norm1
    n2=norm2
    t=shear
    n_min=(n1-n2)/2
    n_max=(n1+n2)/2
   
    radius=np.sqrt((n1-n2)**2/4+t**2)
    centre_x=n_min
    centre_y=0
    z=np.linspace(0,360,360)
    w=np.linspace(0,50,50)  #according to scale
    x=(n1+n2)/2+radius*np.cos(np.radians(z))
    y=radius*np.sin(np.radians(z))
    p=([n1,n1,n2,n2,n2])
    b=([0,t,-t,0,0])
    ax=plt.axes()
    ax.plot(w,w*0)# this plots x axis

    plt.plot(p,b,x,y)
    plt.xlabel(r"$\sigma$")
    plt.ylabel(r"$\tau$")
    plt.axis('equal')
    plt.show()

norm1=eval(input('enter valuue of maximum stress:'))
norm2=eval(input('enter valuue of minimum stress:'))
shear=eval(input('enter valuue of shear stress:'))
mohr_circle(norm1,norm2,shear)
