'''AIM:Write a python function sin(x,n) to calculate the value of sin(x) using its Taylor series expansion up to n terms .
Compare the values of sin(x) for different values of n with the correct value.'''
# Python3 code for implementing 
# sin function 
import math; 

# Function for calculating sin value 
def cal_sin(n): 

	accuracy = 0.0001; 
	
	# Converting degrees to radian 
	n = n * (3.142 / 180.0); 
	
	x1 = n; 
	
	# maps the sum along the series 
	sinx = n;	 
	
	# holds the actual value of sin(n) 
	sinval = math.sin(n); 
	i = 1; 
	while(True): 
	
		denominator = 2 * i * (2 * i + 1); 
		x1 = -x1 * n * n / denominator; 
		sinx = sinx + x1; 
		i = i + 1; 
		if(accuracy <= abs(sinval - sinx)): 
			break; 
		
	print(round(sinx)); 

# Driver Code 
n = 90; 
cal_sin(n); 
 
