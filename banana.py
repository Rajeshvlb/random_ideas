n = input("string: ").upper()
print(n)
v_s = 'AEIOU'
j = []
l = []
for i in n:
	if i in v_s:
		k = n.index(i)
		while k < len(n):
			j.append(n[n.index(i):k+1])
			k += 1
		n = n[n.index(i)+1:]
	else:
		k = n.index(i)
		while k < len(n):
			l.append(n[n.index(i):k+1])
			k += 1
		n = n[n.index(i)+1:]
print(j)
print(l)
