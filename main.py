import sys
from stats import sort_dict
from stats import get_num_char
from stats import get_num_words

def main():
	if len(sys.argv) != 2:
		raise sys.exit("Usage: python3 main.py <path_to_book>")

	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars_dict = get_num_char(text)
	chars_sorted_list = sort_dict(chars_dict)
	print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
	with open(path) as f:
		return f.read()

def print_report(book_path, num_words, chars_sorted_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

main()
