import sys
import re

# Inspired by Tom Scott's video about this same problem
# Problem: Find the largest, valid english word that can be written on a 7 segment display

# letters that cannot neatly fit on a 7 segment display 
bad_letters = re.compile('[gkmqvwxzio]')

def find_longest_word(wordlist):
    longest_valid_word = ""
    for word in wordlist:
        if (re.match('[gkmqvwxzio]', word)):
            continue
        elif len(word) >= len(longest_valid_word):
            print(word)
            longest_valid_word = word            
    return longest_valid_word

        

if __name__ == "__main__":
    wordlist = [] 
    wordlist = [str(x) for x in sys.stdin.readlines()] 

    print(find_longest_word(wordlist))
