def suma(skaicius):
    sudetis = 0
    for x in skaicius:
        sudetis += x
    return sudetis

skaiciai = [1, 50, 64, 75, 2]
print(suma(skaiciai))