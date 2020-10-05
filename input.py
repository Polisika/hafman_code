def input_probability(filename):
    """
    Input probability of every symbol in alphabet,
    separated by ' '.
    :param filename: string
    :return: list(float)
    """
    with open(filename, 'r') as fin:
        s = fin.read().split(' ')
        return [float(num) for num in s if num.strip()]


def input_text(filename):
    """
    Input text.
    :param filename: string
    :return: str
    """
    with open(filename, 'r') as fin:
        return fin.read()

