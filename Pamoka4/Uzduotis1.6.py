
def unikalus(skaiciai):
    unikalus_sk = []
    for x in skaiciai:
        if x not in unikalus_sk:
            unikalus_sk.append(x)
    return unikalus_sk

sk = [10, 10, 50, 50, 95, 55, 95, 66]  #galima ideti ir stringus
print(unikalus(sk))