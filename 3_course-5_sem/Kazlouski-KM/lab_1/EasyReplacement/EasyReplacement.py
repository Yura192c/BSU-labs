from interface.interface import Cipher


# Съешь же ещё этих мягких французских булок да выпей чаю.
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.


class EasyReplacement(Cipher):
    def __init__(self, key, text, alphabet):
        self.text = text
        self.alphabet = alphabet
        self.key = key.upper()
        self._validate_key()
        # super().__init__()  # Вызов конструктора родительского класса
        # if not isinstance(self.key, int):
        #     raise ValueError('Key must be an integer')

    def _validate_key(self):
        if len(self.key) != len(self.alphabet) or not all(char in self.alphabet for char in self.key):
            raise ValueError("Key must be a permutation of the alphabet")

    def cipher(self):
        text = self.text.upper()
        encrypted_text = ''
        for char in text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                encrypted_char = self.key[char_index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decipher(self):
        ciphertext = self.text.upper()
        decrypted_text = ''
        for char in ciphertext:
            if char in self.alphabet:
                char_index = self.key.index(char)
                decrypted_char = self.alphabet[char_index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
