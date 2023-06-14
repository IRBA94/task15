yn = str(input("Hi, The script can compare squares color from chessboard, if you are ready, please enter Yes/No: "))

if yn == "Yes":

    x = int(input("Please insert first index for coordinate of the square: "))
    y = int(input("Please insert second index for coordinate of the square: "))
    x1 = int(input("Please insert first index for coordinate of the square: "))
    x2 = int(input("Please insert second index for coordinate of the square: "))


    z = x+y+x1+x2

    #if x, y, x1, x2 <= 0 or x, y, x1, x2 > 8: kitxva: ufro martivad rogor chavwero?
    if x <= 0 or x > 8 or y <= 0 or y > 8 or x1 <= 0 or x1 > 8 or x2 <= 0 or x2 > 8:
        print("Invalid coordinate, you can choose a number from 1 to 8")
    else:
            if z % 2 == 0:
                print("The squares colore with this coordinate is similar")
            else:
                print("The squares colore with this coordinate is not similar")

elif yn == "No":
    print("Lets try another time :)")
else:
    print("incorrect data")
