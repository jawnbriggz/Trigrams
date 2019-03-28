
import sys

def word_probability(word, vocab_size):

	uni = open("unigrams_output.txt")

	for line in uni:
		temp = line.split()
		if(temp[0] == word):
			uni.close()
			count = int(temp[-1])
			return ((count/int(vocab_size)), count)

	print(word)

def bigram_probability(bigram, unigram_occurrences):

	temp = bigram.split()
	w1 = temp[0]

	bi = open("bigrams_output.txt")
	for line in bi:
		temp = line.split()
		if(len(temp) > 2):
			temp_bigram = temp[0] + " " + temp[1]
			if(temp_bigram == bigram):
				bigram_count = int(temp[-1])

	bi.close()
	return ((bigram_count/unigram_occurrences), bigram_count)


def trigram_probability(gram, bigram_occurrences):

	tri = open("trigrams_output.txt")

	for line in tri:
		temp = line.split()
		if(len(temp) > 3):
			trigram = temp[0] + " " + temp[1] + " " + temp[2]
			if(trigram == gram):
				count = int(temp[-1])
				tri.close()
				return count/bigram_occurrences


def probabilities(gram, word_count):

	temp = gram.split()

	# create unigram
	unigram = temp[0]
	
	# create bigram
	bigram = []
	bigram.append(temp[0])
	bigram.append(temp[1])
	bigram = gram_to_string(bigram)

	# create trigram
	trigram = gram

	# get probability of a word
	word_tuple = word_probability(unigram, word_count)
	probably = word_tuple[0]
	unigram_occurrences = word_tuple[1]

	# in case that gram is only a word
	if(len(temp) == 1):
		return probably

	# get probability of a bigram
	bigram_tuple = bigram_probability(bigram, unigram_occurrences)
	bigram_occurrences = bigram_tuple[1]
	probably *= bigram_tuple[0]

	# in case gram is only a bigram
	if(len(temp) == 2):
		return probably

	# get probability of a trigram
	probably *= trigram_probability(gram, bigram_occurrences)

	return probably


def gram_to_string(gram):

	s = ""
	idx = 0
	y = len(gram)
	for w in gram:
		if(idx == y-1):
			s += w
		else:
			s += w
			s += " "
		idx += 1

	return s


def main():

	trigrams = open("trigrams_output.txt")

	gram = sys.argv[1]
	first = True
	first_line = trigrams.readline()
	word_count = first_line.split()[2]
	n_gram = len(gram.split())

	if(n_gram == 3):
		for line in trigrams:

			info = line.split()

			if(len(info) > 2):

				trigram = info[0] + " " + info[1] + " " + info[2]

				if(trigram == gram):
					x = probabilities(gram, word_count)
					print("\nTHE PROBABILITY OF ", gram, " IS:\n ", x)
					print()
					return
		print("that n-gram does not exist")

	elif(n_gram > 3):

		sentence_trigrams = []
		idx = 1
		frags = gram.split()
		temp = []

		for w in frags:
			
			temp.append(w)

			if(idx == len(frags)):
				sentence_trigrams.append(temp)
			elif(idx % 3 == 0 and idx != 0):
				sentence_trigrams.append(temp)
				temp = []

			idx = idx + 1

		sent_prob = 1
		for t in sentence_trigrams:
			temp_trigram = gram_to_string(t)
			temp_prob = probabilities(temp_trigram, word_count)
			sent_prob *= temp_prob

		formatted_probability = format(sent_prob, ".12f")

		print("\nTHE PROBABILITY OF THE SENTENCE ", gram, " IS \n\n", formatted_probability)
		print()

	else:
		print("you messed up somehow")

main()