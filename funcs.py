def mirror(word, idx):
    if isinstance(word, str) and isinstance(idx, int):
        if -len(word) <= idx < len(word):
            if 0 <= idx < len(word):
                first_part = word[: idx + 1]
            elif -len(word) <= idx < 0:
                first_part = word[idx:]
            second_part = first_part[::-1]
            final_mirrored = first_part + second_part
            return final_mirrored
        else:
            raise IndexError
    else:
        raise TypeError


def derivee(float_list, interval):
    if interval == 0:
        raise ZeroDivisionError
    elif interval < 0:
        raise ValueError

    if isinstance(float_list, list) is False:
        raise TypeError

    for value in float_list:
        if (isinstance(value, float) is False) and (isinstance(value, int) is False):
            raise TypeError

    result = []
    for idx in range(0, len(float_list) - 1):
        result.append(round(((float_list[idx + 1] - float_list[idx]) / interval), 4))
    return result


def derivee_seconde(float_list, interval):
    return 0
