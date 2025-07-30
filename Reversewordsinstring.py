def reverse_words(s: str) -> str:
    """
    Given a string s, reverse the order of words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    For example:
    reverse_words("the sky is blue") == "blue is sky the"
    reverse_words("  hello world  ") == "world hello"
    reverse_words("a good   example") == "example good a"
    """
    words = s.strip().split()  # Split the string into words after removing leading/trailing spaces
    reversed_words = words[::-1]  # Reverse the order of the words list
    return " ".join(reversed_words)  # Join the reversed words with a single space

# Example Usage:
string1 = "the sky is blue"
reversed_string1 = reverse_words(string1)
print(f"Original: '{string1}'")
print(f"Reversed: '{reversed_string1}'")

string2 = "  hello world  "
reversed_string2 = reverse_words(string2)
print(f"Original: '{string2}'")
print(f"Reversed: '{reversed_string2}'")

string3 = "a good   example"
reversed_string3 = reverse_words(string3)
print(f"Original: '{string3}'")
print(f"Reversed: '{reversed_string3}'")

string4 = ""
reversed_string4 = reverse_words(string4)
print(f"Original: '{string4}'")
print(f"Reversed: '{reversed_string4}'")

string5 = "single"
reversed_string5 = reverse_words(string5)
print(f"Original: '{string5}'")
print(f"Reversed: '{reversed_string5}'")
