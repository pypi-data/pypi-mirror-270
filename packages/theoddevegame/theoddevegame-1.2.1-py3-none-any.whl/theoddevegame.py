"""
Hello everyone, I am Prashant Bhatt, Class XII D of DPS Haldwani, batch 2024-25.
I made this game the odd eve game, a digitised version of hand cricket.
So I invite you all to this wonderful game of OddEve. So enjoy.
This is version 1.2 dated 25 April 2024 under MIT License
"""
ODDEVE_PICS = ["""
           .-.
           | |
           | |
           | |
    _.-.-.-| | 
   ; \\( \\    |
   |\\_)\\ \\   | 
   |    ) \\  |
   |   (    / 
    \\______/ """, """
       .-.
       | |    / )
       | |   / /
       | |  / /
    _.-| |_/ / 
   ; \\( \\    |
   |\\_)\\ \\   | 
   |    ) \\  |
   |   (    / 
    \\______/ """, """
      _.-.
    _| | | 
   | | | | 
   | | | | _ 
   | i ' i\\_|
   |      (_ |
   |      _| |
   |     ;   | 
   |        /
    \\______/ """, """
   .-.-.-.-.
   | | | | |
   | | | | |    
   | | | | |
   | | | | |
   |  ( \\  \\
   |   \\ \\  | 
   |    ) \\ |
   |   (   / 
    \\_____/ """, """
      _.-._
    _| | | |
   | | | | |
   | | | | |  __
   | i ' i | / /
   |       |/ /
   |       ' /
   |      ;  | 
   |        /
    \\______/ """, """
    _
   ( (
    \\=\\ 
   __\\_`-\\
  (____))( \\---
  (____)) _
   (____))
    (__))___/--- """
]

import random,time

def chance():
    """
    Simulates a toss by asking the user for their preference (odd or even)
    and then randomly choosing a number between 1 and 6 for the program.

    Returns:
        True if the user wins the toss (odd + program_number is even), False otherwise.
    """
    print("Here is the toss. Let's go!!!. Choose 'odd' or 'eve(even)'\n")
    user_oe=isplayerchance("odd","eve","o","e")
    prog=random.randint(1,6)
    user_tn=validnum()
    pic(user_tn, "Player's")
    pic(prog, "System's")
    tot=prog+user_tn
    if not user_oe:
        if tot%2!=0:
            print("Player won the toss.")
            return True
        else:
            print("System won the toss")
            return False
    else:
        if tot%2==0:
            print("Player won the toss")
            return True
        else:
            print("System won the toss")
            return False

def SuperOver():
    """
  Simulates a Super Over when both players are tied in Odd Even Cricket.

  This function plays an additional 6 "balls" with the following rules:
      - Batsman cannot get out during the Super Over.
      - Runs are added to the batsman's score for each turn.
      - Player batting first plays all 6 balls and sets a target.
      - Player batting second needs to score 1 run more than the target to win.
  """
    print("\nIt's a tie! Going to Super Over...")

  # Player batting first
    player_score = 0
    for i in range(6):
        print("Player's turn:")
        player_number = validnum()
        print("Now System's turn (bowling).")  # Simulate bowling for clarity
        program_number = random.randint(1, 6)
        pic(player_number, "Player's")
        pic(program_number, "System's")
        if player_number != program_number:
            player_score += player_number
            print(f"Player's score: {player_score}")
        else:
            player_score += 0
            print(f"System's score: {player_score}")

  # Program batting second
    target_score = player_score + 1  # Program needs 1 more than Player's score
    program_score = 0
    for i in range(6):
        print(f"\nSystem's turn (target: {target_score}):")
        program_number = random.randint(1, 6)
        print("Now Player's turn (bowling).")  # Simulate bowling for clarity
        player_number = validnum()
        pic(player_number, "Player's")
        pic(program_number, "System's")
        if player_number != program_number:
            program_score += program_number
            print(f"System's score: {program_score}")
            if program_score >= target_score:
                break   # Exit loop if Player 2 reaches or surpasses the target
        else:
            program_score += 0
            print(f"System's score: {program_score}")

  # Determine winner based on scores
    if program_score > player_score:
        print(f"Sorry, Player! System has won the Super Over and the match! System's final score: {program_score}. Player's final score: {player_score}. Better luck next time.")

    elif player_score > program_score:
        print(f"Congratulations! Player! You won the Super Over and the match! Player's final score: {player_score}. System's final score: {program_score}. Keep it up. ")

    else:
        print("It's a tie even in the Super Over! We need another Super Over!")
    # Call SuperOver again for another tie-breaker
        SuperOver()
        
