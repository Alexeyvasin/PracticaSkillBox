import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

res = re.findall(r'\b[aeiouAEIOU]\w*', text)
print(res)
