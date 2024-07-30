# Write a program to check if a given string is a palindrome.
# Using function and lower() & replace() methods

def is_palindrome(s):
    s = s.lower().replace(" ","")       
# Convert to lowercase and remove spaces using the lowe() and replace() methods.        
    return s == s[::-1]     # check is the string is equal to it's reverse using slicing

# Test the function with an example 

input_string = input("Enter any word to check if a given string is a palindrome or not: ")
result = is_palindrome(input_string)
print(result) 