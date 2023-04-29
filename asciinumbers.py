import sys
g = sys.argv
a = g[2:]
final = []
dfinal = ''
bc = ['"','[',']',',',"'"," "]
if g[1] == "-e":
	#print("made in chrome os text editor")
	for x in a:
		b = 0
		#print(x)
		while True:
			b = b + 1
			#print(b)
			c = x[b-1]
			final.append(ord(c))
			#print(len(x))
			if b == len(x):
				final.append("32")
				break
	
	print(*final)
if g[1] == "-d":
	#print("made in chrome os text editor")
	for x in a:
		final.append(chr(int(x)))
	for x in final:
                if x == "32":
                        dfinal = dfinal + " "
                else:
                        dfinal = dfinal + x
	print(dfinal)
if g[1] == "-t":
	print("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/ASCII-Table-wide.svg/2560px-ASCII-Table-wide.svg.png")
