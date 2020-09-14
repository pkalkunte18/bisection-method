# -*- coding: utf-8 -*-
"""
Bisection method - finds root within tolerance, given a, b and function.
Vee Kalkunte
September 12th, 2020
"""
import math

#-----------------------------Adjustable Inputs-------------------------------#

a = 1 #left interval
b = 2 #right interval
tol = .000001 #how precise you want it - default 10^-5
lim = 20 #how many iterations you want to try before it's no longer worth it

#edit this as needed for functions
def function(x): return (x**3 + 4*x**2 - 10)

#-----------------------------Bisection Method--------------------------------#

#will accept nonzero fx    
def bisection(function, a, b, fx = 0, tol = tol, lim = lim):
    #check first to see if a and b are the correct input - ie, IVT
    fa = function(a)
    fb = function(b)
    #one interval needs to be past the fx we seek, one before the fx we seek
    if(fa * fb > 0): return ("Error, fa and fb fail IVT, no fx at interval")
    
    #once we've passed that test - begin the series
    px = (a + b) / 2
    count = 0
    while(count < lim):
        #new iteration, new times
        fpx = function(px)
        #print format to fit with tabular
        print(count, " & ", a, " & ", b, " & ", px, " & ", fpx)
        
        #check if we've found the solution within tolerance
        if(abs(fpx - fx) < tol): return ("Answer within tolerance:", px)
        
        #reiterate bisextion to get a new potential solution
            #whichever is absolutely smaller is closer, we keep that one
            #also if it's smaller it's clearly beyond the halfway point - so,
            #the other bound becomes px
        fa = function(a)
        fb = function(b)
        if(fa * fpx > 0):
            #a and p are same sign
            a = px
            px = (a + b) / 2
        else:
            #b and p are same sign
            b = px
            px = (a + b) / 2
            
        #iteration += 1
        count += 1
        
    return ("Solution at max iteration:", px)

#-----------------------------Execute-----------------------------------------#
    
#given function
print(bisection(function, a, b))  