import WConio2 as wcon
from collections import Counter
import random as ran
import time

if __name__ == "__main__":
    # Store probability function
    combinations = Counter()
    START = 10

    # Game loop
    n_plays = 0
    predicted = 0
    current_input = ""
    run = True
    print("Start game. Press A or S.")

    while run:
        #time.sleep(0.1)
        # Read input
        #user_input = wcon.getkey()
        
        if ran.randint(0,1):
            user_input = "a"
        else:
            user_input = "s"
        
        #print(f"Player pressed: {user_input} - ", end="")

        if n_plays % 5000 == 0:
            print(f"Nplays: {n_plays} - Prediction rate: {predicted/(n_plays-10)} - Combinations {combinations}")

        if user_input == "q":
            # Quit action
            run = False
            print("Game finished")

        elif user_input in ["a", "s"]:
            # PLAY ACTION

            current_input += user_input
            n_plays += 1

            if len(current_input) == 6:
                # Store current key press
                current_input = current_input[1:]
                combinations[current_input] += 1

                if n_plays > START:
                    # Predict next key press
                    predict_input = current_input[:-1]

                    if combinations[predict_input+"a"] > combinations[predict_input+"s"]:
                        #print("I predict 'a' - ", end="")
                        p = "a"
                    else: 
                        #print("I predict 's' - ", end="")
                        p = "s"
                    if p == user_input:
                        #print("CORRECT", end="")
                        predicted += 1
                    #else:
                        #print("ERROR", end="")
                    
                    #print(f"Prediction rate: {predicted/(n_plays-10)}")

            #print()
            
        elif user_input == "m":
            # Get statistics action
            print("See stats:")
            print("Combinations: ", combinations)
            print("Number of plays: ", n_plays)
            print(f"Prediction rate: {predicted}/{n_plays-10} = {predicted/(n_plays-10)}" )
        else:
            print("invalid input")

    

