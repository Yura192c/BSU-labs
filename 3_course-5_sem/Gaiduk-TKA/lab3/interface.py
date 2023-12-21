from abc import ABC, abstractmethod


class FiniteAutomatInterface(ABC):
    def __init__(self, state, input_alphabet, output_alphabet, transitions, initial_state):
        self.state = state
        self.input_alphabet = input_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.output_alphabet = output_alphabet

    @abstractmethod
    def run(self, input_string):
        pass

    @abstractmethod
    def is_correct(self):
        pass
