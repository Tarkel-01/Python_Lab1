def pre_process(a=0.97):
    def wrapper1(func):
        def wrapper2(s):
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i - 1]
            func(s)

        return wrapper2

    return wrapper1


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


s = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

plot_signal(s)
