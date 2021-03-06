#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np

def naivebayesPXY(x, y):
# =============================================================================
#    function [posprob,negprob] = naivebayesPXY(x,y);
#
#    Computation of P(X|Y)
#    Input:
#    x : n input vectors of d dimensions (dxn)
#    y : n labels (-1 or +1) (1xn)
#    
#    Output:
#    posprob: probability vector of p(x|y=1) (dx1)
#    negprob: probability vector of p(x|y=-1) (dx1)
# =============================================================================


    
    # Convertng input matrix x and y into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    Y = np.matrix(y)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
    # Pre-constructing a matrix of all-ones (dx2)
    X0 = np.ones((d,2))
    Y0 = np.matrix('-1, 1')
    
    # add one all-ones positive and negative example
    Xnew = np.hstack((X, X0)) #stack arrays in sequence horizontally (column-wise)
        #Xnew = np.concatenate((X, X0), axis=1) #concatenate to column
    Ynew = np.hstack((Y, Y0))
    
    # Re-configuring the size of matrix Xnew
    d,n = Xnew.shape
    
# =============================================================================
# fill in code here
    collectYequalOne = [Ynew==1]
    countYequalOne = np.sum(collectYequalOne)
    YequalOneRow = np.asarray(collectYequalOne).flatten()
    XwhenYequalOne = Xnew[:,YequalOneRow]
    posprob = np.sum(XwhenYequalOne, axis=1) / countYequalOne

    collectYequalNeg = [Ynew==-1]
    countYequalNeg = np.sum(collectYequalNeg)
    YequalNegRow = np.asarray(collectYequalNeg).flatten()
    XwhenYequalNeg = Xnew[:,YequalNegRow]
    negprob = np.sum(XwhenYequalNeg, axis=1) / countYequalNeg
    return posprob,negprob

# =============================================================================
