def book_word_count(book_contents):
    words = book_contents.split()
    return f"{len(words)} total words"

def book_char_count(book_contents):
    char_list = {}
    for char in book_contents:
        if char.lower() not in char_list:
            char_list[char.lower()] = 1
        else:
            char_list[char.lower()] += 1
    return char_list

def sort_char(unsorted_char):
    list_of_char = []
    for char in unsorted_char:
        current_char = {}
        current_char["char"] = char
        current_char["num"] = unsorted_char[char]
        list_of_char.append(current_char)
    list_of_char.sort(reverse=True, key=sort_on)
    return list_of_char
    
def sort_on(items):
    return items["num"]
    