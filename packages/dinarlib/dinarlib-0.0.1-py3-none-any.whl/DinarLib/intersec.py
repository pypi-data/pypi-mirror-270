def intersec(a,b):
    c = []
    for element in a:
        if element in b:
            c.append(element)
    return len(c)