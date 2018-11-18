import re

pattern = re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$")
email = re.compile("[\w\.-]+@[\w\.]+")
date = re.compile("\d{2} \w{3} \d{4}")
with open("input.txt") as f:
    data = f.read()

print(pattern.findall(data))
print(email.findall(data))
print(date.findall(data))