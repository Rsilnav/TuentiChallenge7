cases = input()
for i in range(cases):
	num = input()
	count = 0
	x = map(int, raw_input().split())
	count += sum(x)
	print "Case #" + str(i+1) + ": " + str((count + 7)/8)