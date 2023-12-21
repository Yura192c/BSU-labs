from collections import defaultdict


class DiagnosticTreeNode:
    def __init__(self, states, letter=None, has_child=None):
        # self.parent = parent
        self.letter = letter

        self.states = states
        self.children = []
        self.has_child: bool = has_child

    def __str__(self):
        return f'{self.states}xxx{self.children}'


def build_leaves(states, transitions):
    pass


def build_diagnostic_tree(states, alphabet, transitions):
    root = DiagnosticTreeNode(set(states))
    # stack = [root]

    for letter in alphabet:
        node, status = group_by_second_element(states, letter)
        three_node = DiagnosticTreeNode(node, letter=letter, has_child=status)
        pass
        # while stack:
        #     current_node = stack.pop()
        #
        #     for symbol in alphabet:
        #         next_states = set()
        #         for state in current_node.states:
        #             next_states.update(transitions[state][symbol])
        #
        #         grouped_states = group_states_by_output(next_states, outputs)
        #
        #         for output, group in grouped_states.items():
        #             if group not in current_node.children:
        #                 child_node = DiagnosticTreeNode(group)
        #                 current_node.children[group] = (symbol, child_node)
        #                 stack.append(child_node)
        #
        # set_terminal_nodes(root, outputs)
        # diagnostic_experiments = find_diagnostic_experiments(root, alphabet)
        # return diagnostic_experiments




def group_by_second_element(dictionary, key):
    """
    Группировка состояний и проверка на дубликаты
    """

    grouped_dict = defaultdict(list)
    for k, v in dictionary.items():
        grouped_dict[v[key][1]].append(v[key][0])

    result_groups = [group for group in grouped_dict.values() if len(group) > 1]

    # Проверка наличия повторяющихся элементов в группах
    has_duplicates = any(len(set(group)) != len(group) for group in result_groups)

    return result_groups, not has_duplicates


def split_groups(transitions, groups, action):
    """ Остальные слои после 2"""
    new_groups = []

    for group in groups:
        subgroups = []
        elements_by_value = defaultdict(list)

        # Группировка элементов по значениям в transitions[action]
        for element in group:
            value, out = transitions[element][action][0], transitions[element][action][1]
            elements_by_value[out].append(value)

        # Разбиение группы на подгруппы по значениям в transitions[action]
        for subgroup in elements_by_value.values():
            subgroups.append(subgroup)

        new_groups.extend(subgroups)
    has_duplicates = any(len(set(group)) != len(group) for group in new_groups)
    is_final_root = all(len(state) == 1 for state in new_groups)

    return new_groups, has_duplicates, is_final_root


# Пример использования
states = [1, 2, 3, 4, 5]
alphabet = {'a', 'b', 'w'}
transitions = {
    1: {'a': [1, 0], 'b': [1, 1], 'w': [5, 0]},
    2: {'a': [3, 1], 'b': [2, 0], 'w': [4, 0]},
    3: {'a': [2, 1], 'b': [4, 1], 'w': [4, 0]},
    4: {'a': [5, 1], 'b': [1, 1], 'w': [5, 1]},
    5: {'a': [3, 0], 'b': [2, 0], 'w': [4, 1]},
}

# group, res = group_by_second_element(transitions, 'a')
# split_groups(transitions, [[1], [2], [3], [2, 3]], "b")
# # outputs = {0: 'X', 1: 'Y', 2: 'Y'}

diagnostic_tree = build_diagnostic_tree(states, alphabet, transitions)
print("Диагностические эксперименты:", diagnostic_tree)

"""
НЕ РЕАЛИЗОВАН ДО КОНЦА
ИННФА ТУТ:
https://intuit.ru/studies/courses/630/486/lecture/11018?page=3
"""