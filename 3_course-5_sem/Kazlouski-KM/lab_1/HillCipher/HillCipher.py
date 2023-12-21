import math

from interface.interface import Cipher


# Съешь же ещё этих мягких французских булок да выпей чаю.
# Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн жг еютзм ъгб.


class HillCipher(Cipher):
    def __init__(self, key, text, alphabet):
        self.text = text
        self.alphabet = alphabet
        self.key = key.upper()
        self._validate_key()
        # super().__init__()  # Вызов конструктора родительского класса
        # if not isinstance(self.key, int):
        #     raise ValueError('Key must be an integer')

    def _validate_key(self):
        if len(self.key) != 4:
            raise ValueError("Длина ключа не равна 4")

    def _correct_text(self):
        if len(self.text) % 2 != 0:
            self.text += str(self.alphabet[0])

    def _correct_det(self, det):
        if det == 0:
            raise ValueError("Определитель матрицы должен быть не равен нулю по модулю m")
        if math.gcd(det, len(self.alphabet)) != 1:
            raise ValueError("Определитель и m не взаимно простые")

    def _get_det(self, h_key: list[list]):
        # h_key = [
        #     [self.alphabet.index(self.key[0]), self.alphabet.index(self.key[1])],
        #     [self.alphabet.index(self.key[2]), self.alphabet.index(self.key[3])],
        # ]
        det = (h_key[0][0] * h_key[1][1] - h_key[0][1] * h_key[1][0]) % len(self.alphabet)
        self._correct_det(det=det)
        return det

    def _generate_result(self, repeat, h_key: list[list]):
        result = ''
        for i in range(repeat):
            temp = [self.alphabet.index(self.text[i * 2]), self.alphabet.index(self.text[1 + i * 2])]
            result += self.alphabet[(temp[0] * h_key[0][0] + temp[1] * h_key[1][0]) % len(self.alphabet)]
            result += self.alphabet[(temp[0] * h_key[0][1] + temp[1] * h_key[1][1]) % len(self.alphabet)]
        return result

    def cipher(self):
        repeat = len(self.text) // 2
        result = ''
        h_key = [
            [self.alphabet.index(self.key[0]), self.alphabet.index(self.key[1])],
            [self.alphabet.index(self.key[2]), self.alphabet.index(self.key[3])],
        ]

        self._get_det(h_key=h_key)
        return self._generate_result(repeat=repeat, h_key=h_key)
        # for i in range(repeat):
        #     temp = [self.alphabet.index(self.text[i * 2]), self.alphabet.index(self.text[1 + i * 2])]
        #     result += self.alphabet[(temp[0] * h_key[0][0] + temp[1] * h_key[1][0]) % len(self.alphabet)]
        #     result += self.alphabet[(temp[0] * h_key[0][1] + temp[1] * h_key[1][1]) % len(self.alphabet)]
        # return result

    def decipher(self):
        repeat = len(self.text) // 2
        result = ''

        hil_key = [
            [self.alphabet.index(self.key[3]), -self.alphabet.index(self.key[1])],
            [-self.alphabet.index(self.key[2]), self.alphabet.index(self.key[0])]
        ]

        det = self._get_det(h_key=hil_key)
        sp = {(i * det) % len(self.alphabet): i for i in range(len(self.alphabet))}
        const = sp[1]
        hil_key[0][0] = (hil_key[0][0] * const) % len(self.alphabet)
        hil_key[0][1] = (hil_key[0][1] * const) % len(self.alphabet)
        hil_key[1][0] = (hil_key[1][0] * const) % len(self.alphabet)
        hil_key[1][1] = (hil_key[1][1] * const) % len(self.alphabet)
        return self._generate_result(repeat=repeat, h_key=hil_key)
        # for i in range(repeat):
        #     temp = [self.alphabet.index(self.text[i * 2]), self.alphabet.index(self.text[1 + i * 2])]
        #     result += self.alphabet[(temp[0] * hil_key[0][0] + temp[1] * hil_key[1][0]) % len(self.alphabet)]
        #     result += self.alphabet[(temp[0] * hil_key[0][1] + temp[1] * hil_key[1][1]) % len(self.alphabet)]
        # return result
