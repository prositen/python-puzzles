def namelist(names):
    return ", ".join([d['name'] for d in names])[::-1].replace(",", '& ', 1)[::-1]
