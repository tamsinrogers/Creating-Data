# Tamsin Rogers
# September 10, 2019
# CS 152
# Lab 1
# Project 1 Creating Data
# Part 3: Generating Data with Functions
# This program generates the position of a thrown object being acted on by gravity on Earth
# Run the program from the Terminal by entering "python3 gendata.py"

def ballistic1(t):
	"""The ballistic1 function follows a physics equation which computes the position (pf) of
	an object given its initial position (pi), initial velocity (vi), the acceleration acting
	on the object (a) on Earth.  This function takes the parameter t (time duration over which
	the object is thrown) and returns the value for the object's trajectory on Earth.  The
	ballistic1 function returns 5.25 when given the t value 0.5 as its parameter, and returns
	7.0 when given the t value 1.0 as its parameter."""
	pi = 1 # part d - assign the values
	vi = 11
	a = -10
	pf = (pi + (vi*t) + (.5*a*(t**2))) # part c - equation
	return(pf) # part g - saves the value of the above equation
		

#print (ballistic1(0.5)) # part f - test (prints 5.25)
#print (ballistic1(1.0)) # part f - test (prints 7.0)

y = ballistic1(0.5)
#print("f(0.5) is", y)
y = ballistic1(1.0)
#print("f(1.0) is", y)

def ballistic2(pi, vi, a, t): #part h
	"""The ballistic2 function follows a physics equation which computes the position (pf) of
	 an object given its initial position (pi), initial velocity (vi), the acceleration acting
	 on the object (a), and the time duration over which the object is thrown (t) on Earth.  
	 This function takes the parameters pi, vi, a, and t, and returns the value for the 
	 object's trajectory on Earth (the pf value when given pi, vi, a, and t values as its parameters)."""
	pf = (pi + (vi*t) + (.5*a*(t**2))) 
	return(pf) #saves the value of the above equation

testb2 = ballistic2(2, 11, -10, 0.5) #calculates pf for pi=2, vi=2, a=-10, t=0.5 and sets resulting value to the variable testb2
#print(testb2)

def computeAndOutput (pi, vi, a, t): #part i
	"""The computeAndOutput function computes the pf (position) value using the ballistic2
	function explained above.  This function takes the parameters pi, vi, a, and t, and 
	 plots the resulting trajectories by writing the t and y data value points directly to 
	the mydata.csv file."""
	y = ballistic2(pi, vi, a, t) #sets the return value of ballistic2 with the parameters (pi, vi, a, t) to the variable y
	pf = (pi + (vi*t) + (.5*a*(t**2))) #the physical equation for trajectory
	fp = open( 'mydata.csv', 'a' ) #part m - opens a file named "mydata.csv" and prepares to add lines of data to the file
	fp.write( str(t) + "," + str(pf) + "\n" ) #writes the given string to the end of the file
	fp.close() #closes the file
	print(t, ',', y) #prints the resulting t and y values, separated by a comma

def trajectory10(pi, vi, a, t): #partj
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
#part j: the above lines print out two columns of numbers that start with 0, 1.0 and end with 1.9, 3.85 (t, y)

def trajectory100(pi, vi, a, t):
	"""The trajectory100 function computes one hundred points on a trajectory using the parameters pi,
	vi, a, and t.  The t values increase consecutively by 1 for each call of the 
	computeAndOutput function, of which there are ten instances."""
	#developing loops:
	#tCount = 0
	#while tCount < 10:
		#trajectory10(pi, vi, a, (t+1))
		#tCount += 1
	
		#trajectory100(pi, vi, a, t) #partk

		#t100Count = 0
		#while t100Count < 10:
		#	trajectory10(pi, vi, a, (t+1))
			#t100Count += 1
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
#part k: the above lines continue to print out two columns of numbers, the final line is 9.9, 5.95


def clearfile():
	"""The clearfile function clears the existing file before calling trajectory100(),
	which prevents the program from adding more data to the same file."""
	fp = open( 'mydata.csv', 'w' ) #writes the file by creating it from scratch and deleting any pre existing content
	fp.close() #closes the file

clearfile() #clears the existing file before calling trajectory100()