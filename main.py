def main():
    book_path = ("books/frankenstein.txt")
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()