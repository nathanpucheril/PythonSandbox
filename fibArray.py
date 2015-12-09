##############################
# Returns Array of Fibonacci #
###### Numbers Up to n #######


def fibArr(n):
	def helperFib(n):
		if n == 1:
			return 1
		elif n == 2:
			return 1
		else:
			return helperFib(n-1) + helperFib(n-2)
	if n==0:
		return [0]
	return fibArr(n-1) + [helperFib(n)]
