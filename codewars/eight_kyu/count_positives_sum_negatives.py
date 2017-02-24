def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    return [len(list(filter(lambda x: x > 0, arr))), sum(filter(lambda x: x < 0, arr))]