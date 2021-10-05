import re
s = "#1 @ 596,731: 11x27"

print(re.match(r".*@ (\d*),(\d*): (\d*)x(\d*)", s).groups())

print(re.compile(r".*@ (\d*),(\d*): (\d*)x(\d*)").split(s))

print(re.findall(r".*@ (\d*),.*", s))

a = "01234567"

a = a[:1]  + a[3:]
print(a)