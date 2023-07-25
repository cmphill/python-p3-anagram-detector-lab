
class Anagram:
    def __init__(self, word):
        self.word = word
    def get_word(self):
        return self._word
    
    def set_word(self, word):
        self._word = word

    word = property(get_word, set_word)
    def match(self, anagrams):
        anagrams_list = []
        for anagram in anagrams:
            letter = []
            for alphabet in anagram:
                letter.extend(alphabet.split())
            sorted_anagram = (sorted(letter))
            sorted_word = (sorted(self.word))
            if sorted_anagram == sorted_word:
                anagrams_list.append(anagram)
        return anagrams_list


# if __name__ == "__main__":
#     anagrams = Anagrams("hello")
#     anagrams.match(["hello", "lime"])
