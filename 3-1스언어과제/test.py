#6번문제 13.1
filename = "test.txt"
f = open(filename)
line = f.read()
f.close()
flist = line.split()
fhang = line.split('\n')
print("단어",len(flist))
print("문자:",len(line))
print("행:",len(fhang))