def iscompchance(odd,eve): #if comp won the toss
    """
    Stimulates the program decision if it won the toss.

    Args:
        odd: A string displayed as a prompt.
        eve: same as odd.

    Returns: boolean values True, False or integral values 0,1.
    """
    c=random.randint(0,1)
    if c==0:
        print("System takes", eve)
        return 1 
    else:
        print("System takes", odd)
        return 0

def isplayerchance(odd, eve, o, e):#if player won toss
    """
    Same as iscompchance function, except, it is for user.
    """
    print(odd,"or",eve)
    b=input()
    if b.lower().startswith(o):
        return 0
    elif b.lower().startswith(e):
        return 1
    else:
        return isplayerchance(odd, eve, o, e)

def pic(e, my):#print the pics corresponding to the runs
    """
    Prints the runs corresponding to the input given. 
    Gives the hand gesture of the corresponding number.
    
    Args:
        e: an integer representing the prompt by the user or the program.
        my: a string representing the player name.
    """
    print(my,"number is",e,end=" ")
    print(ODDEVE_PICS[e-1])

def validnum(message="Enter your number, between 1 to 6 : "):
    """
  Prompts the user for a valid number and returns it as an integer.

  Args:
      message: A string to display as a prompt to the user.

  Returns:
      An integer representing the valid number entered by the user.
  """
    while True:
        guess = input(message)
        if guess.isdigit() and 1 <= int(guess) <= 6:
            return int(guess)
    else:
        print("Invalid input. Please enter a number between 1 and 6.")

def gamelogic(d, point):#the main gamelogic which runs the game.
    """
  Runs the core game loop of Odd Even Cricket until the user quits.

  Returns: None
    """
    if d:
        print("System's chance.")#comp. bat first
        e=random.randint(1,6)
        print("System has played its chance, Player's turn.")
        f=validnum()
        pic(e, "System's")
        pic(f, "Player's")
        if e==f:#its, out and the chasing starts
            target=point+1
            chase=0
            print(f"Oh, System got out, Player need {target} runs to win \nPlayer's batting.")
            while chase<target:#while runs are less than required runs keep going
                h=validnum()
                print("Player you have played your chance, System's turn.")
                i=random.randint(1,6)
                pic(i, "System's")
                pic(h, "Player's")
                if h==i:#batsman out before winning
                    if point==chase:#same point superover starts
                        tx=False
                        SuperOver()
                        break
                    else:
                        print(f"Sorry, Player! System has won the match! by {point-chase} runs. System's final score: {point}. Player's final score: {chase}. Better luck next time.")
                        tx=False
                        break
                else:
                    chase+=h
                    print("target is", target)
                    print("Now Player, you need",target-chase,"runs")
                    print("Player's score is", chase)
                    tx=True
            if tx:    
                print(f"Congratulation Player, you win, keep it up. System's final score: {point}. Player's final score: {chase}.")

        else:
            point+=e
            print("System's score is", point)
            gamelogic(d, point)
            return point
    else:
        ct=0
        if 50<=point>=55:
            if ct==0:
                print("Player, you have scored a half-century while batting first. Congrats."))
                ct+=1
        if 100<=point>=105:
            if ct==1:
                print("Player, you have scored a century while batting first. Congrats.")
                ct+=1
        if 200<=point>=205:
            if ct==2:
                print("Player, you have scored a Double-century while batting first. Congrats.")
                ct+=1

        print("Player's chance.")
        e=validnum()    
        print("Player, you have played your chance, Now System's turn.")
        f=random.randint(1,6)
        pic(e, "Player's")
        pic(f, "System's")
        if f==e:
            target=point+1
            chase=0
            print("Oh, Player you got out, system need", target, "runs to win \nSystem's batting")
            while chase<target:
                i=random.randint(1,6)
                print("System has played its chance, Player's turn.")
                h=validnum()
                pic(i, "System's")
                pic(h, "Player's")
                if h==i:
                    if point==chase:
                        tx=False
                        SuperOver()
                        break
                    else:
                        print(f"Oh, System lost by {point-chase} runs. Congratulation!! Keep it up. System's final score is {chase}. Player's final score is {point}.")
                        tx=False
                        break
                else:
                    chase+=i
                    print("target is ",target)
                    print("Now System need",target-chase,"runs")
                    print("System's score is", chase)
                    tx=True
            if tx:
                print(f"Sorry, Player! System has won the match! System's final score: {chase}. User's final score: {point}. Better luck next time.")

        else:
            point+=e
            print("Player's score is", point)
            gamelogic(d, point)
            return point

