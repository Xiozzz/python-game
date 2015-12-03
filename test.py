import pickle
filename = "wordbank"
f = open(filename, 'wb')
pickle.dump(['chocolat', 'vanille'], f)
f.close()

f = open(filename, 'rb')
wordBank = pickle.load(f)
for x in wordBank:
	print(x)

f.close()