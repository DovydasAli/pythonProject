def zodzio_info(zodis):
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for i in zodis:
        if(i.isupper()):
            didziosios += 1
        elif(i.islower()):
            mazosios += 1
        elif(i.isnumeric()):
            skaiciai += 1

    print("Zodziu kiekis:", len(zodis.split()))
    print("Didziosios raides:", didziosios)
    print("Mazosios raides:", mazosios)
    print("Skaiciai stringe:", skaiciai)

zodzio_info("Labas rytas Stai ir As")
