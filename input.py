def input_probability_and_alphabet(filename):
    """
    Input probability of every symbol in alphabet,
    separated by ' '.
    :param filename: string
    :return: list(float)
    """
    with open(filename, 'r') as fin:
        return [[float(num) for num in fin.readline().split(' ') if num.strip()],
                [sym for sym in fin.readline().split(' ')]]


def input_text(filename):
    """
    Input text.
    :param filename: string
    :return: str
    """
    with open(filename, 'r') as fin:
        return fin.read()

