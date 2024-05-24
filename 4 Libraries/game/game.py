import random  # Import the random module to generate random numbers

def main():
    while True:
        user_input = input("Level:")  # Prompt the user to input the level (upper bound for the random number)
        if user_input.isnumeric() and int(user_input) > 0:  # Check if the input is a positive number
            break  # Exit the loop if the input is valid
        else:
            pass  # Continue the loop if the input is not valid

    rand_number = random.randint(1, int(user_input))  # Generate a random number between 1 and the user-provided level

    while True:
        guess_number = input("Guess:")  # Prompt the user to guess the number
        if guess_number.isnumeric() and int(guess_number) > 0:  # Check if the guess is a positive number
            if int(guess_number) > rand_number:  # If the guess is greater than the random number
                print("Too large!")  # Inform the user that the guess is too large
            elif int(guess_number) < rand_number:  # If the guess is less than the random number
                print("Too small!")  # Inform the user that the guess is too small
            else:
                print("Just right!")  # Inform the user that the guess is correct
                exit()  # Exit the program
        else:
            pass  # Continue the loop if the guess is not valid

main()  # Call the main function to start the program
