import nltk
from nltk.corpus import wordnet as wn
import itertools
import random
import enchant

#Writing a poem is easy by Alex Fig

#First choose a theme, nothing too long. Too pretenious.
tooLong = True
while tooLong:
    w = raw_input("Choose your theme: ")
    if len(w)<=9:
        tooLong = False

words = []
d = enchant.Dict("en_US")

#Find your words, this may take a bit.
for i in range(0,len(w)+1):
    combinations = list(itertools.combinations(w,i))
    for j in range(0,len(combinations)):
        currentWord = "".join(combinations[j])
        permutations = list(itertools.permutations(currentWord, len(currentWord)))
        for k in range(0,len(permutations)):
            possibleWord = "".join(permutations[k])
            if (possibleWord.find('a')!= -1 or possibleWord.find('e')!=-1 or possibleWord.find('i')!=-1 or possibleWord.find('o')!=-1 or possibleWord.find('u')!=-1 or possibleWord.find('y')!=-1):
                if d.check(possibleWord):
                    words.append(possibleWord)

#Now choose your words, carefully.
poem = words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+"\n"+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+"\n"+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+"\n"+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+"\n"+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+" "+words[random.randint(0,len(words)-1)]+"\n"+words[random.randint(0,len(words)-1)]

#Voila, it's complete.
print(poem)
