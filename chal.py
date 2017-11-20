s = []
def xorshift128plus():
	global s
	x, y = s
	x ^= (x << 23) & (2 ** 64 - 1)
	s[0] = y
	s[1] = x ^ y ^ (x >> 17) ^ (y >> 26)
	return y

def main():
	global s
	T = int(raw_input())
	for t in range(T):
		n, Cmax, Hmax = map(int, raw_input().split())
		C = [[0] * n for x in range(n)]
		for i in range(n):
			s = list(map(int, raw_input().split()))
			for j in range(i + 1, n):
				C[i][j] = C[j][i] = xorshift128plus() % (Cmax + 1)
		
		H = [[0] * n for x in range(n)]
		for i in range(n):
			s = list(map(int, raw_input().split()))
			for j in range(n):
				H[i][j] = xorshift128plus() % (Hmax + 1)
		print(H)
        print(C)


		# solve here

if __name__ == "__main__":
	main()