



#
# def gatedate():
#     import datetime
#     return datetime.datetime.now()




def func1():
    def gatedate():
        import datetime
        return datetime.datetime.now()

    """this function is used to (lock/write) food and exercise on customer file"""
    print("\n1 = Harry\n2 = Rohan\n3 = Hammad")
    inp2 = int(input("client number : "))

    # starting code for harry
    if inp2 == 1:
        print("\n1 = food\n2 = exercise")
        inp3 = int(input("what you want to lock : "))

        if inp3 == 1:
            f = open("harryfood.txt", "a")
            inp4 = input("\nwrite about food : \n")
            f.write(inp4)
            f.close()
            print("you have successfully write this on harry's food", "(", inp4, ")\n")

        elif inp3 == 2:
            f = open("harryexercise.txt", "a")
            inp5 = input("\nwrite about exercise : ")
            f.write(inp5)
            f.close()
            print("you have successfully write this on harry's food", "(", inp5, ")\n")

        else:
            print("your input is wrong!\n")

    # starting code for rohan
    elif inp2 == 2:
        print("\n1 = food\n2 = exercise")
        inp6 = int(input("what you want to lock : "))

        if inp6 == 1:
            f = open("rohanfood.txt", "a")
            inp7 = input("\nwrite about food : ")
            f.write(inp7)
            f.close()
            print("you have successfully write this on harry's food", "(", inp7, ")\n")

        elif inp6 == 2:
            f = open("rohanexercise.txt", "a")
            inp8 = input("\nwrite about exercise : ")
            f.write(inp8)
            f.close()
            print("you have successfully write this on harry's food", "(", inp8, ")\n")
        else:
            print("your input is wrong!")

    # starting code for hammad
    elif inp2 == 3:
        print("\n1 = food\n2 = exercise")
        inp9 = int(input("what you want to lock : "))

        if inp9 == 1:
            f = open("hammadfood.txt", "a")
            inp10 = input("\nwrite about food : ")
            f.write(inp10)
            f.close()
            print("you have successfully write this on harry's food", "(", inp10, ")\n")

        elif inp9 == 2:
            f = open("hammadexercise.txt", "a")
            inp11 = input("\nwrite about exercise : ")
            f.write(inp11)
            f.close()
            print("you have successfully write this on harry's food", "(", inp11, ")\n")
        else:
            print("your input is wrong!\n")

    else:
        print("your input is wrong!\n")  # func1 code end here


def func2():
    """this function is used to (retrieve / see) the food and exercise"""
    print("\n1 = Harry\n2 = Rohan\n3 = Hammad")
    inp2 = int(input("client number : "))

    # starting code for harry
    if inp2 == 1:
        print("\n1 = food\n2 = exercise")
        inp3 = int(input("what you want to see : "))

        if inp3 == 1:
            f = open("harryfood.txt")
            print(f.read())
            f.close()

        elif inp3 == 2:
            f = open("harryexercise.txt")
            print(f.read())
            f.close()

        else:
            print("your input is wrong!\n")

        # starting code for rohan
    elif inp2 == 2:
        print("\n1 = food\n2 = exercise")
        inp6 = int(input("what you want to see : "))

        if inp6 == 1:
            f = open("rohanfood.txt")
            print(f.read())
            f.close()

        elif inp6 == 2:
            f = open("rohanexercise.txt")
            print(f.read())
            f.close()

        else:
            print("your input is wrong!\n")

        # starting code for hammad
    elif inp2 == 3:
        print("\n1 = food\n2 = exercise")
        inp9 = int(input("what you want to see : "))

        if inp9 == 1:
            f = open("hammadfood.txt")
            print(f.read())
            f.close()

        elif inp9 == 2:
            f = open("hammadexercise.txt")
            print(f.read())
            f.close()

        else:
            print("your input is wrong!\n")

    else:
        print("your input is wrong!\n")  # func2 code end here


while True:
    print("\n1 = lock\n2 = retrive")
    inp1 = int(input("what you want to do : "))
    if inp1 == 1:
        func1()
    elif inp1 == 2:
        func2()
    else:
        print("your input is wrong!")
