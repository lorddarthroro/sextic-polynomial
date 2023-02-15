import math

integer = 10000000  # highest integer to test combinations for
# a_i, b_i, c_i, d_i, e_i, f_i = 5, 0, 0, 0, 0, 1


def goal(a, b, c, d, e, f, pow):
    if math.pow(a, pow) + math.pow(b, pow) + math.pow(c, pow) + math.pow(d, pow) + math.pow(e, pow) == math.pow(f, pow):
        return True
    else:
        return False


def loops(degree, n):
    for i in range(1, n):
        a = i
        for j in range(1, n):
            b = j
            for k in range(1, n):
                c = k
                for l in range(1, n):
                    d = l
                    for m in range(1, n):
                        e = m
                        for n in range(1, n):
                            f = n
                        if goal(a, b, c, d, e, f, degree):
                            return a, b, c, d, e, f
    return False


print(loops(6, integer))


