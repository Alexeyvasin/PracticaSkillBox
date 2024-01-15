import re

tongue_twister = ('How much wood would a woodchuck chuck if a woodchuck could chuck wood?')

print(re.match('wo', tongue_twister))
res = (re.search('wo', tongue_twister))
print(res.group())
print(res.start())
print(res.end())
results = re.findall('wo', tongue_twister)
print(results)
new_string = re.sub('wo', 'ЗАМЕНА', tongue_twister)
print(new_string)
