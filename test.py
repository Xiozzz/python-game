lettre = ["c",  'd', "e", "f", "g", "h", 'i']
liste = []

c = 1

# for i in lettre:
# 	while c < 8:
# 		liste.append("'"+ i+ str(c)+"'"+ " : 'card"+str(c)+"',")
# 		c+=1
# 	c = 1

# for i in liste:
# 	print(i, end=" ")

liste2 = []

for i in lettre:
	while c < 8:
		liste2.append("'card"+str(c)+"':[1],")
		c+=1
	c = 1

for i in liste2:
	print(i, end=" ")