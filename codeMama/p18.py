def palindrome(num):
    if num == num[::-1]:
        print (f"{num} is a palindrome number")
    else:
        print (f"{num} is not a palindrome number")
    
x = int(input())
palindrome(str(x))