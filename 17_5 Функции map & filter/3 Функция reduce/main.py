from functools import reduce
from typing import List

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]

print(reduce(lambda a, b: a+1 if b == 'was' else a, ' '.join(sentences).split(), 0))
