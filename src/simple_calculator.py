class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def __setattr__(self, item, value):
        if len(self.__dict__) <= 10:
            self.__dict__[item] = value
        else:
            print('10 attributes already created')

    def __iter__(self):
        print(self.value)
        return self

    def __add__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value + value)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value - value)

    def __rsub__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(value - self.value)

    def __mul__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value * value)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value / value)

    def __rtruediv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(value / self.value)

    def __pow__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value ** value)

    def __rpow__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(value ** self.value)

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def power(self, *exp):
        for x in exp:
            self.value **= x
        return self

    def root(self, *exp):
        for x in exp:
            self.value **= (1 / x)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    # calculator = Calculator(5)
    # calculator.hhh = 1
    # calculator.ll = 1
    # calculator.ppp = 1
    # calculator.jjj = 1
    # calculator.ttt = 1
    # calculator.ggg = 1
    # calculator.lll = 1
    # calculator.ttt = 1
    # calculator.www = 1
    # calculator.yyy = 1
    # calculator.ooo = 1
    # calculator.uuu = 1

    # print(calculator)
    # print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print((Calculator(3) ** 3) + 4)
    print(3 ** 3)
