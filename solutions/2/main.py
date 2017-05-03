
cases = input()

for c in range(cases):
	tmp = []
	num = input()
	x = map(int, raw_input().split())

	tirada = 0
	puntos = 0
	primero = True
	for i in range(num):
		if len(tmp) == 10:
			break
		else:
			if primero:
				if x[i] == 10:
					if i+1 < len(x):
						puntos += x[i+1]
					if i+2 < len(x):
						puntos += x[i+2]
					puntos += 10
					tmp.append(puntos)
				else:
					tirada += x[i]
					primero = False
			else:
				tirada += x[i]
				if tirada == 10:
					if i+1 < len(x):
						puntos += x[i+1]

				puntos += tirada
				primero = True
				tirada = 0

				tmp.append(puntos)

	print "Case #" + str(c+1) + ": " + ' '.join(map(str, tmp))