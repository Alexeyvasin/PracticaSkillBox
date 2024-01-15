import re

tongue_twister = ('How much wood would a woodchuck chuck if a woodchuck could chuck wood?')

print(re.match(r'wo', tongue_twister))
res = (re.search(r'wo', tongue_twister))
print(res.group())
print(res.start())
print(res.end())
results = re.findall(r'wo', tongue_twister)
print(results)
new_string = re.sub(r'wo', 'ЗАМЕНА', tongue_twister)
print(new_string)
