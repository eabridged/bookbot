#!/bin/env python3
from stats import get_word_count, count_symbols, sort_dictionary
from sys import argv, exit

if len(argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

PATH = argv[1]
def get_book_text(filepath: str) -> str:
    """Reads the content of a book from a text file."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


text = get_book_text(PATH)
wordCount = get_word_count(text)

print(
f"""============ BOOKBOT ============
Analyzing book found at {PATH}...
----------- Word Count ----------
Found {wordCount} total words
--------- Character Count -------
""", end="")

for i in sort_dictionary(count_symbols(text)):
    key = [key for key in i.keys()][0]
    value = [value for value in i.values()][0]
    if (key.isalpha()): print(f"{key}: {value}")

