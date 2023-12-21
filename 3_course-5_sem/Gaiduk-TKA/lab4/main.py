class FindEqualStates:
    def __init__(self, alphabet, transitions):
        self.alphabet = alphabet
        self.transitions = transitions

    def find_equal_states(self):
        step = []
        k = {}
        new_k = {}
        answer = []
        for a in self.transitions:
            step.append([a, self.transitions[a][1] + '_' + self.transitions[a][3] + ' '])
        for t in step:
            if t[1] in k:
                k[t[1]].append(t[0])
            else:
                k[t[1]] = [t[0]]
        while True:
            new_k = {}
            for a in self.transitions:
                a1, a2 = self.transitions[a][0], self.transitions[a][2]
                b1, b2 = '', ''
                counter = -1
                for i in k:
                    counter += 1
                    for ii in k[i]:
                        if a1 == ii:
                            b1 = str(counter)
                        if a2 == ii:
                            b2 = str(counter)
                for i in step:
                    if i[0] == a:
                        i[1] += b1 + '_' + b2 + ' '
            for t in step:
                if t[1] in new_k:
                    new_k[t[1]].append(t[0])
                else:
                    new_k[t[1]] = [t[0]]
            if list(k.values()) == list(new_k.values()):
                break
            k = new_k
        for i in new_k:
            if len(new_k[i]) > 1:
                answer.append(new_k[i])
        return new_k, answer


def find_min_word(state1, state2, table):
    line1 = table[state1]
    line2 = table[state2]


alphabet = ['0', '1']
transitions = {
    'q0': ['q2', '1', 'q12', '0'],
    'q1': ['q7', '0', 'q1', '1'],
    'q2': ['q14', '0', 'q4', '1'],
    'q3': ['q6', '0', 'q7', '0'],
    'q4': ['q6', '0', 'q4', '1'],
    'q5': ['q7', '0', 'q5', '1'],
    'q6': ['q5', '0', 'q14', '1'],
    'q7': ['q14', '0', 'q5', '1'],
    'q8': ['q14', '0', 'q4', '1'],
    'q9': ['q10', '1', 'q6', '0'],
    'q10': ['q6', '0', 'q8', '0'],
    'q11': ['q13', '0', 'q5', '0'],
    'q12': ['q10', '0', 'q5', '1'],
    'q13': ['q13', '1', 'q11', '1'],
    'q14': ['q11', '0', 'q0', '1'],
    'q15': ['q1', '1', 'q8', '0']
}

e_states_1 = FindEqualStates(alphabet, transitions)
info, s = e_states_1.find_equal_states()
print('Equal states: ')
for i in s:
    print(i)
for i in info:
    print(i)

# s1 = input("q1")
# s2 = input("q2")

# r = find_min_word("q1", 'q4', info)
