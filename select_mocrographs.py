from sys import argv

goodlist = open('goodlist').readlines()
infile = open('particles.star')
#print (goodlist)

for i in open('particles.star'):
	lines = infile.readline()
	#print (lines)
	if len(lines) < 30:
		print (lines[:-1])
	elif lines[100:126]+'\n' in goodlist:
		print (lines[:-1])
