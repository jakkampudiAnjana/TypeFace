#step1:  Take the input word
#step2: open the file
#step3: read a word
#step4: check weather the given word matches the sound of given input(pass to a function)
step5: if yes  append into list
#step6: Retain the first letter of the word as it is
#step7: Encode the Consonants
#step8:drop the vowels
#step9 :  make the Code Length 4
#step10: finally return the hashcode generated
x=input
#soundex_generator(x)
l=[]
search=soundexgen(x)
fname = input("Enter file name: ")
with open(fname, 'r') as f:
    for line in f:
        for word in line.split():
            if(soundexgen(word)==search):
                l.append(word)        
def soundexgen(token):

	
	token = token.upper()
	soundex = ""
	soundex += token[0]

	dictionary = {"BFPV": "1", "CGJKQSXZ": "2",
				"DT": "3",
				"L": "4", "MN": "5", "R": "6",
				"AEIOUHWY": "."}

	for char in token[1:]:
		for key in dictionary.keys():
			if char in key:
				code = dictionary[key]
				if code != '.':
					if code != soundex[-1]:
						soundex += code

	soundex = soundex[:7].ljust(7, "0")

	return soundex