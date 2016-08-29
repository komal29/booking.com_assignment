def find_sum(number_map):
	for key in number_map:
		if number_map.get(key) in number_map.keys():
			return 1
	return 0

if __name__ == '__main__':
	N = int(input())
	M = int(input())
	number_map = {}
	for i in range(M):
		temp = int(input())
		number_map.update({ temp : abs(N-temp)})
	print(find_sum(number_map))
	

