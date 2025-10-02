def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        file_contents = file.read()
    return file_contents

def count_words(content: str) -> str:
    split_content = content.split()
    num_words = len(split_content)
    return f"Found {num_words} total words."

def count_chars(content: str) -> dict[str, int]:
    result = {}
    lower_content = content.lower()
    for char in lower_content:
        if char not in result:
            result.update({char: 1})
        else:
            result.update({char: result[char] + 1})
    return result

def dict_to_list(char_count: dict[str, int]) -> list:
    unsorted = []
    for char in char_count:
        if not char.isalpha():
            continue
        else:
            unsorted.append({"char": char, "num": char_count[char]})
    return unsorted

def sort_on(items):
    return items["num"]

def sort_list(l: list) -> list:
    l.sort(reverse=True, key=sort_on)
    return l

def generate_report(path:str) -> str:
    report = (f"============ BOOKBOT ============\n"
              f"Analyzing book found at {path}...\n"
              f"----------- Word Count ----------\n"
              f"{count_words(get_book_text(path))}\n"
              f"--------- Character Count -------\n")

    sorted_list = sort_list(dict_to_list(count_chars(get_book_text(path))))
    for entry in sorted_list:
        report += f"{entry["char"]}: {entry["num"]}\n"

    report += "============= END ==============="
    return report

