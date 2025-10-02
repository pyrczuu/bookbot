from stats import get_book_text, count_chars, dict_to_list, sort_list, sort_on, generate_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(generate_report(sys.argv[1]))


main()