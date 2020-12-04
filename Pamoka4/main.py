def pasisveikink():
    print("Labas rytas!")

pasisveikink()

def pasisveikink(vardas):
    print("Labas", vardas)

pasisveikink("Simai")

def kvadratas(skaicius):
    kvadratu = skaicius ** 2
    print(kvadratu)

kvadratas(2)

def kvadratas(skaicius):
    kvadratu = skaicius ** 2
    return kvadratu


print(5+ kvadratas(5))