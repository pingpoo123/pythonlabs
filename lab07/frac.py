def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return abs(a)

class Frac:
    def __init__(self, a, b):
        self.numer = a // gcd(a, b)
        self.denom = b // gcd(a, b)

    def __str__(self):
        return str(f'{self.numer}/{self.denom}')
    
    def add(self, addend):
        a = int(self.numer) * int(addend.denom) + int(self.denom) * int(addend.numer)
        b = 


x = Frac(10,25)
y = Frac(10,25)
print(x.numer)
print(x.denom)
print(x.add(y))