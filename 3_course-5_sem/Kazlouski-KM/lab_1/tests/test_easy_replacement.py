from EasyReplacement.EasyReplacement import EasyReplacement
import unittest
import random


class TestShiftCipher(unittest.TestCase):
    def test_cipher(self):
        key = 'ЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГД '
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'Съешь же ещё этих мягких французских булок да выпей чаю.'
        shift_cipher = EasyReplacement(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.cipher(), 'ЦЯЙЭБ ЛЙ ЙЮК ВЧНЪ СДЗПНЪ ЩХЕТЫШМЦПНЪ ЁШРУП ИЕ ЖАФЙО ЬЕГ.')

    def test_decipher(self):
        key = 'ЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГД '
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        text = 'ЦЯЙЭБ ЛЙ ЙЮК ВЧНЪ СДЗПНЪ ЩХЕТЫШМЦПНЪ ЁШРУП ИЕ ЖАФЙО ЬЕГ.'
        shift_cipher = EasyReplacement(key=key, text=text, alphabet=alphabet)
        # ciphered_text = shift_cipher.decipher()
        self.assertEqual(shift_cipher.decipher(), 'СЪЕШЬ ЖЕ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК ДА ВЫПЕЙ ЧАЮ.')

    def test_dynamic(self):
        deafult_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
        # Преобразуем строку в список символов
        alphabet_list = list(deafult_alphabet)
        # Перемешиваем символы случайным образом
        random.shuffle(alphabet_list)
        # Преобразуем список обратно в строку
        shuffled_alphabet = ''.join(alphabet_list)
        key = ''.join(alphabet_list)
        text_length = 20  # Задайте желаемую длину текста
        text = ''.join(random.choices(shuffled_alphabet, k=text_length))

        easy_replacements_cipher = EasyReplacement(key=key, text=text, alphabet=shuffled_alphabet)
        cipher = easy_replacements_cipher.cipher()
        easy_replacements_cipher.text = cipher
        decipher = easy_replacements_cipher.decipher()
        self.assertEqual(decipher, text)

    def test__validate_key(self):
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

        with self.assertRaises(ValueError) as context:
            easy_replacements_cipher = EasyReplacement(key=key, text=text, alphabet=shuffled_alphabet)
        self.assertEqual(str(context.exception), 'Key must be a permutation of the alphabet')


if __name__ == "__main__":
    unittest.main()
