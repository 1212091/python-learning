import collections
from collections import defaultdict

input_data = raw_input()

word_dict = defaultdict(int)

for word in input_data.split(" "):
    word_dict[word] += 1

word_dict_ordered = collections.OrderedDict(sorted(word_dict.items()))

for key, value in word_dict_ordered.items():
    print(str(key) + ":" + str(value))
