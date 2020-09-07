def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            self.num = top
            self.den = bottom
            self.common = gcd(self.num, self.den)
        else:
            print("Are the numerator and denominators integers?")

        if self.den < 0:
            self.num = -1 * self.num
            self.den = -1 * self.den
            self.common = gcd(self.num, self.den)



    def __str__(self):
        return str(self.num // self.common) + "/" + str(self.den // self.common)

    def __repr__(self):
        return str(self.num // self.common) + "/" + str(self.den // self.common)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        try:
            if self.num and self.den:
                newnum = self.num * otherfraction.den + \
                         self.den * otherfraction.num
                newden = self.den * otherfraction.den
                return Fraction(newnum, newden)
        except:
            return None

    def __iadd__(self, otherfraction): # +=
        try:
            if self.num and self.den:
                newnum = self.num * otherfraction.den + \
                         self.den * otherfraction.num
                newden = self.den * otherfraction.den
                return Fraction(newnum, newden)
        except:
            return None

    def __radd__(self, otherfraction): # +=
        try:
            if self.num and self.den:
                self.num = self.num * otherfraction.den + \
                                 self.den * otherfraction.num
                self.den = self.den * otherfraction.den
                return Fraction(self.num, self.den)
        except:
            return None

    def __sub__(self, otherfraction):
        try:
            if self.num and self.den:
                newnum = self.num * otherfraction.den - \
                         self.den * otherfraction.num
                newden = self.den * otherfraction.den
                return Fraction(newnum, newden)
        except:
            return None

    def __mul__(self, otherfraction):
        try:
            if self.num and self.den:
                newnum = self.num * otherfraction.num
                newden = self.den * otherfraction.den
                return Fraction(newnum, newden)
        except:
            return None

    def __truediv__(self, otherfraction):
        try:
            if self.num and self.den:
                newnum = self.num * otherfraction.den
                newden = self.den * otherfraction.num
                return Fraction(newnum, newden)
        except:
            return None

    def __eq__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den

                return firstnum == secondnum
        except:
            return None

    def __gt__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den
                return firstnum > secondnum
        except:
            return None

    def __ge__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den
                return firstnum >= secondnum
        except:
            return None


    def __lt__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den
                return firstnum < secondnum
        except:
            return None

    def __le__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den
                return firstnum <= secondnum
        except:
            return None

    def __ne__(self, other):
        try:
            if self.num and self.den:
                firstnum = self.num * other.den
                secondnum = other.num * self.den
                return firstnum != secondnum
        except:
            return None

x = Fraction(4, -3)
y = Fraction(2, 2)

print(x - y)
print(repr(x-y))
# print(x * y)
# print(x / y)
