import math
with open('two_cities_ascii.txt', 'r') as f:
	text = f.read()
length = len(text)
done = []
characters = 0
while characters < length:
  s = 0
  c = text[characters]
  for i in range(length):
	  character = text[i]
	  ascii_number = ord(character)
	  if (ascii_number % 2 != 0 and character == c):
		  s = s + 1
  popularity = math.trunc(s/length*100)
  star = "*"
  n = ord(c)
  if (n%2!=0 and ((n > 64 and n < 90) or (n > 96 and n < 122))): #check for english letters
	  if not c in done:
		  print( c,":", popularity*star)
		  done.append(c) 
  characters += 1	
f.close()
