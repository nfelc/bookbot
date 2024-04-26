def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    letters = letter_count(text)
    listed_letters = dict_to_list(letters)
    listed_letters.sort(reverse=True, key=sort_on)    
    print(f"--- begin report of {book_path}---")
    print(f"{words} words found in the document")
    print()
    for letter in listed_letters:
        print(f"The '{letter["char"]}' character was found {letter["num"]} times")
    print("---end report---")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    count = {}
    for c in text:
        lower = c.lower()
        if lower in count:
            count[lower] += 1
        else: 
            count[lower] = 1
    return count

def dict_to_list(dict):
    chars = []
    for i in dict:
        if i.isalpha() == True:
            chars.append({"char": i, "num":dict[i]})
    return chars

def sort_on(dict):
    return dict["num"]


main()