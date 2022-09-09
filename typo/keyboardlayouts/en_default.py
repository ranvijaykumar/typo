import random

NEIGHBORINGLETTERS = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['r', 'd', 's', 'w'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['n', 'b', 'g', 'y', 'u', 'j'],
    'i': ['o', 'k', 'j', 'u'],
    'j': ['h', 'u', 'i', 'k', 'm', 'n'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],
    'q': ['a', 'w'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'z', 'x', 'd', 'e', 'w'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'd', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x'],
}

NEIGHBORINGNUMPADDIGITS = {
    '0': ['1', '2'],
    '1': ['4', '5', '2', '0'],
    '2': ['0', '1', '4', '5', '6', '3'],
    '3': ['2', '5', '6'],
    '4': ['7', '8', '5', '2', '1'],
    '5': ['7', '8', '9', '4', '6', '1', '2', '3'],
    '6': ['9', '8', '5', '2', '3'],
    '7': ['8', '5', '4'],
    '8': ['7', '4', '5', '6', '9'],
    '9': ['8', '5', '6']
}

VISUALLYSIMILARDIGITS = {
    '0': ['6', '8', '9'],
    '1': ['7'],
    '2': ['7'],
    '3': ['5', '8', '9'],
    '4': ['9'],
    '5': ['3', '8'],
    '6': ['0', '8'],
    '7': ['1', '2'],
    '8': ['0', '3', '5', '6'],
    '9': ['0', '3', '4']
}

VISUALLYSIMILARCHARS = {
    '0': ['6', '8', '9', 'o', 'D', 'O', 'U'],
    '1': ['7', 'I'],
    '2': ['7', 'Q', 'Z'],
    '3': ['5', '8', '9'],
    '4': ['9', 'U'],
    '5': ['3', '8', 'S'],
    '6': ['0', '8', 'b', 'G'],
    '7': ['1', '2', 'T', 'Z'],
    '8': ['0', '3', '5', '6', 'B', 'S'],
    '9': ['0', '3', '4', 'g', 'q'],
    'b': ['6'],
    'c': ['e'],
    'e': ['c'],
    'g': ['9', 'q'],
    'i': ['I'],
    'm': ['n'],
    'n': ['m', 'p'],
    'o': ['0'],
    'p': ['n'],
    'q': ['9', 'g'],
    'u': ['v'],
    'v': ['u'],
    'y': ['z'],
    'z': ['y'],
    'B': ['8', 'P'],
    'C': ['G'],
    'D': ['0', 'O'],
    'E': ['F'],
    'F': ['7', 'E', 'R'],
    'G': ['6', 'C'],
    'I': ['1', 'i', 'L', 'T'],
    'L': ['I'],
    'M': ['N'],
    'N': ['M'],
    'O': ['0', 'D', 'U'],
    'P': ['B'],
    'Q': ['2'],
    'S': ['5', '8'],
    'T': ['I', '7'],
    'U': ['0', '4', 'O', 'V'],
    'V': ['U', 'W'],
    'W': ['U'],
    'X': ['Y'],
    'Y': ['5', 'X'],
    'Z': ['2', '7']
}


# Data type classes, and capitalization are preserved.
def get_random_neighbor(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a neighbor")

    if char.isdecimal():
        numpad = random.choice([True, False])
        if numpad:
            return random.choice(NEIGHBORINGNUMPADDIGITS[char])
        else:
            if char == '0':
                return '9'
            elif char == '1':
                return '2'
            else:
                return str(int(char) + (-1) ** random.randint(0, 1))
    elif char.lower() in NEIGHBORINGLETTERS:
        neighbor = random.choice(NEIGHBORINGLETTERS[char.lower()])
        return neighbor.upper() if char.isupper() else neighbor
    else:
        return char


def get_random_visually_similar_char(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a visually similar character")

    if char in VISUALLYSIMILARCHARS:
        return random.choice((VISUALLYSIMILARCHARS[char]))
    else:
        return char


def get_random_visually_similar_digit(char, seed=None):
    if seed is not None:
        random.seed(seed)

    if len(char) != 1:
        raise Exception("Need exactly one character to find a visually similar digit")

    if char.isdigit():
        if char in VISUALLYSIMILARDIGITS:
            return random.choice((VISUALLYSIMILARDIGITS[char]))
        else:
            return char
    else:
        raise Exception("'" + char + "' is not a digit.")
