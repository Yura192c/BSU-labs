from interface.interface import Cipher


def mod_inverse(a, m):
    # Находим обратное число a по модулю m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


class Affine(Cipher):
    def __init__(self, key, text, alphabet):
        # super().__init__()
        self.text = text
        self.alphabet = alphabet
        self.key = key
        self.a, self.b = self.alphabet.index(self.key[0]), self.alphabet.index(self.key[1])
        self.m = len(self.alphabet)

    def cipher(self):
        result = ''

        for char in self.text:
            if char.upper() in self.alphabet:
                is_upper = char.isupper()
                char = char.upper()

                index = self.alphabet.index(char)
                new_index = (self.a * index + self.b) % len(self.alphabet)
                new_char = self.alphabet[new_index]

                if is_upper:
                    new_char = new_char.lower()

                result += new_char
            else:
                result += char

        return result


    def decipher(self):
        result = ''

        a_inverse = mod_inverse(self.a, len(self.alphabet))
        if a_inverse is None:
            raise ValueError('Невозможно выполнить дешифрование с заданными ключами.')

        for char in self.text:
            if char.upper() in self.alphabet:
                is_upper = char.isupper()
                char = char.upper()

                index = self.alphabet.index(char)
                new_index = (a_inverse * (index - self.b)) % len(self.alphabet)
                new_char = self.alphabet[new_index]

                if is_upper:
                    new_char = new_char.lower()

                result += new_char
            else:
                result += char

        return result

