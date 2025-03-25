from stats import get_num_words, get_num_chars, sorted_dict
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]    
    book_text = get_book_text(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{path_to_book}'")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_dict(get_num_chars(book_text)).items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()