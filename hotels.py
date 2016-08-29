from collections import Counter

if __name__ == '__main__':
	review_words = input().split()
	M = int(input())
	reviews = []
	hotel_ids = []
	for i in range(2*M):
		if i%2 == 0:
			hotel_id = int(input())
			hotel_ids.append(hotel_id)
		else:
			review = input().split()
			reviews.append(review)

	reviews_dict = dict()
	for i in range(len(hotel_ids)):
		current_hotel_id = hotel_ids[i]
		if current_hotel_id in reviews_dict:
			reviews_list = reviews_dict.get(current_hotel_id)
			reviews_list.extend(reviews[i])
		else:
			reviews_dict.update({ current_hotel_id : reviews[i]})

	count_map = dict()
	for key in reviews_dict:
		reviews_list_count = Counter(reviews_dict.get(key))
		sum = 0
		for item in review_words:
			if item in reviews_list_count:
				sum = sum + reviews_list_count.get(item)
		count_map.update({key : sum})

	count_map_sorted = sorted(count_map.items(), key=lambda x: x[1], reverse=True)

	result = [x[0] for x in count_map_sorted]
	print(' '.join(map(str, result)))

