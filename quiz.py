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

def add_a_question():
  question=input("Enter a Question: ")
  answer=input("Ok then tell me ,"+question.lower()+": ")
  
  with open ("question.txt","a") as f:
      line=question+"|"+answer+"\n"
      f.write(line)
      

while True:   
    option = show_menu()
    if int(option)== 1:
        print("run quiz")
    if int(option)== 2:
       add_a_question()
    if int(option) == 3:
        break
