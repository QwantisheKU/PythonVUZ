def f22(x):
	#0b00000000000000000000000000000000
	F = x & 0x80000000
	E = x & 0x7FF00000
	D = x & 0xF8000
	C = x & 0x6000
	B = x & 0x1C00
	A = x & 0x3FF
	
	F >>= 16
	E >>= 4
	D >>= 15
	C <<= 17
	B <<= 17
	A <<= 5
	
	x = A + B + C + D + E + F
	return x
#print(hex(f22(0xd287f152)))
#print(hex(f22(0x0491615f)))
	
 