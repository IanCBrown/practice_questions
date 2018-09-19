
import sys

vowels = ['a','e','i','o','u']

word = input("Input a word to reverse the vowels: \n")
if len(word) == 0 or len(word) == 1:
    print("{} is not long enough to be reversed".format(word))
    sys.exit()

wordToList = list(word)

reversedVowels = []
indexes = []

x = 0
for i in wordToList:
    if i == 'a':
        reversedVowels.append('u')
        indexes.append(x)
    if i == 'e':
        reversedVowels.append('o')
        indexes.append(x)
    if i == 'i':
        reversedVowels.append('y')
        indexes.append(x)
    if i == 'o':
        reversedVowels.append('e')
        indexes.append(x)
    if i == 'u':
        reversedVowels.append('a')
        indexes.append(x)
    x += 1

if len(indexes) >= 1:
    for (index, reversedVowel) in zip(indexes, reversedVowels):
        wordToList[index] = reversedVowel

print(''.join(wordToList))
