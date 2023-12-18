def main():
    file = input("File name: ")
    split_extension = file.lower().strip().split(".")
    check_extension(split_extension[-1])

def check_extension(file):
    if file == "jpg": file = "jpeg"
    match file:
        case "gif" | "jpeg" | "png": print(f"image/{file}")
        case "pdf" | "zip": print(f"application/{file}")
        case "txt" : print("text/plain")
        case _: print("application/octet-stream")


main()
