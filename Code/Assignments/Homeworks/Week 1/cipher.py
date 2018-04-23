phrase = raw_input("Enter sentence to encrypt: ")
shift = int(raw_input("Enter shift value: "))

encoded_phrase = ''

for c in phrase:
	if ord(c) >= 65 and ord(c) <= 90:
		if ord(c)+ shift < 90:
			encoded_letter = chr(ord(c)+shift)
		else:
			encoded_letter = chr((ord(c)+shift)%91+65)
	elif ord(c) >= 97 and ord(c)<= 122:
		if ord(c)+shift < 123:
			encoded_letter = chr(ord(c)+shift)
		else:
			encoded_letter = chr((ord(c)+shift)%123+97)
	else:
		encoded_letter = c

	encoded_phrase = encoded_phrase + encoded_letter

print "The encoded phrase is:", encoded_phrase