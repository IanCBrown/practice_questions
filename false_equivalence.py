#every letter in the alphabet has a number value starting at a = 1; 
#every words has some value equal to the sum of these letter values. 
#compare words for equality based on these sums. 


alphabet = {'a': 1,'b': 2, 'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,
                    'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}


def get_sum(word):
    sum = 0
    for letter in word:
        sum += (alphabet[letter])
    return sum

word1 = input("-->")
word2 = input("-->")

try:
    if get_sum(word1) == get_sum(word2):
        print(True)
    else:
        print(False)
except KeyError:
    print("No spaces or numbers")

