# Tamsin Rogers
# September 10, 2019
# CS 152
# Lab 1
# Project 1 Creating Data
# Part 4: Generate & plot other trajectories with different initial conditions or acceleration on different planets
# This program generates the position of a thrown object being acted on by gravity on Venus
# Run the program from the Terminal by entering "python3 venus.py"

def venus(pi, vi, a, t):
	"""The venus function follows a physics equation which computes the position (pf) of
	 an object given its initial position (pi), initial velocity (vi), the acceleration acting
	 on the object (a), and the time duration over which the object is thrown (t) on Venus.  
	 This function takes the parameters pi, vi, a, and t, and returns the value for the 
	 object's trajectory on Venus (the pf value when given pi, vi, a, and t values as its 
	 parameters)."""
	vi = (0.926*vi)	#velocity on Venus is 0.926x velocity on Earth
	a = (0.907*a)	#acceleration on Venus is 0.907x acceleration on Earth
	pf = (pi + (vi*t) + (.5*a*(t**2))) 
	return(pf) #saves the value of the above equation

testVenus = venus(2, 11, -10, 0.5) #calculates pf for pi=2, vi=2, a=-10, t=0.5 and sets resulting value to the variable testVenus

def computeAndOutput (pi, vi, a, t):
	"""The computeAndOutput function computes the pf (position) value using the venus
	function explained above.  This function takes the parameters pi, vi, a, and t, and 
	and plots the resulting trajectories by writing the t and pf data value points directly to 
	the venus.csv file."""
	y = venus(pi, vi, a, t) #sets the return value of mercury with the parameters (pi, vi, a, t) to the variable y
	pf = (pi + (vi*t) + (.5*a*(t**2))) #the physical equation for trajectory
	fp = open( 'venus.csv', 'a' ) #opens a file named "venus.csv" and prepares to add lines of data to the file
	fp.write( str(t) + "," + str(pf) + "\n" ) #writes the given string to the end of the file
	fp.close() #closes the file
	print(t, ',', y) #prints the resulting t and y values, separated by a comma

def trajectory10(pi, vi, a, t): 
	"""The trajectory10 function computes ten points on a trajectory using the parameters pi,
	vi, a, and t.  The t values increase consecutively by (N*0.1) for each call of the 
	computeAndOutput function, of which there are ten instances."""
	computeAndOutput(pi, vi, a, (t+(0*0.1)))
	computeAndOutput(pi, vi, a, (t+(1*0.1)))
	computeAndOutput(pi, vi, a, (t+(2*0.1)))
	computeAndOutput(pi, vi, a, (t+(3*0.1)))
	computeAndOutput(pi, vi, a, (t+(4*0.1)))
	computeAndOutput(pi, vi, a, (t+(5*0.1)))
	computeAndOutput(pi, vi, a, (t+(6*0.1)))
	computeAndOutput(pi, vi, a, (t+(7*0.1)))
	computeAndOutput(pi, vi, a, (t+(8*0.1)))
	computeAndOutput(pi, vi, a, (t+(9*0.1)))

trajectory10(1, 11, -10, 0)
trajectory10(1, 11, -10, 1)
#the above lines print out two columns of numbers (t, y)

def trajectory100(pi, vi, a, t):
	"""The trajectory100 function computes one hundred points on a trajectory using the parameters pi,
	vi, a, and t.  The t values increase consecutively by 1 for each call of the 
	computeAndOutput function, of which there are ten instances."""
	trajectory10(pi, vi, a, (t+0))
	trajectory10(pi, vi, a, (t+1))
	trajectory10(pi, vi, a, (t+2))
	trajectory10(pi, vi, a, (t+3))
	trajectory10(pi, vi, a, (t+4))
	trajectory10(pi, vi, a, (t+5))
	trajectory10(pi, vi, a, (t+6))
	trajectory10(pi, vi, a, (t+7))
	trajectory10(pi, vi, a, (t+8))
	trajectory10(pi, vi, a, (t+9))

trajectory100(1, 50, -10, 0)
#the above lines continue to print out two columns of numbers (t, y)

def clearfile():
	"""The clearfile function clears the existing file before calling trajectory100(),
	which prevents the program from adding more data to the same file."""
	fp = open( 'venus.csv', 'w' ) #writes the file by creating it from scratch and deleting any pre existing content
	fp.close() #closes the file

clearfile() #clears the existing file before calling trajectory100()