# from collections import deque
#
# previous_lines = deque(maxlen=5)
# with open('text.txt') as f:
#     for line in f:
#         print(line)
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

    # Example use on a file

    with open('text.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
