import math
cases = input()

for c in range(cases):
	x = input()
	print "Case #" + str(c+1) + ": " + str(int(math.log(x, 2)) + 1)