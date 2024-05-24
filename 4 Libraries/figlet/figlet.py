import sys  # Import the sys module for accessing command line arguments
import random  # Import the random module for choosing a random font
from pyfiglet import Figlet  # Import the Figlet class from the pyfiglet module
def main():
    figlet = Figlet()  # Create an instance of the Figlet class
    font_list = []  # Initialize an empty list to hold the available fonts
    font_list = figlet.getFonts()  # Get the list of available fonts from the Figlet instance
    com_str = ["-f", "--font"]  # List of command line arguments for font selection
     # Check if no command line arguments are provided or if there are exactly three arguments
    if len(sys.argv)==1 or len(sys.argv)==3:
        if len(sys.argv)==1:
            user_string=input()
            font_name=random.choice(font_list)
            figlet.setFont(font=font_name) # chose the font
            print(figlet.renderText(user_string))
        else:
            if sys.argv[1] in com_str and sys.argv[2] in font_list:
                user_string=input()
                figlet.setFont(font=sys.argv[2])# Font set by the user
                print(figlet.renderText(user_string))
            else:
                sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()

