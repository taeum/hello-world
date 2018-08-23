import matplotlib.pyplot as plt

import collections
import operator



text = "My very photogenic mother died in a freak accident picnic, lightning when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know \ " \
       "those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges"

#print(text)

for char in '-.,;:)(\n':
    text = text.replace(char,' ')

text = text.lower()

#print(text)
word_list= text.split()

print(word_list)
#init dictionary

d={}
for word in word_list:
    d[word] = d.get(word,0) +1

print(d)

#https://stackoverflow.com/questions/16010869/python-plot-a-bar-using-matplotlib-using-a-dictionary
#plot graph
plt.bar(range(len(d)), list(d.values()), align='center')
plt.xticks(range(len(d)), list(d.keys()))
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x


#plot the graph
#plt.show()

#sort dic
od = collections.OrderedDict(sorted( d.items() , key = operator.itemgetter(1),reverse = True) )

print(od)
