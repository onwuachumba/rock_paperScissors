import random

def rocky_play():

    rock="r"

    paper="p"

    scissors="s"

    paper>rock

    scissors>paper

    rock>scissors

    trials=4

    user_name =input("please enter your name:\n" )

    my_score=0

    my_comp=0

    choices=[rock,paper,scissors]

    print("welcome to rock paper scissors")

    while trials>=0:
          computer=random.choice(choices)

          user_input=(input(f"please input your choice {rock} {paper} or {scissors}\n"))

          if user_input not in choices:
             print("invalid input try again")
          if user_input in choices:
                 if user_input>computer:
                     my_score+=1
                     
                     print(computer)
                     print(f"you have won play again you have {trials} trails left")
                 if user_input<computer:
                     
                     
                     my_comp+=1 
                     print(computer)
                     print(f"you have lost play again you have {trials} trails left")
                 if user_input==computer:
                   
                    print(computer)
                    print(f"it;s a draw play again you have {trials} trails left")
          trials-=1
    print(f"your score is {my_score} ")
    print(f"computer score is {my_comp} ")
    if my_score>my_comp:
        print(f"{user_name} you win")
    elif my_comp>my_score:
        print(f"{user_name}you loose")

rocky_play()        

