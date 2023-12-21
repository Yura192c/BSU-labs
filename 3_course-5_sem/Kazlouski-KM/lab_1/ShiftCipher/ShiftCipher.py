from interface.interface import Cipher


# Съешь же ещё этих мягких французских булок да выпей чаю.
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.


class ShiftCipher(Cipher):
    def __init__(self, key, text: str, alphabet):
        self.text = text.upper()
        self.alphabet = alphabet.rstrip()
        self.key = self.alphabet.index(key)
        # super().__init__()  # Вызов конструктора родительского класса
        # if not isinstance(self.key, int):
        #     raise ValueError('Key must be an integer')

    def cipher(self):
        res = ''
        for letter in self.text:
            if letter == ' ':
                res += " "
                continue
            if letter == '.':
                res += "."
                continue
            index = self.alphabet.index(letter)
            if index + self.key >= len(self.alphabet):
                index = index - len(self.alphabet)
            res += self.alphabet[index + self.key]
        return res

    def decipher(self):
        res = ''
        for letter in self.text:
            if letter == ' ':
                res += " "
                continue
            if letter == '.':
                res += "."
                continue
            index = self.alphabet.index(letter)
            if index + 3 >= len(self.alphabet):
                index = index - len(self.alphabet)
            res += self.alphabet[index - self.key]
        return res