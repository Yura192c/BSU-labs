from interface.interface import Cipher


def pad_word_to_key_length(text, key):
    word_length = len(text)
    key_length = len(key)

    # Вычисляем остаток от деления длины слова на длину ключа
    remainder = word_length % key_length

    # Если остаток не равен нулю, дополняем слово пробелами
    if remainder != 0:
        padding_length = key_length - remainder
        text += ' ' * padding_length

    return text


class CipherReplacement(Cipher):
    def __init__(self, key, text, alphabet: str):
        self.text = text
        self.alphabet = alphabet
        self.key = key
        # super().__init__()  # Вызов конструктора родительского класса
        # if not isinstance(self.key, int):
        #     raise ValueError('Key must be an integer')
        self._generate_indexes()

    def _generate_indexes(self):
        indexes = [self.alphabet.index(char) for char in self.key]
        sorted_indexes = sorted(range(len(indexes)), key=lambda i: indexes[i])

        # Создаем новый список с номерами по величине
        ranked_indexes = [0] * len(indexes)
        for i, idx in enumerate(sorted_indexes):
            ranked_indexes[idx] = i + 1
        self.code_indexes = ranked_indexes
        self.decode_indexes = [ranked_indexes.index(i) + 1 for i in range(1, len(ranked_indexes) + 1)]

    def _operation(self, mode: str):
        if mode == 'decode':
            indexes = self.decode_indexes
        elif mode == 'code':
            indexes = self.code_indexes
            self.text = pad_word_to_key_length(text=self.text, key=self.key)
        encrypted_text = ''

        split_words = [self.text[i:i + len(self.key)] for i in range(0, len(self.text), len(self.key))]
        for word in split_words:
            for i, char in enumerate(word, start=0):
                encrypted_text = encrypted_text + word[indexes[i] - 1]
        return encrypted_text

    def cipher(self):
        return self._operation(mode='code')

    def decipher(self):
        return self._operation(mode='decode')
