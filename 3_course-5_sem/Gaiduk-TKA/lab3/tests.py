import unittest

from classes import Milli, FiniteAutomat


class TestFiniteAutomat(unittest.TestCase):

    def setUp(self) -> None:
        state_1 = ['q0', 'q1', 'q2', 'q3']
        input_alphabet_1 = ['0', '1']
        output_alphabet_1 = ['a', 'b']
        transitions_1 = {
            'q0': {'0': ('q2', 'a'), '1': ('q1', 'b')},
            'q1': {'0': ('q0', 'b'), '1': ('q2', 'a')},
            'q2': {'0': ('q3', 'a'), '1': ('q2', 'b')},
            'q3': {'0': ('q3', 'a'), '1': ('q3', 'a')},
        }
        initial_state_1 = 'q0'
        self.automat = FiniteAutomat(state_1, input_alphabet_1, output_alphabet_1, transitions_1, initial_state_1)

    def test_finite_automat_correct(self):
        self.assertTrue(self.automat.is_correct())

    def test_finite_automat_run(self):
        self.assertEqual(self.automat.run("1010110001"), "bababbaaab")


class TestAutomatMilli(unittest.TestCase):

    def setUp(self) -> None:
        states = ['S1', 'S2', 'S3']
        inputs = ['A', 'B']
        outputs = {
            'S1': {'A': 'O1', 'B': 'O2'},
            'S2': {'A': 'O2', 'B': 'O1'},
            'S3': {'A': 'O1', 'B': 'O1'}
        }
        transitions = {
            'S1': {'A': 'S1', 'B': 'S3'},
            'S2': {'A': 'S3', 'B': 'S1'},
            'S3': {'A': 'S1', 'B': 'S2'},
        }
        initial_state = 'S1'

        self.automat = Milli(states, inputs, outputs, transitions, initial_state)

    def test_finite_automat_correct(self):
        self.assertTrue(self.automat.is_correct())

    def test_finite_automat_run(self):
        self.assertEqual(self.automat.run("BABABBAA"), "O2O1O2O1O2O2O1O1")


if __name__ == "__main__":
    unittest.main()
