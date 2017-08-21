from string import digits


def parseTerm(term):
    base = 1
    if term[0] == '-':
        base = -1
    term = term.strip('-')
    for i, ch in enumerate(term):
        if ch not in digits:
            prefix = term[:i]
            n = int(prefix) if prefix else 1
            n = abs(n) * base
            term = term[i:]
            break
    term = ''.join(sorted(term))
    return (term, n)


def simplify(poly):
    terms = []
    signals = '+-'
    term = ''
    poly = poly.strip('+')  # Remove leading +
    for i, ch in enumerate(poly):
        if term and ch in signals:
            terms.append(term)
            term = '' if ch == '+' else '-'
        else:
            term += ch
    if term:
        terms.append(term)
    # Split terms in cof * vars
    parsedTerms = map(parseTerm, terms)
    # Sum the cof os the terms with same vars
    simplified = {}
    for term, n in parsedTerms:
        if simplified.get(term):
            simplified[term] = simplified[term] + n
        else:
            simplified[term] = n
    # Mount the new poly
    new_poly = ''
    for term in sorted(simplified.keys(), key=lambda x: (len(x), x)):
        cof = simplified[term]
        if cof:
            signal = ''
            if cof < 0 or new_poly:
                signal = '-' if cof < 0 else '+'
            cof = abs(cof) if abs(cof) != 1 else ''
            new_poly += '%s%s%s' % (signal, cof, term)
    return new_poly
