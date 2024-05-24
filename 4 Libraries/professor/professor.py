import random  # Import the random module to generate random numbers

def main():
    level = get_level()  # Get the difficulty level from the user
    print("Score:", generate_integer(level))  # Generate and solve problems, then print the final score

def get_level():
    while True:
        level = input("Level:")  # Prompt the user to input the difficulty level
        if level.isnumeric() and 0 < int(level) <= 3:  # Check if the input is a number between 1 and 3
            break  # Exit the loop if the input is valid
        else:
            pass  # Continue the loop if the input is not valid
    return level  # Return the valid difficulty level

def generate_integer(level):
    gen_problem = 0  # Initialize the problem counter
    score = 0  # Initialize the score counter
    a = 0  # Initialize the counter for incorrect attempts

    while gen_problem != 10:  # Loop until 10 problems have been generated
        if int(level) == 1:
            x, y = random.randint(0, 9), random.randint(0, 9)  # Generate two random numbers between 0 and 9
        elif int(level) == 2:
            x, y = random.randint(10, 99), random.randint(10, 99)  # Generate two random numbers between 10 and 99
        elif int(level) == 3:
            x, y = random.randint(100, 999), random.randint(100, 999)  # Generate two random numbers between 100 and 999

        right_answer = x + y  # Calculate the correct answer
        user_answer = input(f"{x} + {y} =")  # Prompt the user to solve the problem

        while True:
            if user_answer.isnumeric() and int(user_answer) == right_answer:  # Check if the user's answer is correct
                score += 1  # Increment the score
                gen_problem += 1  # Increment the problem counter
                break  # Exit the inner loop to generate a new problem
            else:
                a += 1  # Increment the incorrect attempt counter
                if a < 3:  # Allow up to 3 attempts for each problem
                    print("EEE")  # Print an error message
                    user_answer = input(f"{x} + {y} =")  # Prompt the user to solve the problem again
                else:
                    print(f"{x} + {y} = {x + y}")  # Print the correct answer after 3 incorrect attempts
                    gen_problem += 1  # Increment the problem counter
                    break  # Exit the inner loop to generate a new problem

    return score  # Return the final score

if __name__ == "__main__":
    main()  # Call the main function to start the program
