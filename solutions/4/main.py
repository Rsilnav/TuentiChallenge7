cases = input()

for ca in range(cases):

	sides = sorted(map(int, raw_input().split()[1:]))

	x = 0
	found = False
	for i in range(2, len(sides)):
		if sides[i] < sides[i-2] + sides[i-1]:
			x = i
			found = True
			break

	if not found:
		print "Case #" + str(ca+1) + ": IMPOSSIBLE"
		continue

	new = [s for s in sides if s <= sides[x] + sides[x-1]]
	maxim = sides[x]
	
	lado_a = maxim
	lado_a_i = x

	minim = -1

	for i in range(len(new)-1):

		if i == x:
			continue

		for j in range(i):

			if j == x:
				continue

			lado_b = new[i]
			lado_c = new[j]
			m = max([lado_a, lado_b, lado_c])
			s = sum([lado_a, lado_b, lado_c])

			if m < s - m:
				if minim == -1 or s < minim:
					minim = s

	print "Case #" + str(ca+1) + ": " + str(minim)