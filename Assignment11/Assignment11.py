import re

# Problem 1: Check allowed characters
def problem_1():
    print("Problem 1")
    # Test strings
    tests = [
        "ABCDEFabcdef123450",
        "*&%@#!}{"
    ]
    # Pattern (only letters and numbers)
    pattern = r"^[A-Za-z0-9]+$"
    for text in tests:
        # Match checks from the start
        if re.match(pattern, text):
            print(f"'{text}' -> Pass")
        else:
            print(f"'{text}' -> Fail")

# Problem 2: a followed by zero or more b's
def problem_2():
    print("Problem 2")
    # Test strings
    tests = [
        "ab",
        "abc",
        "a",
        "ab",
        "abb"
    ]
    # Pattern (a then zero or more b's)
    pattern = r"ab*"
    for text in tests:
        # using fullmatch so the whole string has to match
        if re.fullmatch(pattern, text):
            print(f"'{text}' -> Pass")
        else:
            print(f"'{text}' -> Fail")

# Problem 3: a followed by one or more b's
def problem_3():
    print("Problem 3")
    # Test strings
    tests = [
        "ab",
        "abc",
        "a",
        "ab",
        "abb"
    ]
    # Pattern (a then at least one b)
    pattern = r"ab+"
    for text in tests:
        # fullmatch makes sure the whole string fits the pattern
        if re.fullmatch(pattern, text):
            print(f"'{text}' -> Pass")
        else:
            print(f"'{text}' -> Fail")

# Problem 4: lowercase letters joined by an underscore
def problem_4():
    print("Problem 4")
    # Test strings
    tests = [
        "aab_cbbbc",
        "aab_Abbbc",
        "Aaab_abbbc"
    ]
    # Pattern (lowercase letters, underscore, lowercase letters)
    pattern = r"^[a-z]+_[a-z]+$"
    for text in tests:
        # fullmatch makes sure the whole string fits the pattern
        if re.fullmatch(pattern, text):
            print(f"'{text}' -> Pass")
        else:
            print(f"'{text}' -> Fail")

# Problem 5: match a word at the beginning of a string
def problem_5():
    print("Problem 5")
    tests = [
        "The quick brown fox jumps over the lazy dog.",
        " The quick brown fox jumps over the lazy dog."
    ]
    # Pattern (word characters at the very start of the string)
    pattern = r"^\w+"
    for text in tests:
        match = re.match(pattern, text)
        if match:
            print(f"'{text}' -> Starts with word: '{match.group()}'")
        else:
            print(f"'{text}' -> Does not start with a word")

# Problem 6: match a word containing 'z'
def problem_6():
    print("Problem 6")
    tests = [
        "The quick brown fox jumps over the lazy dog.",
        "Python Exercises."
    ]
    # Pattern (any word that has a 'z' somewhere in it)
    pattern = r"\w*z\w*"
    for text in tests:
        # find all words that contain 'z'
        matches = re.findall(pattern, text)

        # filter out empty strings (regex can match empty if no z)
        matches = [m for m in matches if m != ""]

        if matches:
            print(f"'{text}' -> Words with 'z': {matches}")
        else:
            print(f"'{text}' -> No words with 'z'")

# Problem 7: remove leading zeros from an IP address
def problem_7():
    print("Problem 7")
    ip = "216.08.094.196"
    print("Original IP:", ip)
    # split the IP into its 4 parts
    parts = ip.split(".")
    cleaned_parts = []
    for p in parts:
        # remove leading zeros using regex
        new_p = re.sub(r"^0+", "", p)
        # if the whole part was zeros, make it "0"
        if new_p == "":
            new_p = "0"
        cleaned_parts.append(new_p)
    cleaned_ip = ".".join(cleaned_parts)
    print("Cleaned IP:", cleaned_ip)

# Problem 8: search for literal strings inside a sentence
def problem_8():
    print("Problem 8")
    text = "The quick brown fox jumps over the lazy dog."
    words = ["fox", "dog", "horse"]
    for w in words:
        # re.escape makes sure the word is treated literally
        pattern = re.escape(w)

        if re.search(pattern, text):
            print(f"'{w}' was found in the text")
        else:
            print(f"'{w}' was not found in the text")

# Problem 9: search for a literal string and show its location
def problem_9():
    print("Problem 9")
    text = "The quick brown fox jumps over the lazy dog."
    word = "fox"
    # treat the word literally (in case it has special characters)
    pattern = re.escape(word)
    match = re.search(pattern, text)
    if match:
        print(f"'{word}' was found in the text")
        print("Start index:", match.start())
        print("End index:", match.end())
    else:
        print(f"'{word}' was not found in the text")

# Problem 10: replace whitespaces with underscores and vice versa
def problem_10():
    print("Problem 10")
    tests = [
        "Regular Expressions",
        "Code_Examples"
    ]
    for text in tests:
        print("\nOriginal:", text)
        # replace spaces with underscores
        no_spaces = re.sub(r"\s", "_", text)
        # replace underscores with spaces
        no_underscores = re.sub(r"_", " ", text)
        print("Spaces → Underscores:", no_spaces)
        print("Underscores → Spaces:", no_underscores)

# Problem 11: extract year, month, and day from a URL
def problem_11():
    print("Problem 11")
    url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
    print("URL:", url)
    # regex to capture year/month/day
    pattern = r"/(\d{4})/(\d{2})/(\d{2})/"
    match = re.search(pattern, url)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        print("Year:", year)
        print("Month:", month)
        print("Day:", day)
    else:
        print("No date found in the URL")

# Problem 12: find all words starting with 'a' or 'e'
def problem_12():
    print("Problem 12")
    text = ("The following example creates an ArrayList with a capacity of 50 elements. "
            "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.")
    # pattern: words starting with a or e (case-insensitive)
    pattern = r"\b[aAeE]\w*"
    matches = re.findall(pattern, text)
    print("Words found:", matches)

# Problem 13: replace spaces, commas, and dots with colons
def problem_13():
    print("Problem 13")
    text = "Python Exercises, PHP exercises."
    print("Original:", text)
    # replace space, comma, or dot with colon
    result = re.sub(r"[ ,.]", ":", text)
    print("Modified:", result)

# Problem 14: find all words starting with 'a' or 'e'
def problem_14():
    print("Problem 14")
    text = ("The following example creates an ArrayList with a capacity of 50 elements. "
            "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.")
    # words starting with a or e (case-insensitive)
    pattern = r"\b[aAeE]\w*"
    matches = re.findall(pattern, text)
    print("Words found:", matches)

# Problem 15: remove multiple spaces from a string
def problem_15():
    print("Problem 15")
    text = "Python      Exercises"
    print("Original:", repr(text))
    # replace 1+ spaces with a single space
    cleaned = re.sub(r"\s+", " ", text)
    print("Cleaned:", repr(cleaned))

# Menu System
def main():
    while True:
        print("\n=== Regex Assignment Menu ===")
        print("0. Quit")
        for i in range(1, 16):
            print(f"{i}. Problem {i}")
        choice = input("Choose an problem: ")
        if choice == "0":
            print("Goodbye!")
            break
        # Dynamically call the correct function
        try:
            globals()[f"problem_{int(choice)}"]()
        except (KeyError, ValueError):
            print("Invalid choice. Try again.")




if __name__ == "__main__":
    main()
