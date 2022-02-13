"""
References
http://sonorouschocolate.com/notes/index.php?title=The_best_strategies_for_Wordle

wordle_tree.txt obtained from
http://sonorouschocolate.com/notes/images/c/c4/Optimaltree.normalmode.txt
"""
PATTERN_CODE = '012'


def build_tree(text_file_path='wordle_tree.txt', pattern_code=PATTERN_CODE):
    """:return 'salet', dict_tree"""

    def pattern_replace(string):
        result = list(string)
        for i, c in enumerate(string):
            if c in 'BYG':
                result[i] = pattern_code['BYG'.find(c)]
        return ''.join(result)

    shape = 2315, 5
    data = [[''] * shape[1] for _ in range(shape[0])]
    with open(text_file_path) as text_file:
        for _i, line in enumerate(text_file.readlines()):
            line = [line[i + 6:i + 19] for i in range(0, len(line) - 6, 13)]
            for _j, _s in enumerate(line):
                data[_i][_j] = pattern_replace(_s.strip())

    # print(*data, sep='\n')
    # exit()
    all_correct = pattern_replace('GGGGG')

    def build(level, start, end):
        # data[start: end][level] are the children
        result = {}
        children_rows = [row for row in range(start, end) if data[row][level]]
        children_rows.append(end)
        for child_start, child_end in zip(children_rows[:-1], children_rows[1:]):
            child_info = data[child_start][level]
            child_pattern, child_word = child_info[:5], child_info[7:]
            if child_word:
                if child_pattern == all_correct:
                    child_subtree = {}
                else:
                    child_subtree = build(level + 1, child_start, child_end)
                result[child_pattern] = child_word, child_subtree
        return result

    return 'salet', build(0, 0, shape[0])


def solve():
    guess, solver = build_tree()
    while True:
        pattern = input(guess + '\n').strip()
        try:
            guess, solver = solver[pattern]
        except KeyError:
            print("KeyError!")


if __name__ == '__main__':
    solve()
