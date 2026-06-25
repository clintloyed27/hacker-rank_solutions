import re

string = input()
k = input()

matches = list(re.finditer(r'(?={})'.format(re.escape(k)), string))

if matches:
    for m in matches:
        print((m.start(), m.start() + len(k) - 1))
else:
    print((-1, -1))