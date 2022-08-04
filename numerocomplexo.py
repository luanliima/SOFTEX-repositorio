class complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)

    def __add__(self, outronumero):
        real = self.real + outronumero.real
        imag = self.imag + outronumero.imag
        return complexo(real, imag)

    def __sub__(self, outronumero):
        real = self.real - outronumero.real
        imag = self.imag - outronumero.imag
        return complexo(real, imag)

    def __mul__(self, outronumero):
        real = self.real * outronumero.real
        imag = self.imag * outronumero.imag
        return complexo(real, imag)

    def __truediv__(self, outronumero):
        real = self.real / outronumero.real
        imag = self.imag / outronumero.imag
        return complexo(real, imag)        

c = complexo (2, 4)
j = complexo (8, 3)

print (c)
print (j)

print (c + j)
