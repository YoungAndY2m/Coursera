def get_extensions(input):
    input = input.lower()
    match input:
        case input if (input == 'gif') or (input == 'jpg') or (input == 'jpeg') or (input == 'png'):
            print("image/" + input)
        case input if (input == 'pdf') or (input == 'zip'):
            print("application/" + input)
        case input if input == 'txt':
            print("text/plain")
    return 0

def main():
    file = input("File name: ")
    name, suffix = file.split('.')
    get_extensions(suffix)
    return 0

main()