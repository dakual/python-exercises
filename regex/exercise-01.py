import re

str = "Jessa salary is 8000$"

# compile regex pattern
str_pattern = "\d{3}"
rex_pattern = re.compile(str_pattern)

# findall
res = re.findall(r"\b\w+\b", str)
print("findall:", res)


# match regex pattern at start of the string
res = re.match(r"\w+", str)
print("match:", res.group())


# search regex pattern anywhere inside string
res = re.search(r"\d+", str)
print("search:",res.group())


# split regex pattern
res = re.split(r"\s", str)
print("split:", res)


# sub regex pattern for replacement
res = re.sub(r"\s", "-", str)
print("sub:", res)


# fullmatch regex pattern
res = re.fullmatch(r".{21}", str)
print("fullmatch:", res.group())


# finditer regex pattern
res = re.finditer(r"\d{2}", str)
for obj in res:
    print("finditer:", obj.group())


# subn regex pattern
result = re.subn(r"[a-z]{6}", "XXXXXX", str)
print("subn:", result)