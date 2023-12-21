from Affine.Affine import Affine, mod_inverse
import unittest
import random


class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'ВД'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        text = 'ПРИВЕТ'
        cipher = Affine(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        # self.assertAlmostEqual)
        self.assertEqual(cipher.cipher(), 'гехзни')

    def test_decipher(self):
        key = 'ВД'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        text = 'гехзни'
        cipher = Affine(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(cipher.decipher(), 'ПРИВЕТ')

    def test_dynamic_test(self):
        deafult_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        # Преобразуем строку в список символов
        alphabet_list = list(deafult_alphabet)
        # Перемешиваем символы случайным образом
        random.shuffle(alphabet_list)
        # Преобразуем список обратно в строку
        shuffled_alphabet = ''.join(alphabet_list)
        key = ''.join(random.choices(shuffled_alphabet, k=2))
        # print(key)
        text_length = 20  # Задайте желаемую длину текста
        text = ''.join(random.choices(shuffled_alphabet, k=text_length))

        a, b = shuffled_alphabet.index(key[0]), shuffled_alphabet.index(key[1])

        affine_cipher = Affine(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = affine_cipher.cipher()
        affine_cipher.text = cipher
        # if mod_inverse(a, len(shuffled_alphabet)) is None:
        #     with self.assertRaises(ValueError) as context:
        #         affine_cipher.decipher()
        #     self.assertEqual(str(context.exception), 'Невозможно выполнить дешифрование с заданными ключами.')
        # else:
        decipher = affine_cipher.decipher()

        self.assertEqual(decipher, text)

    def test_mod_inverse_valid(self):
        # Тестирование валидного случая, когда обратное число существует
        a = 3
        m = 11
        result = mod_inverse(a, m)
        self.assertEqual(result, 4)

    def test_mod_inverse_invalid(self):
        # Тестирование случая, когда обратное число не существует
        a = 4
        m = 8
        result = mod_inverse(a, m)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
