def is_palindrome(string):
	string = string.lower()
	if len(string) <= 1:
		return True
	else:
		return string[0] == string[-1] and is_palindrome(string[1:-1])

print is_palindrome("ABBA")
print is_palindrome("Able was i ere i saw Elba")
print is_palindrome("Able")
print is_palindrome("Shit!")
print is_palindrome("ana")
print is_palindrome("anna")
print is_palindrome("")
