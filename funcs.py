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
    float_list.sort()
    negative = bool([item for item in float_list if item < 0])
    if negative is True:
        raise ValueError

    if interval == 0:
        raise ZeroDivisionError
    elif interval < 0:
        raise ValueError

    result = []
    for idx in range(0, len(float_list)-1):
        result.append(round(((float_list[idx + 1] - float_list[idx]) / interval), 4))
    return result
