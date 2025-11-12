num1 = 6
num2 = 7

for n in range(num1):
    #print("N: " + str(n))
    for o in range(num1):
        if n > o:
            print("n was bigger")
        elif n < o:
            print("o was bigger")
        else:
            print("EQUAL")
        #print("O: " + str(o))