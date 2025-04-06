import sys

from stats import get_num_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars_dict(text)
    report(book_path, num_words, num_chars)


def sort_on(dict):
    return dict["num"]


def char_isalpha_and_sorted_list(dict):
    chars_sorted = []
    for char in dict:
        if char.isalpha():
            chardict = {"char": char, "num": dict[char]}
            chars_sorted.append(chardict)
    chars_sorted.sort(reverse=True, key=sort_on)
    return chars_sorted


def report(book_path, num_words, num_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    chars_sorted = char_isalpha_and_sorted_list(num_chars)
    for char in range(0, len(chars_sorted)):
        print(
            # f"'{chars_sorted[char]["char"]}' appears {chars_sorted[char]["num"]} times in the book"
            f"{chars_sorted[char]['char']}: {chars_sorted[char]['num']}"
        )
    print("--- End report ---")


def get_num_chars_dict(text):
    chars = {}
    for char in text:
        lower = char.lower()
        if lower not in chars:
            chars[lower] = 1
        elif lower in chars:
            chars[lower] += 1
    return chars


def get_book_text(file):
    with open(file) as f:
        return f.read()


main()
