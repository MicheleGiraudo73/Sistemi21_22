def spiral(size):
	m = [[0] * size for i in range(size)]
	dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
	x, y, c = 0, -1, 1
	for i in range(2*size - 1):
		for j in range((2*size - i) // 2):
			x += dx[i % 4]
			y += dy[i % 4]
			m[x][y] = c
			c += 1
	return m

def main():
    size = int(input("inserire: "))
    print(spiral(size))

if __name__=="__main__":
    main()