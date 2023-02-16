import sys
import time

print("1: For loop from 1 to 30")
print("2: For loop which displays numbers 10 to 100 in steps (increments) of 5")
print("3: 5 times table")
print("4: Iterating through a string")
print("5: Looping through a list")
print("6: Including else with a list")
print("7: Using int(input(...")
print("8: Including a break")
print("9: Including a nested loop")

def challengeHandler():
    if (choice == 1):
        for i in range(1, 31):
            print(i)
            time.sleep(0.1)
    elif (choice == 2):
        for i in range(10, 101, 5):
            print(1)
            time.sleep(0.1)
    elif (choice == 3):
        for i in range(0, 61, 5):
            print(i)
            time.sleep(0.1)
    elif (choice == 4):
        stringChoice = input("Please enter string: ")
        for element in stringChoice:
            print(element, end=' ')
            time.sleep(0.5)
    elif (choice == 5):
        fruitList = ["Apple", "Cherry", "Banana", "Kiwi", "Dragonfruit", "Starfruit", "Grape"]
        for i in range(len(fruitList)):
            print(fruitList[i])
            time.sleep(0.5)
    elif (choice == 6):
        listChoice = input("Please choose desired list: Fruit(F), or Vegetable(V)")
        if (listChoice.upper() == "F"):
            fruitList = ["Apple", "Cherry", "Banana", "Kiwi", "Dragonfruit", "Starfruit", "Grape"]
            print(fruitList)
            time.sleep(1)
        elif (listChoice.upper() == "V"):
            vegetableList = ["Broccoli", "Peas", "Cauliflower", "Cucumber", "Carrot", "Bok Choy", "Rice"]
            print(vegetableList)
            time.sleep(1)
        else:
            print("Value not recognised. ")
    elif (choice == 7):
        num = int(input("Input number: "))
        print(num)
        time.sleep(1)
    elif (choice == 8):
        while (True):
            i = 0
            if (i < 100):
                print(i)
                i += 1
                time.sleep(0.1)
            break
    elif (choice == 9):
        x = 0
        i = True
        while (x < 100):
            if(i == True):
                print("i is True")
                i = False
            elif (i == False):
                print("i is False")
                i = True
            x += 1
            time.sleep(0.05)
    else:
        print("Challenge not recognised. ")

choice = int(input("Please input number of challenge. "))
challengeHandler()
sys.exit()
