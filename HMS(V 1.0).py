import datetime
def gettime():
    return datetime.datetime.now()
print("Welcome to the Health Management System program.")
try:
    q1 = int(input("Enter 1 to add data and 2 to retrive data:"))
    if q1 == 1:
        Data = int(input("Which type of data do you want to modify?\nPress 1 to select Exercise.\nPress 2 to select Diet.\nType here:"))
        if Data == 1:
            name = int(input("Whose data do you want to modify?\nPress 1 to select Harry.\nPress 2 to select Carry.\nPress 3 to select Larry.\nType here:"))
            if name == 1:
                value = input("Type the name of Exercise here:")
                with open("Harry-Ex.txt", "a") as a:
                    a.write(str([str(gettime())]) + ":" + value + "\n")
                    print("Successfully Written!\n")
            elif name == 2:
                value = input("Typr the name of Exercise here:")
                with open("Carry-Ex.txt", "a") as b:
                    b.write(str([str(gettime())]) + ":" + value + "\n")
                    print("Successfully Written!\n")
            elif name == 3:
                value = input("Type the name of Exercise here:")
                with open("Larry-Ex.txt", "a") as c:
                    c.write(str([str(gettime())]) + ":" + value + "\n")
                    print("Successfully Written!\n")
                   
        elif Data == 2:
            name = int(input("Whose data do you want to modify?\nPress 1 to select Harry.\nPress 2 to select Carry.\nPress 3 to select Larry.\nType here:"))
            if name == 1:
                value = input("Type the name of Food here:")
                with open("Harry-Food.txt", "a") as d:
                    d.write(str([str(gettime())]) + ":" + value + "\n")
                    print("Successfully Written!\n")
            elif name == 2:
                value = input("Type the name of Food here:")
                with open("Carry-Food.txt", "a") as e:
                    e.write(str([str(gettime())]) + ":" + "\n")
                    print("Successfully Written!")
            elif name == 3:
                value = input("Type the name of Food here:")
                with open("Larry-Food,.txt", "a") as f:
                    f.write(str([str(gettime())]) + ":" + "\n")
                    print("Successfully Written!\n")

    elif q1 == 2:
        Data_ = int(input("Which type of data do you want to read?\nPress 1 to select Exercise.\nPress 2 to select Diet.\nType here:"))
        if Data_ == 1:
            name = int(input("Whose data do you want to read?\nPress 1 to select Harry.\nPress 2 to select Carry.\nPress 3 to select Larry.\nType here:"))
            if name == 1:
                with open("Harry-Ex.txt") as g:
                    gettime()
                    print(g.read())
            elif name == 2:
                with open("Carry-Ex.txt") as h:
                    gettime()
                    print(h.read())
            elif name == 3:
                with open("Larry-Ex.txt") as i:
                    gettime()
                    print(i.read())

        elif Data_ == 2:
            name = int(input("Whose data do you want to read?\nPress 1 to select Harry.\nPress 2 to select Carry.\nPress 3 to select Larry.\nType here:"))
            if name == 1:
                with open("Harry-Food.txt") as g:
                    gettime()
                    print(g.read())
            elif name == 2:
                with open("Carry-Food.txt") as h:
                    gettime()
                    print(h.read())
            elif name == 3:
                with open("Larry-Food.txt") as i:
                    gettime()
                    print(i.read())
           
except ValueError as j:
    print("Invalid Input!")
