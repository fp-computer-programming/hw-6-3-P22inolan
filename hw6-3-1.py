# Author: IBN (AMDG) 11/15/2021

word1 = list(input("Give me a word. "))
word2 = list(input("Give me another word. "))

(word1).sort()
(word2).sort()

if word1 == word2:
    print("The two words are anagrams.")
else:
    print("The two words are not anagrams.")
