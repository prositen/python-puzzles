def recoverSecret(triplets):
    word = dict()
    first = list()
    last = list()

    for a, b, c in triplets:
        if a not in word:
            word[a] = {'before': set(), 'after': set()}
        if b not in word:
            word[b] = {'before': set(), 'after': set()}
        if c not in word:
            word[c] = {'before': set(), 'after': set()}
        word[b]['before'].add(a)
        word[b]['after'].add(c)

        word[c]['before'].add(a)
        word[c]['before'].add(b)
        word[a]['after'].add(b)
        word[a]['after'].add(c)

    word_len = len(word)
    while len(first) + len(last) < word_len:
        for n, v in word.items():
            if len(v['before']) == 0:
                first.append(n)
            elif len(v['after']) == 0:
                last.append(n)

        for v in word.values():
            v['before'].discard(first[-1])
            v['after'].discard(last[-1])
        if first[-1] in word:
            del word[first[-1]]
        if last[-1] in word:
            del word[last[-1]]

    return ''.join(first) + ''.join(last[::-1])