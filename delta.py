if __name__ == '__main__':
	data = list(map(int, input().split()))
	result_data = list()
	for i in range(len(data)):
		if i == 0:
			result_data.append(data[i])
		else:
			prev_item = data[i-1]
			current_item = data[i]
			diff = current_item-prev_item
			if diff >= -127 and diff <= 127:
				result_data.append(diff)
			else:
				result_data.append(-128)
				result_data.append(diff)
	print(" ".join(map(str, result_data)))