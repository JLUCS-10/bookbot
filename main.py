from stats import get_num_words, get_characters, build_sorted_char_list
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book1 =  sys.argv[1]
    book_text = get_book_text(book1)
    num_words = get_num_words(book_text)
    dict_char = get_characters(book_text)
    sorted_list = build_sorted_char_list(dict_char)
    
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/{book1}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    
main()