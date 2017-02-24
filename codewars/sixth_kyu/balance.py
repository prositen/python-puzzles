from collections import Counter


def balance(arr1, arr2):
    return sorted(Counter(arr1).values()) == sorted(Counter(arr2).values())
