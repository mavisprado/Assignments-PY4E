name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

sender = dict()
bigcount = None
mostword = None

for i in handle:
    if i.startswith('From '):
        lst = i.split()
        for m in lst:
            mails = lst[1]
            mlist = []
            mlist.append(mails)
        for ms in mlist:
            sender[ms] = sender.get(ms, 0) + 1

for ml,count in sender.items():
        if bigcount is None or count > bigcount:
            mostword = ml
            bigcount = count

print(mostword, bigcount)
