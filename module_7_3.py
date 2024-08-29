import string


class WordsFinder:
    file_names = []
    __PUNCT = set(string.punctuation)

    def __init__(self, *args):
        self.file_names.extend(args)

    def get_all_words(self):
        all_words = {}
        for el in self.file_names:
            with open(el, encoding='utf-8') as file:
                file_line = ' '.join(file.read().splitlines())
            file_line = ''.join(ch for ch in file_line if ch not in self.__PUNCT).lower().split()
            all_words[el] = file_line
        return all_words

    def upd_word(self, word):
        word = ''.join(ch for ch in word if ch not in self.__PUNCT).lower()
        return word

    def find(self, word):
        word = self.upd_word(word)
        for key, value in self.get_all_words().items():
            if word in value:
                i = value.index(word) + 1
                return {key: i}

    def count(self, word):
        word = self.upd_word(word)
        for key, value in self.get_all_words().items():
            if word in value:
                count_ = value.count(word)
                return {key: count_}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.find('It`s'))
print(finder2.count('teXT'))
