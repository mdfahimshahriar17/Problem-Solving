def check_palindrome(text):
    is_palindrome = False

    palindrome = ""

    len_text = len(text)-1

    while len_text >= 0:

        palindrome += text[len_text]

        len_text -= 1
    

    if palindrome == text:
        is_palindrome = True
    
    return is_palindrome



text = input()
result = check_palindrome(text=text)
if result:
    print("YES")
else:
    print("NO")

