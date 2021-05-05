#!/usr/bin/env python
#MODIFICACION
from __future__ import print_function
from __future__ import division
import MDAnalysis
import numpy.linalg
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def select():
     
    u = MDAnalysis.Universe('umbrella.gro','umbrella.trr') 
    interface=u.select_atoms('resname SOL and prop z <= 120')
    interface.atoms.write('interface.gro')
#    print(interface[0].pos,interface[0].velocity )
    

select()

    
x,y,z=np.meshgrid(np.arange(0, 10, 0.5), np.arange(0, 10, 0.5), np.arange(0, 10, 0.5))

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d') # get current axis
ax.scatter(x,y,z,color='k')

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d') # get current axis
ax.scatter(x,y,z)
plt.show()
