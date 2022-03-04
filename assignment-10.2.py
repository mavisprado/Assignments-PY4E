name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for iv in handle:
    if iv.startswith('From '):
        findhrs = iv.find(":")
        hrs = iv[findhrs-2 : findhrs]
        count[hrs] = count.get(hrs, 0 ) + 1

lst = list()
for k, v in count.items():
        tppl = (k,v)
        lst.append(tppl)

lst = sorted(lst)

for v, k in lst:
        print(v, k)
