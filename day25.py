#AoC Day 25 -- The Halting Problem
# !!!

import collections


file = """
Begin in state A.
Perform a diagnostic checksum after 12261543 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
""".strip().split('\n')


def main(file):
    tape = collections.defaultdict(bool)
    cursor = 0
    state = 'A'

    for _ in range(12261543):
        if state == 'A':
            if not tape[cursor]:
                tape[cursor] = True
                cursor += 1
                state = 'B'
            else:
                tape[cursor] = False
                cursor -= 1
                state = 'C'
        elif state == 'B':
            if not tape[cursor]:
                tape[cursor] = True
                cursor -= 1
                state = 'A'
            else:
                tape[cursor] = True
                cursor += 1
                state = 'C'
        elif state == 'C':
            if not tape[cursor]:
                tape[cursor] = True
                cursor += 1
                state = 'A'
            else:
                tape[cursor] = False
                cursor -= 1
                state = 'D'
        elif state == 'D':
            if not tape[cursor]:
                tape[cursor] = True
                cursor -= 1
                state = 'E'
            else:
                tape[cursor] = True
                cursor -= 1
                state = 'C'
        elif state == 'E':
            if not tape[cursor]:
                tape[cursor] = True
                cursor += 1
                state = 'F'
            else:
                tape[cursor] = True
                cursor += 1
                state = 'A'
        elif state == 'F':
            if not tape[cursor]:
                tape[cursor] = True
                cursor += 1
                state = 'A'
            else:
                cursor += 1
                state = 'E'
    return sum(tape.values())


print(main(file))