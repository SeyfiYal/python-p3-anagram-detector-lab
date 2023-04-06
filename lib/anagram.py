# your code goes here!

class Anagram():
    def __init__(self,word):
        self.word = word

    def match(self,word_list):
        anagrams = []
        sorted_word = sorted(self.word.lower())
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word and candidate != self.word:
                anagrams.append(candidate)
        return anagrams



listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])