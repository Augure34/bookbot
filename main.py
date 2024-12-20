def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    generate_report(book_path, num_words, chars_dict)

def generate_report(book_title, word_count, chars_dict):
    print(f"||| {book_title} |||")
    print(f"{word_count} total words in book.")
    for char in chars_dict:
        if char.isalpha():
            print(f"Char {char.upper()} exists {chars_dict[char]} times.")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
