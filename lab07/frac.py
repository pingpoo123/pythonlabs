def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

class Frac:
    def __init__(self, a, b):
        d = gcd(a, b)
        self.numer = a // d
        self.denom = b // d
    
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def add(self, x):
        sum_numer = self.numer * x.denom + self.denom * x.numer
        sum_denom = self.denom * x.denom
        sum_frac = Frac(sum_numer, sum_denom)
        return sum_frac

    def sub(self, x):
        dif_numer = self.numer * x.denom - self.denom * x.numer
        dif_denom = self.denom * x.denom
        dif_frac = Frac(dif_numer, dif_denom)
        return dif_frac

    def mul(self, x):
        prd_numer = self.numer * x.numer
        prd_denom = self.denom * x.denom
        prd_frac = Frac(prd_numer, prd_denom)
        return prd_frac

    def div(self, x):
        quo_numer = self.numer * x.denom
        quo_denom = self.denom * x.numer
        quo_frac = Frac(quo_numer, quo_denom)
        return quo_frac
    
    def __add__(self, x):
        return self.add(x)
    
    def __sub__(self, x):
        return self.sub(x)
    
    def __mul__(self, x):
        return self.mul(x)
    
    def __div__(self, x):
        return self.div(x)

# x = Frac(1, 6)
# y = Frac(1, 6)
# z = x.add(y)
# print(f"{x} + {y} = {z}") # Skriver ut 1/6 + 1/6 = 1/3

# x = Frac(2, 3)
# y = Frac(1, 6)
# z = x.sub(y)
# print(f"{x} - {y} = {z}") # Skriver ut 2/3 - 1/6 = 1/2

# x = Frac(2, 5)
# y = Frac(3, 4)
# z = x.mul(y)
# print(f"{x} * {y} = {z}") # Skriver ut 2/5 * 3/4 = 3/10

# x = Frac(3, 7)
# y = Frac(5, 2)
# z = x.div(y)
# print(f"{x} / {y} = {z}") # Skriver ut 3/7 / 5/2 = 6/35

# x = Frac(1, 3).add(Frac(1, 3)).add(Frac(1, 6)).add(Frac(1, 6))
# print(x)

# x = Frac(1, 3).add(Frac(1,3)).add(Frac(1, 6).mul(Frac(1, 6)))
# print(x)

