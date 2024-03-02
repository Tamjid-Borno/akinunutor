
import akinator

def main():
    # Create an instance of the Akinator game
    aki = akinator.Akinator()

    # Start the game and get the first question
    question = aki.start_game()

    # Continue the game until the progression reaches 80%
    while aki.progression <= 80:
        user_input = input(question + "\n\t")
        if user_input == "b":
            try:
                question = aki.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            question = aki.answer(user_input)

    # End the game and make the final guess
    aki.win()

    # Display the guess and ask if it's correct
    correct = input(f"It's {aki.first_guess['name']}({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t")
    if correct.lower() == "yes" or correct.lower() == "y":
        print("Yay\n")
    else:
        print("Oof\n")

if __name__ == "__main__":
    main()
