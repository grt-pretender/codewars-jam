# Complete the square sum function so that 
# it squares each number passed into it and then sums the results together.


# ===================================
# 1) One solution
# ===================================


def square_sum(numbers):
    if len(numbers) == 0:
    	return 0
    return sum([pow(c, 2) for c in numbers])



# ===================================
# 2) With a new variable
# ===================================


def square_sum(numbers):
	res = 0
	for num in numbers:
   		res += num*num
	return res