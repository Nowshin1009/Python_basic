def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def show_palindromic_substrings(s):
    n = len(s)
    unique_substrings = set()  
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j + 1]):
                unique_substrings.add(s[i:j + 1])

    for substring in unique_substrings:
        print(substring)

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

print("Unique palindromic substrings:")
show_palindromic_substrings(input_string)
