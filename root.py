'''
Functions for root-finding.  Each of these functions takes in an argument
x and returns f(x).
'''
import numpy as np

def f1(x):
    # should be an easy one to determine roots
    # roots are (exactly):  +2.5, -8.7, -1.2
    return (x-2.5)*(x+8.7)*(x+1.2)

def f2(x):
    # somewhat harder to determine the root
    # root is (approximately): -3.0943512729560467
    return (0.2*np.sin(2.0*x)+0.6) + 0.2*x

def f3(x):
    # good luck! this will kill many root-finders.  MWUHAHAHA.
    # roots are (approximately): 3.1240484736455802, 3.6352284118019034
    return (np.sin(2.0*(x-4))+0.6) + 0.5*(x-4)**2

def f3(x):
	return x^5-x^3
def f4(x):
	return x**2*np.sin(x)

def f5(x):
	return (4*x**5+0.5*x**4+x**3-3*x**2+x-1)

def n_point_formula_derivative(function,evaluation_point, number_of_lattice_points, n_point_flag):
	interval_width = 0.5/10**number_of_lattice_points
	five_point_function_value_list = []
	for i in range(-2,3):
		five_point_function_value_list.append(function(evaluation_point + i*interval_width))
	if n_point_flag == 2:
		return ((five_point_function_value_list[3] - five_point_function_value_list[2])/(interval_width))
	if n_point_flag == 3:
		return ((five_point_function_value_list[3] - five_point_function_value_list[1])/(2*interval_width))
	if n_point_flag == 5:
		return ((five_point_function_value_list[0] - 8*five_point_function_value_list[1]
			+ 8*five_point_function_value_list[3] - five_point_function_value_list[4])/(12*interval_width))


def newtons_method(guess, function):
	print("guess: ",guess)
	print("function: ",function(guess))
	print("derivative: ",n_point_formula_derivative(function,guess,3,5))
	return guess - function(guess)/n_point_formula_derivative(function,guess,3,5)

guess = 8
max_iterations = 100
for i in range(0,max_iterations):
	print("iteration: ",i)
	guess = newtons_method(guess,f5)

from math import fabs
tolerance = 0.0001
def bisection(function,low_guess,high_guess,tolerance):
	midpoint = (low_guess + high_guess)/2.0
	print("low guess: ",low_guess)
	print("high guess: ",high_guess)
	print("midpoint: ",midpoint)
	print("function: ",function(midpoint))
	if fabs(function(midpoint)) < tolerance:
		return midpoint
	else:
		if function(low_guess)*function(midpoint) > 0:
			bisection(function,midpoint,high_guess,tolerance)
		else:
			bisection(function,low_guess,midpoint,tolerance)

from scipy import optimize

"""

print(optimize.brentq(f4,2,4))
bisection(f4,2,4,tolerance)

bisection(f1,2.0,3.0,tolerance)
bisection(f1,-1.0,10.0,tolerance)
bisection(f1,-2.1,-1.1,tolerance)
bisection(f1,-5,2,tolerance)
bisection(f1,-9.0,-8.0,tolerance)
bisection(f1,-20,-2,tolerance)

bisection(f2,-4,-3,tolerance)
bisection(f2,-10,0,tolerance)


bisection(f3,3.4,10.0,tolerance)
bisection(f3,-10.0,3.5,tolerance)
"""
