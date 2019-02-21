
def trigramGenerator(x):

	sentence = []
	for line in x:
		temp = line.split()
		sentence += temp

	gramsList = []

	first = 0
	second = 1
	third = 2
	for gram in sentence:
		if(first <= (len(sentence) - 3)):
			trigram = []
			trigram.append(sentence[first])
			trigram.append(sentence[second])
			trigram.append(sentence[third])
			gramsList.append(trigram)
		first += 1
		second += 1
		third += 1	

	return gramsList	

def countTrigram(gramsList):

	countsList = []

	for trigram in gramsList:
		count = 0
		for t in gramsList:
			if(t == trigram):
				count += 1
		countsList.append(count)

	return countsList

def getMostOccuring(countsList, gramsList):
	idx = 0
	maxOccurences = 0
	bestIdx = 0
	for x in countsList:
		if(x > maxOccurences):
			maxOccurences = x
			bestIdx = idx
		idx +=1

	beginning = gramsList[bestIdx]
	return beginning


def main():

	book = "catinthehat.txt"

	x = open(book)

	print("MODE: ", x.mode)

	gramsList = trigramGenerator(x)	
	countsList = countTrigram(gramsList)

	start = getMostOccuring(countsList, gramsList)

	print(start)

	file = open("trigrams_output.txt", "w")

	idx = 0
	for g in gramsList:
		file.write(str(g))
		file.write("	")
		file.write(str(countsList[idx]))
		file.write("\n")

		idx += 1

	file.close()

main()