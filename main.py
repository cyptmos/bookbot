from stats import num_of_words, num_of_characters, sorted_list
import sys


def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_string = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = num_of_words(book_string)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")




    characters = sorted_list(num_of_characters(book_string))
    for x in characters:
        if x['char'].isalpha():
            print(f"{x['char']}: {x['num']}")

    print("============= END ===============")



main()
