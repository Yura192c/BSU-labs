from CipherReplacements.CipherReplacements import CipherReplacement
import unittest
import random


class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'ФЛОТ'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'МАНДАРИН'
        cipher = CipherReplacement(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        # self.assertAlmostEqual)
        self.assertEqual(cipher.cipher(), 'ДМАННАРИ')

    def test_decipher(self):
        key = 'ФЛОТ'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'ДМАННАРИ'
        cipher = CipherReplacement(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(cipher.decipher(), 'МАНДАРИН')

    def test_dynamic_test(self):
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

        replacements_cipher = CipherReplacement(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = replacements_cipher.cipher()
        replacements_cipher.text = cipher
        decipher = replacements_cipher.decipher()
        self.assertEqual(decipher, text)

if __name__ == "__main__":
    unittest.main()
