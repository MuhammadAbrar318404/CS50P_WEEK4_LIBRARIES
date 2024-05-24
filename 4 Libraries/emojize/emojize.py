import emoji
def main():
    # Prompt the user to input text
    user_input = input("Input: ")
    # Convert the input text to emoji using the emoji library
    print(emoji.emojize(user_input))

if __name__ == "__main__":
    main()  # Call the main function to start the program