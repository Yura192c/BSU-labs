from ShiftCipher.ShiftCipher import ShiftCipher
import unittest
import random


class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'Г'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'Съешь же ещё этих мягких французских булок да выпей чаю.'
        shift_cipher = ShiftCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.cipher(), 'ФЭЗЫЯ ЙЗ ЗЬИ АХЛШ ПВЁНЛШ ЧУГРЩЦКФНЛШ ДЦОСН ЖГ ЕЮТЗМ ЪГБ.')

    def test_decipher(self):
        key = 'Г'
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'ФЭЗЫЯ ЙЗ ЗЬИ АХЛШ ПВЁНЛШ ЧУГРЩЦКФНЛШ ДЦОСН ЖГ ЕЮТЗМ ЪГБ.'
        shift_cipher = ShiftCipher(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.decipher(), 'СЪЕШЬ ЖЕ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК ДА ВЫПЕЙ ЧАЮ.')

    def test_dynamic_test(self):
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

        shift_cipher = ShiftCipher(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = shift_cipher.cipher()
        shift_cipher.text = cipher
        decipher = shift_cipher.decipher()
        self.assertEqual(decipher, text)


if __name__ == "__main__":
    unittest.main()
