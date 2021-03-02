import json
def dict_depth(v):  
    counter = 0
    for i in v: 
        if i == "{" or i == "[": 
            counter += 1
    return(counter)
    
with open('just_a_dictionary.txt') as f: 
    data = f.read() 
    d = json.loads(data)
    ditems = len(d)
depth = 0
if ditems == 0:
	depth = 0 
else:
	depth = depth + 1
	for i in range(ditems):
		key, val = d.items()
		v = str(val)
		depth = depth + dict_depth(v)
print ("The depth of the dictionary is", depth)		 
		 
		 
f.close()
