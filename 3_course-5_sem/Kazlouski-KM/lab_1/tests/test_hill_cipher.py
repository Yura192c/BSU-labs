from HillCipher.HillCipher import HillCipher
import unittest
import random

class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'МАСВ'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        text = 'УТКОКРОКОДИЛ'
        shift_cipher = HillCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.cipher(), 'ЗЕРЭУБЭХГЗГЧ')

    def test_decipher(self):
        key = 'МАСВ'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        text = 'ЗЕРЭУБЭХГЗГЧ'
        shift_cipher = HillCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.decipher(), 'УТКОКРОКОДИЛ')

    def test_dynamic(self):
        deafult_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        # Преобразуем строку в список символов
        alphabet_list = list(deafult_alphabet)
        # Перемешиваем символы случайным образом
        random.shuffle(alphabet_list)
        # Преобразуем список обратно в строку
        shuffled_alphabet = ''.join(alphabet_list)
        key = ''.join(random.choices(shuffled_alphabet, k=4))
        text_length = 20  # Задайте желаемую длину текста
        text = ''.join(random.choices(shuffled_alphabet, k=text_length))

        hill_cipher = HillCipher(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = hill_cipher.cipher()
        hill_cipher.text = cipher
        decipher = hill_cipher.decipher()
        self.assertEqual(decipher, text)


if __name__ == "__main__":
    unittest.main()
