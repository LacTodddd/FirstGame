from random import choice

def game_pao_ying_chub():
    hands = ["hammer", "scissor", "paper"]
    round_count = 0
    player_score = 0
    com_score = 0
    draw_count = 0

    ## open game
    print("Welcome to Pao Ying Chub game!!")
    print("\nThe rules are simple, choose 1 option/round.")
    print("Available options: hammer, scissor, paper.")
    print("\nOr 'quit' >> if you want to finish the game.")
    print("---------------------------------------")

    ## start the game
    while True:
        round_count += 1  # round_count = round_count + 1
        print(f"\n --- Round: {round_count} ---")
        com_hand = choice(hands)

        player_hand = input("Choose your hand: ").lower()

        ## if the player select "quit" the game
        if player_hand == "quit":
            print("Thank you for playing Pao-Ying-Chub game")
            break

        ## check player_hand
        if player_hand not in hands:
            print("Please select again.")
            round_count -= 1 # not count because player made wrond choice.
            continue

        ## show result/round
        print(f"Player choose: {player_hand}")
        print(f"Computer choose: {com_hand}")


        ## draw
        if player_hand == com_hand:
            print("Draw!")
            draw_count += 1

        ## player win
        elif (player_hand == "hammer" and com_hand == "scissor") or \
             (player_hand == "scissor" and com_hand == "paper") or \
             (player_hand == "paper" and com_hand == "hammer"):
                print("You win this round!!")
                player_score += 1

        ## comp win
        else:
            print("This round you lose.")
            com_score += 1

    ## summary the final score
    print("\n --- Game over! ---")
    print(f"Final score >> you: {player_score} VS Computer: {com_score}")
    print(f"Draws: {draw_count}")

    if player_score > com_score:
        print("Congratulations! You win!!")
    elif player_score < com_score:
        print("Sorry, You lose. Better luck next time!")
    else:
        print("We are tied.")