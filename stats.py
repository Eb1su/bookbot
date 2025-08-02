def book_word_count(book_contents):
    words = book_contents.split()
    return f"{len(words)} words found in the document"