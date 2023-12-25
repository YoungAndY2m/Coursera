import sys
from PIL import Image, ImageOps

def main():
    input, output = check_input()
    photoshop(input, output)

def check_input():
    length = len(sys.argv)
    if length < 3: sys.exit("Too few command-line arguments")
    elif length > 3: sys.exit("Too many command-line arguments")
    else:
        try:
            input = sys.argv[1]
            output = sys.argv[2]
            input_extension = input.split(".")[1].lower()
            output_extension = output.split(".")[1].lower()
            if input_extension != output_extension:
                sys.exit("Input and output have different extensions")
            if input_extension not in ["jpg", "jpeg", "png"] or output_extension not in ["jpg", "jpeg", "png"]:
                sys.exit("Invalid input")
        except IndexError:
            sys.exit("Invalid input")
        return input, output

def photoshop(input, output):
    try:
        input_img = Image.open(input)
        shirt = Image.open("shirt.png")
        # resize and crop the input with ImageOps.fit
        size = shirt.size
        input_img = ImageOps.fit(input_img, size)
        input_img.paste(shirt, shirt)
        input_img.save(output)


    except FileNotFoundError: sys.exist(f"Input does not exist")

if __name__ == "__main__":
    main()