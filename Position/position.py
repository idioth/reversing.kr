answer = "76876-77776"

for a in range(ord('a'), ord('z') + 1):
	for b in range(ord('a'), ord('z') + 1):
		for c in range(ord('a'), ord('z') + 1):
			name = [a, b, c, ord('p')]
			result = ""

			serial = ""
			serial += str(((name[0] & 1) + 5) + (((name[1] >> 2) & 1) + 1))
			serial += str((((name[0] >> 3) & 1) + 5) + (((name[1] >> 3) & 1) + 1))
			serial += str((((name[0] >> 1) & 1) + 5) + (((name[1] >> 4) & 1) + 1))
			serial += str((((name[0] >> 2) & 1) + 5) + ((name[1] & 1) + 1))
			serial += str((((name[0] >> 4) & 1) + 5) + (((name[1] >> 1) & 1) + 1))
			serial += "-"
			serial += str(((name[2] & 1) + 5) + (((name[3] >> 2) & 1) + 1))
			serial += str((((name[2] >> 3) & 1) + 5) + (((name[3] >> 3) & 1) + 1))
			serial += str((((name[2] >> 1) & 1) + 5) + (((name[3] >> 4) & 1) + 1))
			serial += str((((name[2] >> 2) & 1) + 5) + ((name[3] & 1) + 1))
			serial += str((((name[2] >> 4) & 1) + 5) + (((name[3] >> 1) & 1) + 1))

			if serial == answer:
				for i in range(0, 4):
					result += chr(name[i])
				print result