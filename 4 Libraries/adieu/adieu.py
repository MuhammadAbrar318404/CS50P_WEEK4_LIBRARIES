def main():
    new_list = get_name()  # Get the list of names from the user input
    new_str = correction(new_list)  # Correct the list of names to form the farewell string
    print(f"\n{new_str}")  # Print the farewell string

def get_name():
    list_un = []  # Initialize an empty list to store names
    while True:
        try:
            user_nam = input("Name:")  # Prompt the user to input a name
            list_un.append(user_nam)  # Append the inputted name to the list
        except EOFError:  # If the user inputs EOF (Ctrl+D), break the loop
            break
    return list_un  # Return the list of names

def correction(new_list):
    new_str = ""  # Initialize an empty string to store the corrected string
    if len(new_list) == 1:  # If there is only one name in the list
        new_str = "Adieu, adieu, to " + new_list[0]  # Form the farewell string for one name
    elif len(new_list) == 2:  # If there are two names in the list
        new_str = "Adieu, adieu, to " + new_list[0] + " and " + new_list[1]  # Form the farewell string for two names
    else:  # If there are more than two names in the list
        new_str = "Adieu, adieu, to " + ", ".join(new_list[:-1]) + ", and " + new_list[-1]  # Form the farewell string for multiple names
    return new_str  # Return the farewell string

main()  # Call the main function to start the program
