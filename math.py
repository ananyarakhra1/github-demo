#add implementation
def add(x,y): 
	return x+y 
#subtract implementation
def subtract(x,y): 
	return x-y 		#on master branch 
#multiply implementation
def multiply(x,y): 
	return x*y		#on Bug 456 branch 
#divide implementation
def divide(x,y): 
	if x<0:
		return NEGATIVE_PARAM_ERROR	#on master branch
	if y==0:
		return DIVIDE_BY_0_ERROR	#on Bug789 branch
	else:
		return x/y