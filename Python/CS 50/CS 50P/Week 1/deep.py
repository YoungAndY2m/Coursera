def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print("Yes" if match_pattern(ans) else "No")

def match_pattern(ans):
    match ans.lower().strip():
        case "42" | "forty-two" | "forty two": return True
        case _: return False

main()
