'''
The simplest numerical method for solving nonlinear equations of the form f(x)=0
'''

from math import *
from time import time
import sys

def toFixed(numObj):
	# fixed number of digits
	digits=5
	return f"{numObj:.{digits}f}"

def f(x):
	# introduction of function
	r=eval(function)
	return r	

def bisection(a,b,err):
	# implementation of method
	c=(a+b)/2.0
	while abs(b-a)>err:
		if f(a)*f(c)<0:
			b=c
		else:
			a=c
		c=(a+b)/2.0
	print('')	
	print('The root = ',toFixed(c))
	print('The function equals with the root = ',toFixed(f(c)))
	
def searching(a,b):
	# searching of root interval
	a1=a
	b1=b
	while a1<b1:
		if f(a1)*f(a1+step)>0:
			a1+=step
		else:
			print('')
			print('The root between points ',toFixed(a1),' and ',toFixed(a1+step))
			bisection(a1,a1+step,err)
			a1+=step

function=input('Input the function: ')
a=eval(input('Input the lower limit: '))
b=eval(input('Input the high limit: '))
err=eval(input('Input the accuracy: '))
step=eval(input('Input the step of search: '))
tic=time()
searching(a,b)
toc=time()
print('')
print(toFixed(toc-tic),' seconds to do the program')
input('Press ENTER to exit...')
