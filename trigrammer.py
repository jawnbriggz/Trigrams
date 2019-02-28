
import re
import sys
import string
import operator

def book_parser(x):

	full_text = []

	for line in x:
#		strip of punctuation and lowercase it
		line = line.lower()
		line = line.translate(str.maketrans('','',string.punctuation))
		temp = line.split()
		full_text += temp	

	OVERALL_LENGTH = len(full_text)

	return(full_text, OVERALL_LENGTH)


def gramGenerator(full_text, OVERALL_LENGTH):

	unigrams = {}
	bigrams = {}
	trigrams = {}

	first = 0
	second = 1
	third = 2

	for t in full_text:

#		construct grams
		bigram = []
		trigram = []

		if(first <= OVERALL_LENGTH - 3):
			trigram.append(full_text[first])
			trigram.append(full_text[second])
			trigram.append(full_text[third])

		if(first <= OVERALL_LENGTH - 2):
			bigram.append(full_text[first])
			bigram.append(full_text[second])

		first += 1
		second += 1
		third += 1

		s = gram_to_string(trigram)
		strang = gram_to_string(bigram)

#		create the dictionaries
		if(s in trigrams):
			trigrams[s] += 1
		else:
			trigrams[s] = 1

		if(strang in bigrams):
			bigrams[strang] += 1
		else:
			bigrams[strang] = 1

		if(t in unigrams):
			unigrams[t] += 1
		else:
			unigrams[t] = 1	

	return(unigrams, bigrams, trigrams)


def gram_to_string(gram):

	s = ""
	idx = 0
	y = len(gram)
	for w in gram:
		if(idx == y):
			s += w
		else:
			s += w
			s += " "
		idx += 1

	return s


def print_to_file(bigrams, trigrams):

#	save trigrams and # of occurrences to a file
	file = open("trigrams_output.txt", "w")

	for t in trigrams:
		count = str(trigrams[t])
		file.write(t)
		file.write("	")
		file.write(count)
		file.write("\n")

	file.close()

#	save bigrams and # of occurrences to a file
	file = open("bigrams_output.txt", "w")

	for t in bigrams:
		count = str(bigrams[t])
		file.write(t)
		file.write("	")
		file.write(count)
		file.write("\n")

	file.close()


def main():

	book = sys.argv[1]

#	open the file, do what you gotta do and then close it.
	x = open(book)

	parsed_text = book_parser(x)
	text = parsed_text[0]
	OVERALL_LENGTH = parsed_text[1]

	x.close()

#	GET THE GRAMS
	grams = gramGenerator(text, OVERALL_LENGTH)

	unigrams = grams[0]
	bigrams = grams[1]
	trigrams = grams[2]

	most_occurring_word = max(unigrams.items(), key=operator.itemgetter(1))[0]
	most_occurring_bigram = max(bigrams.items(), key=operator.itemgetter(1))[0]
	most_occurring_trigram = max(trigrams.items(), key=operator.itemgetter(1))[0]

	print("THE MOST OCCURRING WORD: ", most_occurring_word)
	print("THE MOST OCCURRING BIGRAM: ", most_occurring_bigram)
	print("THE MOST OCCURRING TRIGRAM: ", most_occurring_trigram)


main()