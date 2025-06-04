from stats import get_word_count, get_character_count

def main():
    book_path = ("books/frankenstein.txt")
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")
    character_count = get_character_count(book_text)
    print(character_count)

def get_book_text(file):
    with open(file) as f:
        return f.read()

main()