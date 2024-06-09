def calc_rpn(exp):
    s = [] 
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    parts = exp.split()
    for p in parts:
        if p in ops:
            y = s.pop()
            x = s.pop()
            res = ops[p](x, y)
            s.append(res)
        else:
            s.append(float(p))
    return s[0]
print(calc_rpn("3 5 + 8 *"))