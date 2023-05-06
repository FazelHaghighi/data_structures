import os

def permutations(string):
    permute(string, 0)

def permute(string, step):
    if step == len(string):
        print("".join(string))
        return

    for i in range(step, len(string)):
        string_copy = list(string)
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permute(string_copy, step + 1)

def main():
    print("Enter the string:")
    string = input()
    os.system("cls")
    print("Permutations are:")
    permutations(string)

if __name__ == "__main__":
    main()
