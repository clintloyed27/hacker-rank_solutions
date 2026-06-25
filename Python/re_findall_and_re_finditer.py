import re

s = input()

pattern = r'(?<=^|[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU]|$)'

matches = re.findall(pattern, s)

if matches:
    for m in matches:
        print(m)
else:
    print(-1)