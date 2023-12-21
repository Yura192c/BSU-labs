from interface.interface import Cipher


# Съешь же ещё этих мягких французских булок да выпей чаю.
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.


class VigenereCipher(Cipher):
    def __init__(self, key, text, alphabet):
        self.text = text.replace(" ", "").upper()
        self.alphabet = alphabet.rstrip()
        self.key = key
        # super().__init__()  # Вызов конструктора родительского класса
        # if not isinstance(self.key, int):
        #     raise ValueError('Key must be an integer')

    def cipher(self):
        encrypted_text = ''
        key_length = len(self.key)

        for i in range(len(self.text)):
            char = self.text[i]
            if char.isalpha():
                char = char.upper()
                is_upper = char.isupper()
                key_char = self.key[i % key_length].upper()

                # Определяем сдвиг для текущей буквы в тексте
                shift = self.alphabet.index(key_char)

                # Зашифровываем букву с учетом сдвига
                if char in self.alphabet:
                    char_index = self.alphabet.index(char)
                    encrypted_index = (char_index + shift) % len(self.alphabet)
                    encrypted_char = self.alphabet[encrypted_index]
                else:
                    encrypted_char = char

                if is_upper:
                    encrypted_text += encrypted_char
                else:
                    encrypted_text += encrypted_char.lower()
            else:
                encrypted_text += char

        return encrypted_text

    def decipher(self):
        decrypted_text = ''
        key_length = len(self.key)
        # alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

        for i in range(len(self.text)):
            char = self.text[i]
            if char.isalpha():
                char = char.upper()
                is_upper = char.isupper()
                key_char = self.key[i % key_length].upper()

                # Определяем сдвиг для текущей буквы в тексте
                shift = self.alphabet.index(key_char)

                # Расшифровываем букву с учетом сдвига
                if char in self.alphabet:
                    char_index = self.alphabet.index(char)
                    decrypted_index = (char_index - shift) % len(self.alphabet)
                    decrypted_char = self.alphabet[decrypted_index]
                else:
                    decrypted_char = char

                if is_upper:
                    decrypted_text += decrypted_char
                else:
                    decrypted_text += decrypted_char.lower()
            else:
                decrypted_text += char

        return decrypted_text

