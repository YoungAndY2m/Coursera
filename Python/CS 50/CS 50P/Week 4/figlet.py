from pyfiglet import Figlet
import sys, random

figlet = Figlet()

# zero command-line argument - random font
if len(sys.argv) == 1:
    msg = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print("Output: \n", figlet.renderText(msg))
# two arguments - specific fonts
elif len(sys.argv) == 3:
    # if not -f or --font and the second is the font name, quit
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        msg = input("Input: ")
        font = sys.argv[2]
        figlet.setFont(font=font)
        print("Output: \n", figlet.renderText(msg))
else: sys.exit("Invalid usage")
