import calendar
def keliamieji_metai(metai):
    atsakymas = calendar.isleap(metai)
    if atsakymas == True:
        print(metai, "yra keliamieji")
    else:
        print(metai, "nera keliamieji")

keliamieji_metai(int(input("Iveskite metus")))