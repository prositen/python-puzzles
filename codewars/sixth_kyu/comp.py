def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return sorted([x**2 for x in set(array1)]) == sorted(set(array2)) if array1 and array2 else True