from stats import get_word_count, get_character_count, get_sorted_dict
import sys

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = (sys.argv[1])
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_dict = get_sorted_dict(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_dict:
        if(d["char"].isalpha()):
            print(f"{d["char"]}: {d["num"]}")

def get_book_text(file):
    with open(file) as f:
        return f.read()

main()