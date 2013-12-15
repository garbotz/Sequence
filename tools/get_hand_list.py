# returns a list of words that fit criteria.
import sys

word_source = open("dict.txt").read().splitlines()
new_dict = []

q_qwerty = {0:"qaz",1:"wsx",2:"edc",3:"rfvtgb",
	4:"yhnujm",5:"ik,",6:"ol.",7:"p;/\'[]"}
select = ["left","right","1left","1right","2left","2right",
	"3left","3right","4left","4right","5left","5right","6left","6right","equal"]
choice = ""

options = sys.argv

def main():

	if options[1] == "h":
		print "-mode -min -max -hand"
		print "arg1: weight, rhythm"
		print "arg2: min length"
		print "arg3: max length"
		print "arg4:"
		print "weight: left, right, [1-6]left, [1-6]right, equal (filter by hand weight)"
		print "rhythm: left, right (starting hand)"
		exit()

	matches = 0
	rejects = 0

	for w in word_source:
		if len(w) >= int(options[2]) and len(w) <= int(options[3]):
			if options[1] == "weight":
				if wordcheck(w):
					with open("weight_{}_{}_{}.txt".format(options[4],options[2],options[3]),'a') as tmp:
						tmp.write("{}\n".format(w))
						matches += 1
				else:
					rejects += 1
			elif options[1] == "rhythm":
				if backandforth(w):
					with open("rhythm_{}_{}_{}.txt".format(options[4],options[2],options[3]),'a') as tmp:
						tmp.write("{}\n".format(w))
						matches += 1
				else:
					rejects += 1
			# elif options[1] == "difficulty":
				
	print "%s matching words found."%matches
	print "%s rejected."%rejects

def wordcheck(word):
	fingers = getfingers(word)
	hand = gethand(fingers)
	if hand == options[4]:
		return True
	else:
		return False

def backandforth(word):
	fingers = getfingers(word)
	h = options[4]
	for f in fingers:
		if f <= 3:
			if h == "left":
				return False
			else: 
				h = "left"
		else:
			if h == "right":
				return False
			else:
				h = "right"
	return True

def getfingers(word):
	tmplist = []
	tmp = list(word)
	for letter in tmp:
		for value in q_qwerty:
			if letter in q_qwerty[value]:
				tmplist.append(value)
	return tmplist

def gethand(fingers):
	l = 0
	r = 0

	for x in fingers:
		if x <= 3:
			l += 1
		else:
			r += 1

	diff = (l - r)
	if diff < 0: diff *= -1

	if   r == 0:
		return select[0]
	elif l == 0:
		return select[1]

	elif l-6 > r:
		return select[12]
	elif r-6 > l:
		return select[13]

	elif l-5 > r:
		return select[10]
	elif r-5 > l:
		return select[11]
		
	elif l-4 > r:
		return select[8]
	elif r-4 > l:
		return select[9]

	elif l-3 > r:
		return select[6]
	elif r-3 > l:
		return select[7]

	elif l-2 >= r:
		return select[4]
	elif r-2 >= l:
		return select[5]		

	elif l-1 >= r:
		return select[2]
	elif r-1 >= l:
		return select[3]

	else:
		return select[14]

main()