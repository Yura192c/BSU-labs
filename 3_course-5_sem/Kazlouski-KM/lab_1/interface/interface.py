from abc import ABC, abstractclassmethod


class Cipher(ABC):

    # @abstractclassmethod
    def __init__(self) -> None:
        pass
        # with open("alphabet.txt", "r") as alphabet:
        #     self.alphabet = alphabet.read()
        #     print(f'Alphabet: {self.alphabet}/ type: {type(self.alphabet)}')
        # with open("interface/input.txt", "r") as text:
        #     self.text = text.read()
        #     print(f'Text: {self.text}/ type: {type(self.text)}')
        # with open("interface/key.txt", "r") as key:
        #     self.key = self.alphabet.index(key.read())
        #     if not isinstance(self.key, int):
        #         raise ValueError('Key must be an integer')
        #     print(f'Key: {self.key}/ type: {type(self.key)}')

    @abstractclassmethod
    def decipher(self):
        pass

    @abstractclassmethod
    def cipher(self):
        pass
