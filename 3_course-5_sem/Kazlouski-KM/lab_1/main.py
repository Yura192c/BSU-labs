# from interface.interface import Cipher
from ShiftCipher.ShiftCipher import ShiftCipher
from Affine.Affine import Affine
from EasyReplacement.EasyReplacement import EasyReplacement
from VigenereCipher.VigenereCipher import VigenereCipher
from CipherReplacements.CipherReplacements import CipherReplacement
from HillCipher.HillCipher import HillCipher

if __name__ == '__main__':
    data = {
        1: "Шифр сдвига",
        2: "Аффийный шифр",
        3: "Шифр простой замены",
        4: "Шифр Хилла",
        5: "Шифр перестановки",
        6: "Шифр Виженера",
    }
    for key, value in data.items():
        print(key, value)
    n = int(input("Выберете метод шифрования:\n"))
    d = int(input("1 Шифровка \n2 Дешифровка\n"))
    with open("alphabet.txt", "r") as alphabet:
        alphabet = alphabet.read()
        print(f'Alphabet: {alphabet}/ type: {type(alphabet)}')
    with open("input.txt", "r") as text:
        text = text.read()
        print(f'Text: {text}/ type: {type(text)}')
    with open("key.txt", "r") as key:
        key = key.read()
        # if not isinstance(key, int):
        #     raise ValueError('Key must be an integer')
        print(f'Key: {key}/ type: {type(key)}')

    match n:
        case 1:
            cipher = ShiftCipher(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
        case 2:
            cipher = Affine(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
        case 3:
            cipher = EasyReplacement(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
        case 4:
            cipher = HillCipher(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
        case 5:
            cipher = CipherReplacement(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
        case 6:
            cipher = VigenereCipher(key=key, text=text, alphabet=alphabet)
            match d:
                case 1:
                    print(cipher.cipher())
                case 2:
                    print(cipher.decipher())
