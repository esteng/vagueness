

def regex_adjective(word):
	wordList = word
	firstLetter = worList[0].lower()
	firstLetterCap = wordList[0].upper()
	restOfWord = wordList[1:].lower()
	print("([iI]s|[aA]n|[aA])?(([^\w])+(["+firstLetter+firstLetterCap+"]"+restOfWord+")[^\w])")


def regex_noun(word):
	wordList = word
	firstLetter = wordList[0].lower()
	firstLetterCap = wordList[0].upper()
	restOfWord = worList[1:].lower()
	print("([iI]s)?([aA]n|[aA])?(([^\w])+(["+firstLetter+firstLetterCap+"]"+restOfWord+")[^\w])")

	
