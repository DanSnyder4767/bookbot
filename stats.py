def get_num_words(text):
	words = text.split()
	return len(words)

def get_num_char(text):
	lower_text = text.lower()
	char_count = {}
	for n in lower_text:
		if n in char_count:
			char_count[n] += 1
		else:
			char_count[n] = 1
	return char_count

def sort_on(items):
	return items["num"]

def sort_dict(dict):
	dict_list = []
	for n in dict:
		new_dict = {"char": "", "num": 0}
		new_dict["char"] = n
		new_dict["num"] = dict[n]
		dict_list.append(new_dict)
	dict_list.sort(reverse=True, key=sort_on)
	return dict_list
