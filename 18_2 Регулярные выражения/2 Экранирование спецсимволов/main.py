import re
tongue_twister = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
print(re.findall(r'\\wwood\+\?,', tongue_twister))
