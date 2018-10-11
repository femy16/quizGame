def show_menu():

    print("Quiz Game")
    print("----------")
    print()
    print("1.Run Quiz")
    print("2.Enter a Question")
    print("3.Exit")
    print()
    
    option=input("Enter options: ")
    return option
 
while True:   
    option = show_menu()
    if int(option) == 3:
        break
