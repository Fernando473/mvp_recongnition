from word2number import w2n


def to_number(array: []) -> str:
    try:
        numbers = [w2n.word_to_num(number) for number in array]

        return ''.join(map(str, numbers))
    except Exception as e:
        return str(e)
