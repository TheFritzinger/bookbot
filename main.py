def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    get_num_characters(text)
    char_count = get_num_characters(text)
    print(f"""--- Begin report of {book_path} ---
    {num_words} words found in the document \n""" )
    for char, number in char_count.items():
        if char.isalpha():
            print(f"The '{char}' character was found {number} times")

def get_num_words(text):    # counts words in the given text
    words = text.split()
    return len(words)

def get_book_text(path):    # reads the text from a file
    with open(path) as f:
        return f.read()
    
def get_num_characters(text):   # counts how often every character appears in the given text
    lowered_text = text.lower()
    unique_char = sorted(set(lowered_text))
    char_dict = {}
    for char in unique_char:
        char_count = lowered_text.count(char)
        char_dict[char] = char_count
    return char_dict
        

main()
