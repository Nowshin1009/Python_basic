def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def show_palindromic_substrings(s):
    n = len(s)
    unique_substrings = set()  # Set to store unique palindromic substrings
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j + 1]):
                unique_substrings.add(s[i:j + 1])

    # Print unique palindromic substrings
    for substring in unique_substrings:
        print(substring)

# Input string
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

# Print unique palindromic substrings
print("Unique palindromic substrings:")
show_palindromic_substrings(input_string)
