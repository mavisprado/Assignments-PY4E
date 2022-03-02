fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    rd = line.strip()
    div = line.split()
    elements = lst.append(div)

lst.sort()

print(lst)
