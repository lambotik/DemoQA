import re

position = ['position: relative; left: 31px; top: 0px;'][0].split(';')
left = position[1]
top = position[2]
l = re.findall(r'\d+', left)
t = re.findall(r'\d+', top)
le = [int(i) for i in l][0]
to = [int(i) for i in t][0]
print(le)
print(to)

