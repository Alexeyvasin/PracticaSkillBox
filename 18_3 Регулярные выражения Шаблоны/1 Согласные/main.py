import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

res = re.findall(r'\b[aeuoiAEUOI]\w*', text)
print(res)
res = re.findall(r'\b[^ ,.aeuoiAEUOI]\w*', text)
print(res)
