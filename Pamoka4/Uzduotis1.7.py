
def pirminis_sk(sk):
    if sk > 1:
        for i in range(2, sk):
            if (sk % i) == 0:
                print(sk, "nera pirminis skaicius")
                break
            else:
                print(sk, "yra pirminis skaicius")
                break

pirminis_sk(3)