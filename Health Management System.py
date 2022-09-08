# 1. Ask if we want to lock data or retrieve data
# 3. There are three clients
# 4. Each client will have two files
# # 5. We will write two files and will also take time as input
def gettime():
    import datetime
    return datetime.datetime.now()

inp = int(input("Welcome to HEALTH MANAGEMENT SYSTEM\nTo enter data: press 0\nTo retrieve data: Press 1\n"))
new = bool(inp)
Type1 = int(input("For Food Data: press 1.\nFor Exercise Data: press 2\n"))

if inp == False:
    z = int(input("Whose data do you wish to enter?\nFor Harry: press 1\nFor Rohan: press 2\nFor Hammad: press 3\n"))
    if z == 1:
         if Type1 == 1:
             f = open("HarryFoodDetails.txt", "w")
         else:
            f = open("HarryExerciseDetails.txt", "w")

    elif z == 2:
        if Type1 == 1:
            f = open("RohanFoodDetails.txt", "w")
        else:
            f = open("RohanExerciseDetails.txt", "w")
    elif z == 3:
        if Type1 == 1:
            f = open("HammadFoodDetails.txt", "w")
        else:
            f = open("HammadExerciseDetails.txt", "w")

    data = input("Enter your information")
    f.write(str([str(gettime())]) + "  " + data + "\n")
    f.close()

elif inp ==True:
    y = int(input("Whose data do you wish to retrieve?\nFor Harry: press 1\nFor Rohan: press 2\nFor Hammad: press 3\n"))
    if y == 1:
            if Type1 == 1:
                f = open("HarryFoodDetails.txt")
                print(f.readlines())
                f.close()
            else:
                f = open("HarryExerciseDetails.txt")
                print(f.readlines())
                f.close()
    elif y == 2:
             if Type1 == 1:
                 f = open("RohanFoodDetails.txt")
                 print(f.readlines())
                 f.close()
             else:
                 f = open("RohanExerciseDetails.txt")
                 print(f.readlines())
                 f.close()
    elif y == 3:
            if Type1 == 1:
                 f = open("HammadFoodDetails.txt")
                 print(f.readlines())
                 f.close()
            else:
                 f = open("HammadExerciseDetails.txt")
                 print(f.readlines())
                 f.close()

#Ram Krishna

