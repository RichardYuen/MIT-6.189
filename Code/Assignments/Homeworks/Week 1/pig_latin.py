VOWELS = ['a', 'e', 'i', 'o', 'u']
dual_letters = ['th', 'st', 'qu', 'pl', 'tr']
punctuation = ['!', '?', ':', ';']
phrase = ''

def pig_latin(word):
    # word is a string to convert to pig-latin
    new_word = []
    ##### YOUR CODE HERE #####
    if word[len(word)-1] in punctuation:
    	punct = word[len(word)-1]
    	word_len = len(word) - 1
    else:
    	punct = ''
    	word_len = len(word)

    if word[0] in VOWELS:
        new_word = word[:word_len] +'hay'
        return new_word + punct
    elif word[:2] in dual_letters:
        new_word = word[2:word_len] + word[:2] + 'ay'
        return new_word + punct
    else:
    	new_word = word[1:word_len] + word[0] + 'ay'
    	return new_word + punct
 

while True:
	phrase = raw_input("Enter a phrase contain only words and spaces: ")
	if phrase == "QUIT":
		break
	
	lower_phrase = phrase.lower()
	word_list = lower_phrase.split()

	new_word_list = [pig_latin(word) for word in word_list]
	new_string = ' '.join(new_word_list)
	print new_string