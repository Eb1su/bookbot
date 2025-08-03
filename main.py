import sys

from stats import book_word_count
from stats import book_char_count
from stats import sort_char

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents

def formatted_out(book_path, word_count, sorted_char):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count}")
    print("--------- Character Count -------")
    for entry in sorted_char:
        if entry["char"].isalpha() == True:
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

def main():
    #If no file path has been provided return the following message
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = book_word_count(book)
    character_count = book_char_count(book)
    sort_count = sort_char(character_count)
    
    formatted_out(book_path, word_count, sort_count)

main()