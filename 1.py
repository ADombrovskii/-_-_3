def dec_boost(boost):
    def wrapper(v, t, a):
        s = v * t + (a * t ** 2) / 2
        print(s)

    return wrapper


@dec_boost
def boost(v1, v2, t):
    if isinstance(v1, int) == False or isinstance(v2, int) == False or isinstance(t, int) == False:
        raise ValueError('v1 или v2 или t - не числа')
    if t == 0:
        raise Exception('t = 0')

    a = (v1 - v2) / t

    print(a)
