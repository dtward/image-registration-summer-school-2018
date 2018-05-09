# This file contains several convenience functions for working with data in the summer school
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_landmarks(fname):
    '''Load landmarks from text file, we assume that the first line has size info'''
    with open(fname) as f:
        for i,line in enumerate(f):
            if i == 0:
                # the first line says the size of the file
                d,n = [int(n) for n in line.split()]
                X = np.empty((d,n))
                continue
            X[:,i-1] = [float(n) for n in line.split()]
    return X

def load_surface(fname):
    '''Load byu surface from text file
    vertices are output as a 3xN numy array
    faces are output as a Mx3 numpy integer array
    they are transposed to be compatible with trisurf'''
    with open(fname) as f:
        for i,line in enumerate(f):
            if i == 0:
                # the first gives info about file
                _,nv,nf,_ = [int(n) for n in line.split()]
                vertices = np.empty((3,nv),dtype=float)
                faces = np.empty((nf,3),dtype=int)
                continue
            elif i == 1:
                continue
            if i <= nv+1:
                vertices[:,i-2] = [float(n) for n in line.split()]
            else:
                faces[i-(nv+2),:] = [np.abs(int(n))-1 for n in line.split()]
    return vertices, faces

def axis_equal(ax=None):
    '''Set x,y,z axes to constant aspect ratio
    ax is a matplotlib 3d axex object'''
    if ax is None: ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()
    cx = np.mean(xlim)
    cy = np.mean(ylim)
    cz = np.mean(zlim)
    rx = np.diff(xlim)
    ry = np.diff(ylim)
    rz = np.diff(zlim)
    r = np.max([rx,ry,rz])
    ax.set_xlim(cx + np.array([-1,1])*0.5*r)
    ax.set_ylim(cy + np.array([-1,1])*0.5*r)
    ax.set_zlim(cz + np.array([-1,1])*0.5*r)
    
def plot_grid(X0, X1, rstride=1, cstride=1, ax=None, **kwargs):
    ''' 
    plot a grid defined by X0 and X1, 
    which are 2d arrays that should be the same size
    for example as output from meshgrid
    
    rstride defines how many rows to skip
    cstride defines how many columns to skip
    '''
    if ax is None: ax = plt.gca()
    # some defaults
    defaultargs = {
        'color':'k'
    }
    kwargs.update(defaultargs)
    # plot rows
    for i in range(0, X0.shape[0], rstride):
        ax.plot(X0[i,:], X1[i,:], **kwargs)
    if i < X0.shape[0]-1: ax.plot(X0[-1,:], X1[-1,:], **kwargs)
    # plot columns
    for j in range(0,X0.shape[1],cstride):
        ax.plot(X0[:,j], X1[:,j], **kwargs)
    if i < X0.shape[1]-1: ax.plot(X0[-1,:], X1[-1,:], **kwargs)