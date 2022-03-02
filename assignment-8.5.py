fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0

for line in fh:
    if line.startswith('From '):
        div = line.split()
        mail = div[1]
        print(mail)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
