import csv

def intro ():
    print("Welcome to the Book Trade Terminal!")
    print("")
    options()



def options():
    print("Type '1' to see everything in stock")
    print("Type '2' to look in different categories of books")
    print("Type '3' to search for a specific author")
    inp  = int(input('\n' + "Make sure to type a number:" + '\n'))

    print("")

    if (inp == 1):
        pAll()
    elif (inp == 24):
        edit()
    else:
        print('\n' "Invalid input! Please try again!" '\n')
        options()



def pAll():
    for row in rows:
        for col in row:
            print("%10s"%col, end=" ")
        print('\n')
    
    print("If you would like the books sorted type '1'. If not, hit enter.")
    inp = input()
    
    print("")

    if (inp == '1'):
        sortAll()
    else:
        print("L")



def sortAll():
    print("How would you like the books sorted?")
    print("Type '1' for alphabetically")
    print("Type '2' for categories")
    
    print("")

    inp = int(input("Make sure to type a number:" '\n'))

    print("")

    if (inp == 1):
        print("a")
    elif (inp == 2):
        print("c")
    else:
        print("Try Again!")
        sortAll()



def edit():
    print("Welcome to the Textbook Trade Terminal Editor!" '\n')
    print("")





filename = "data.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

intro()


print("Have a nice day")
quit()
