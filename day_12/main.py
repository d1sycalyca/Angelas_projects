import random
art = r"""
        $$\   $$\                         $$\                                  $$$$$$\                                                              
        $$$\  $$ |                        $$ |                                $$  __$$\                                                             
        $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\  
        $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\ 
        $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ |$$ |  \__|
        $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$   ____|$$ |      
        $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      
        \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \______/  \______/  \_______|\_______/ \_______/  \_______|\__|      
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            """

def number_gen():
    print(art)
    print("Welcome to the number guessing game")
    print("Im thinking of a number between 1-100")
    difficulty = input("Choose a difficulty: type 'easy or 'hard': ").lower()
    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5
    comp_number = random.choice(range(1,101))
    print(f"You have {lives} attempts to guess the number")
    print(comp_number)
    while lives > 1:
        guess = int(input("Make a guess: "))
        lives -=1
        if guess > comp_number:
            print("Too high.\nGuess again.")
        elif guess == comp_number:
            print(f"You guessed it. The answer was {comp_number}")
            break
        else:
            print("Too low.\nGuess again.")
            print(f"You have {lives} attempts to guess the number")
    again = input("Would you like to play again? Type 'y' or 'n': ")
    if again == "y":
        print("\n" * 20)
        number_gen()


number_gen()