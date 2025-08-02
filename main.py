from stats import book_word_count

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents


def main():
    frankenstein_path = "./books/frankenstein.txt"
    book = get_book_text(frankenstein_path)
    word_count = book_word_count(book)
    print(word_count)


main()