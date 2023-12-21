from VigenereCipher.VigenereCipher import VigenereCipher
import unittest
import random


class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'кларнет'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'Карл у Клары украл кораллы'
        shift_cipher = VigenereCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.cipher(), 'ХЛРЬБПЮКЬЫДШХТЦЦОБНРЮЁ')

    def test_decipher(self):
        key = 'кларнет'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'ХЛРЬБПЮКЬЫДШХТЦЦОБНРЮЁ'
        cipher = VigenereCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(cipher.decipher(), 'КАРЛУКЛАРЫУКРАЛКОРАЛЛЫ')

    def test_dynamic(self):
        deafult_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        # Преобразуем строку в список символов
        alphabet_list = list(deafult_alphabet)
        # Перемешиваем символы случайным образом
        random.shuffle(alphabet_list)
        # Преобразуем список обратно в строку
        shuffled_alphabet = ''.join(alphabet_list)
        key = random.choice(shuffled_alphabet)
        text_length = 20  # Задайте желаемую длину текста
        text = ''.join(random.choices(shuffled_alphabet, k=text_length))

        vigenere_cipher = VigenereCipher(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = vigenere_cipher.cipher()
        vigenere_cipher.text = cipher
        decipher = vigenere_cipher.decipher()
        self.assertEqual(decipher, text.replace(' ', ''))


if __name__ == "__main__":
    unittest.main()
