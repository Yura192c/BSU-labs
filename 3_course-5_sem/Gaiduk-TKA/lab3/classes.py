from interface import FiniteAutomatInterface


class FiniteAutomat(FiniteAutomatInterface):
    def run(self, input_string):
        current_state = self.initial_state
        answer = ''.join(self.transitions[current_state][input_symbol][1] for input_symbol in input_string)
        return answer

    def is_correct(self):
        return (
                all(len(set(item)) == len(item) for item in [self.state, self.input_alphabet, self.output_alphabet]) and
                self.initial_state in self.state and
                all(
                    all(new_s in self.state and out in self.output_alphabet for new_s, out in
                        self.transitions[st].values())
                    for st in self.state
                )
        )


class Milli(FiniteAutomatInterface):
    def run(self, input_string):
        current_state = self.initial_state
        answer = ''.join(self.output_alphabet[current_state][input_symbol] for input_symbol in input_string)
        return answer

    def is_correct(self):
        return (
                len(set(self.state)) == len(self.state) and
                len(set(self.input_alphabet)) == len(self.input_alphabet) and
                self.initial_state in self.state and
                all(self.transitions[s][i] in self.state for s in self.state for i in self.input_alphabet) and
                all(s in self.state and all(i in self.input_alphabet for i in self.output_alphabet[s]) for s in
                    self.output_alphabet) and
                all(s in self.state and all(i in self.input_alphabet for i in self.transitions[s]) for s in
                    self.transitions)
        )
