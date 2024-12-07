str=input()
vowels="aeiouAEIOU"
if any(char in vowels for char in str):
    print("The string contains a vowel.")
else:
    print("The string does not contain any vowel.")