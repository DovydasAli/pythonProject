def didziausias_skaicius(*args):
     didziausias = 0
     for sk in args:
         if sk > didziausias:
             didziausias = sk
     return didziausias


print(didziausias_skaicius(10, 50, 112, 154, 2, 987))