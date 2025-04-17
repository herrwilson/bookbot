from stats import word_counter, character_counter, dictionary_sorter
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]    
    content = get_book_text(path_to_book)
    
    content = get_book_text(path_to_book)
    word_count = word_counter(content)
    character_count = character_counter(content)
    sorted_characters = dictionary_sorter(character_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}...")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_characters:
        if i.isalpha() == True:
            print(f"{i}: {sorted_characters[i]}")
    print("============= END ===============")

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()
    
main()