def rules():
    """
  Prints a detailed explanation of the rules of Odd Even hand Cricket.
    """
    print("\nWelcome to Odd Even Cricket!")
    print("\n**Gameplay:**")
    print(
        "- The game is played between two players: you and the program."
        "\n- Players take turns 'batting' and 'bowling' using finger gestures representing numbers between 1 and 6."
        "\n- To 'bat', a player chooses a number and reveals it with a finger gesture."
        "\n- To 'bowl', a player chooses a number and reveals it with a finger gesture."
        "\n- The batsman scores points equal to their chosen number during their turn."
        "\n- The batsman gets 'out' if their chosen number matches the bowler's number."
        "\n- You have only one wicket. i.e you can get out only one time."
    )

    print("\n**Winning Conditions:**")
    print(
        "- The player batting second, has to reach the target set by player batting first. If he succeed he win, else player batting first wins."
        "\n- If both players have the same score after their turns are exhausted, a Super Over is triggered."
        "\n- Target is +1 run made by player batting first."
    )

    print("\n**Super Over:**")
    print(
        "- A Super Over consists of 6 additional 'balls' for each player."
        "\n- The batsman cannot get out during the Super Over, but score don't get added if same both throws same number."
        "\n-  - If you bat first:"
        "\n      - You play all 6 balls and set a target score."
        "\n      - The program needs to score 1 run more than your score to win."
        "\n  - If the program bats first:"
        "\n      - It plays all 6 balls and sets a target score."
        "\n      - You need to score exactly or more then the target score to win, i.e. +1 run than the program score to win."
    )

    print("\n**Toss:**")
    print(
        "- A coin toss is simulated to determine who bats first."
        "\n- If you win the toss, you can choose to bat or bowl first."
        "\n- If the program wins the toss, it randomly decides whether to bat or bowl first."
    )

    print("\n**Program Decisions:**")
    print(
        "- The program randomly chooses a number between 1 and 6 when bowling/batting."
        "\n- The program randomly decides whether to bat or bowl first if it wins the toss."
    )

    print("\n**User Interaction:**")
    print(
        "- You will be prompted to enter your chosen number and confirm your preference (bat or bowl) if you win the toss."
        "\n- You can quit the game by entering 'q' after a match."
    )

    print("\n**Additional Notes:**")
    print(
        "- This program uses ASCII art representations of hand gestures to simulate the game."
        "\n- Scores for both players will be displayed throughout the game."
    )

    print("\nReady to play? Let's go!")
    
def game():#below is the preview image of the game.
    """
    The main gaim loop of the odd eve game
    """
    print("""
          __      __  __        __    ___  __       __   __   __       __         __
    |  | |   |   |   |  | |\\/| |       |  |  |     |  | |  \\ |  \\   / |   \\    / |
    |  | |-- |   |   |  | |  | |--     |  |  |     |  | |  | |  |  /  |--  \\  /  |--
    |/\\| |__ |__ |__ |__| |  | |__     |  |__|     |__| |__; |__; /   |__   \\/   |__
    """)
    v=input("Want to know about rules, if yes press y, else press any key to continue.\n")
    if v.lower().startswith("y"):
        rules()
    while True:#game starts.
        point=0
        d=chance()
        if not d:
            k=iscompchance("bowling", "batting")
            gamelogic(k, point)
        else:
            k=isplayerchance("batting","bowling","bat","bowl")
            gamelogic(k, point)

        q=input("To quit press q else press enter key: ")
        if q.lower().startswith("q"):
            break

game()
