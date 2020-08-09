from fractions import Fraction

def solve(eq):
    eq = eq.replace("=", "-(")+")"
    eq = eq.replace("(x", "*(x")
    eq = eq.replace("x", "*x")
    eq = eq.replace("+*x", "+x")
    eq = eq.replace("-*x", "-x")
    eq = eq.replace("+*(", "+(")
    eq = eq.replace("-*(", "-(")
    eq = eq.replace("(*x", "(x")
    if eq[0] == '*':
        eq = eq[1:]
    c = eval(eq, {'x': 1j})
    try:
        return -c.real/c.imag
    except ZeroDivisionError:
        if c == 0:
            return '无穷多解'
        else:
            return '无解'


test = input('请输入一个方程：')
test = test.replace(" ", "")
ans = solve(test)
print('The answer is', ans)
if type(ans) != str:
    print(Fraction(ans).limit_denominator())
