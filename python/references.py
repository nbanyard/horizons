import re

VALID_RE = re.compile(r"^\s*[STNstn]\s*[A-Za-z]\s*(?:\d\s*\d\s*){2,5}$")
SPACES_RE = re.compile("\s*")

BIG_LETTERS = {
    'S': (0, 0),
    'N': (0, 5),
    'T': (5, 0),
    'O': (5, 5),
    'H': (0, 10)
}

SMALL_LETTERS = {
    'A': (0, 4),
    'B': (1, 4),
    'C': (2, 4),
    'D': (3, 4),
    'E': (4, 4),
    'F': (0, 3),
    'G': (1, 3),
    'H': (2, 3),
    'J': (3, 3),
    'K': (4, 3),
    'L': (0, 2),
    'M': (1, 2),
    'N': (2, 2),
    'O': (3, 2),
    'P': (4, 2),
    'Q': (0, 1),
    'R': (1, 1),
    'S': (2, 1),
    'T': (3, 1),
    'U': (4, 1),
    'V': (0, 0),
    'W': (1, 0),
    'X': (2, 0),
    'Y': (3, 0),
    'Z': (4, 0),
}

LETTERS_TO_NUMBERS = {bl + sl: (bn[0] + sn[0], bn[1] + sn[1])
                           for sl, sn in SMALL_LETTERS.items()
                           for bl, bn in BIG_LETTERS.items()}
NUMBERS_TO_LETTERS = {n: l for l, n in LETTERS_TO_NUMBERS.items()}

def to_osref(input, figures):
    """
    Convert OS reference or (eastings, northings) to OS reference of a given
    number of figures
    """
    if figures < 2 or figures > 10 or figures % 2 != 0:
        raise InvalidFigureReferenceRequest(figures)
    if type(input) == str:
        if not VALID_RE.match(input):
            raise InvalidReferenceError(input)
        clean = SPACES_RE.sub("", input).upper()

        letters = clean[0:2]
        digits = clean[2:]
        eastings = digits[:len(digits)//2]
        northings = digits[len(digits)//2:]

        return (
            letters +
            (eastings + "00000")[:figures//2] +
            (northings + "00000")[:figures//2]
        )
    elif type(input) == tuple and type(input[0]) == int and type(input[1]) == int and len(input) == 2:
        eastings, northings = input
        half_figures = figures // 2
        denominator = 10 ** (5 - half_figures)
        modulo = 10 ** half_figures
        bigsquare = NUMBERS_TO_LETTERS[(eastings // 100000, northings // 100000)]
        return "%s%s%s" % (
            bigsquare,
            str((eastings // denominator) %  modulo).zfill(half_figures),
            str((northings // denominator) % modulo).zfill(half_figures)
        )

    raise InvalidCoordinatesError(input)

class InvalidReferenceError(Exception):
    def __init__(self, reference):
        self.message = "Invalid OS reference (%s)" % reference

    def __str__(self):
        return self.message

class InvalidCoordinatesError(Exception):
    def __init__(self, data):
        self.message = "Invalid OS coorindates (%s)" % data

    def __str__(self):
        return self.message

class InvalidFigureReferenceRequest(Exception):
    def __init__(self, figures):
        self.message = "Cannot create a refrence with these figures: %s" % figures

    def __str__(self):
        return self.message
