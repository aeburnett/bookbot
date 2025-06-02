def main():
    book_path = ("books/frankenstein.txt")
    word_count = get_word_count(book_path)
    print(f"{word_count} words found in the document")

def get_book_text(file):
    with open(file) as f:
        return f.read()

def get_word_count(file):
    count = 0;
    with open(file) as f:
        text = f.read()
        for i in text.split():
            count += 1
    return count

main()