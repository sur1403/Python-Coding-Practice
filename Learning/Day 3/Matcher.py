x = 4

match x:
    case 0: 
        print("x is 0")

    # case 4: 
    #     print("x is 4")

    case 8:
        print("x is 8")

    case _ if x > 80:
        print("x is greater than 80")

    case _ if x < 20:
        print("x is less than 20")

