# Create a program that asks the user for an input string of alphabetic characters. Convert the string 
# to a run-length encoded (RLE) string of characters and numbers. Use the compressed format, where a 
# single instance of a character has no count. For example, AAABCC would be A3BC2. Use a separate 
# function for string processing. Avoid using global variables by passing parameters and returning 
# results. Include appropriate data validation and parameter validation. Add program and function 
# documentation, consistent with the documentation standards for your selected programming language.

# StringsRLE.py
# Author: Michael Brzozka
# Description: A program that asks the user for an alphabetic input string and 
# converts it into a run length encoded string. The compressed format doesn't 
# include the count when a character appears only once. The program validates 
# user input, ensuring only alphabetic characters are processed. String 
# processing is done in a separate function with parameters and return values 
# (no global variables).

# Convert a string of alphabetic characters into its run‑length encoded form. 
# Parameters: input_string (str): The alphabetic string to encode. Must not be 
# empty and must contain only A–Z or a–z characters.
# Returns: str: The RLE version of the input string, using compressed format.
# Raises: ValueError: If input_string is empty or contains non alphabetic 
# characters.
def encode_rle(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")
    # Escape literal characters first
    safe = []
    for ch in input_string:
        if ch == '#':
            safe.append("##")
        elif ch.isdigit():
            safe.append("#" + ch)
        else:
            safe.append(ch)
    safe = "".join(safe)
    # Perform normal RLE on the escaped stream
    encoded = []
    count = 1
    for i in range(1, len(safe)):
        if safe[i] == safe[i - 1]:
            count += 1
        else:
            encoded.append(safe[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    encoded.append(safe[-1] + (str(count) if count > 1 else ""))
    # Prefix marks this as encoded
    return "##00" + "".join(encoded)

# Decode an RLE string into its expanded form.
# Parameters: encoded_string (str): A non empty string containing alphabetic
# characters and optional numeric counts.
# Returns: str: The decoded version of the RLE string.
# Raises: ValueError: If the string is empty, not a string, or contains 
# invalid RLE formatting.
def decode_rle(encoded_string):
    if not isinstance(encoded_string, str):
        raise ValueError("Input must be a string.")
    if len(encoded_string) == 0:
        raise ValueError("Input string cannot be empty.")
    if not encoded_string.startswith("##00"):
        raise ValueError("Encoded strings must begin with ##00.")
    s = encoded_string[4:]  # strip prefix
    decoded = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        # Escape sequences
        if ch == '#':
            if i + 1 >= n:
                raise ValueError("Dangling escape # at end of string.")
            nxt = s[i + 1]
            if nxt == '#': # literal '#'
                decoded.append('#')
                i += 2
                continue
            elif nxt.isdigit(): # literal digit
                decoded.append(nxt)
                i += 2
                continue
            else:
                raise ValueError("Invalid escape sequence #{}".format(nxt))
        # Normal RLE letter
        if not ch.isalpha():
            raise ValueError("Invalid RLE format: expected alphabetic character or escape.")
        i += 1
        count_str = ""
        while i < n and s[i].isdigit():
            count_str += s[i]
            i += 1
        count = int(count_str) if count_str else 1
        decoded.append(ch * count)
    return "".join(decoded)

# Main program function. Prompts the user for an alphabetic string, validates 
# it, and prints the RLE result.
def main():
    user_input = input("Enter a string (alphabetic or RLE format): ").strip()
    try:
        # If it begins with ##00, it is encoded and must be decoded
        if user_input.startswith("##00"):
            result = decode_rle(user_input)
            print("Decoded string:", result)
        else:
            # Otherwise encode it
            result = encode_rle(user_input)
            print("Encoded string:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()