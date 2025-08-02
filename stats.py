def book_word_count(book_contents):
    words = book_contents.split()
    return f"{len(words)} words found in the document"

def book_char_count(book_contents):
    char_list = {}
    for char in book_contents:
        if char.lower() not in char_list:
            char_list[char.lower()] = 1
        else:
            char_list[char.lower()] += 1
    return char_list