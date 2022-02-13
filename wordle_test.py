"""
wordle_list.txt obtained from
https://github.com/alex1770/wordle/blob/main/wordlist_hidden
"""
from wordle_solver import build_tree, PATTERN_CODE
from collections import Counter

WORDLE_LIST = 'wordle_list.txt'
CHEAT_CODE = '?'


class Wordle:
    def __init__(self, answer='', pattern_code=PATTERN_CODE):
        self.answer = answer
        self.pattern_code = pattern_code

    def guessing(self, guess):
        if len(guess) != 5:
            print("### len(guess) != 5 ###")
            return ''
        result = [self.pattern_code[0]] * 5
        ans_counter = Counter(self.answer)
        # First, scan for the correct characters
        for i, g in enumerate(guess):
            if g == self.answer[i]:
                result[i] = self.pattern_code[2]
                ans_counter[g] -= 1
                if not ans_counter[g]:
                    del ans_counter[g]
        # Second, scan the second time for labeling yellow
        for i, g in enumerate(guess):
            if g != self.answer[i] and g in ans_counter:
                result[i] = self.pattern_code[1]
                ans_counter[g] -= 1
                if not ans_counter[g]:
                    del ans_counter[g]
        return ''.join(result)

    def simulating(self, cheat_code=CHEAT_CODE):
        """
        :param cheat_code: if cheat_code, build_tree() before start guessing,
        you can type the cheat_code (default='?') to see the optimal guess
        """
        print("Answer:", self.answer)
        print("Start simulating...",
              (" (cheat code='%s')" % cheat_code if cheat_code else '')
              )
        if cheat_code:  # can cheating
            optimal_guess, tree = build_tree()
            guess = input().strip()

            while guess != self.answer:
                if guess == cheat_code:
                    pattern = "optimal_guess: %s" % optimal_guess
                else:
                    pattern = self.guessing(guess)
                    if pattern in tree:
                        optimal_guess, tree = tree[pattern]
                    else:
                        print("pattern not in tree!")
                guess = input(pattern + '\n').strip()

        else:  # cannot cheating
            guess = input().strip()
            while guess != self.answer:
                guess = input(self.guessing(guess) + '\n').strip()

        print("### Bingo! ###")


def get_tree_words(salet_and_tree):
    stack = [salet_and_tree]
    result = set()
    while stack:
        word, tree = stack.pop()
        result.add(word)
        stack.extend(tree.values())
    return result


def load_words(wordle_list=WORDLE_LIST):
    with open(wordle_list) as f:
        return [word.rstrip() for word in f.readlines()]


def test_word(salet_and_tree, answer):
    salet, tree = salet_and_tree
    wordle = Wordle()
    wordle.answer = answer
    pattern = wordle.guessing(salet)
    subtree = tree
    step = 1
    while pattern != PATTERN_CODE[2] * 5:
        step += 1
        if pattern not in subtree:
            return -step
        guess, subtree = subtree[pattern]
        pattern = wordle.guessing(guess)
    return step


def test_words(salet_and_tree, words):
    fail = 0
    for answer in words:
        test_code = test_word(salet_and_tree, answer)
        if test_code < 0:
            print(answer, test_code)
            fail += 1
    print("Fail num:", fail)


def main_test():
    salet_and_tree = build_tree()
    tree_words = get_tree_words(salet_and_tree)
    wordle_words = load_words()

    print("Failed tree's words:")
    test_words(salet_and_tree, tree_words)
    print()
    print("Failed Wordle's words:")
    assert not test_words(salet_and_tree, wordle_words)


def start_simulate(answer, pattern_code=PATTERN_CODE, cheat_code=CHEAT_CODE):
    Wordle(answer, pattern_code).simulating(cheat_code)


def demo():
    main_test()
    print()
    start_simulate('pygmy')
    print()
    start_simulate('pygmy', cheat_code='')


if __name__ == '__main__':
    # demo()
    start_simulate(input("Input answer: ").strip())
