from stats import book_word_count
from stats import book_char_count
from stats import sort_char

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents

def main():
    book_path = "./books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = book_word_count(book)
    character_count = book_char_count(book)
    sort_count = sort_char(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path[2:]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count}")
    print("--------- Character Count -------")
    for entry in sort_count:
        count = entry["num"]
        char = entry["char"]
        if char.isalpha() == True:
            print(f"{char}: {count}")
    print("============= END ===============")


main()