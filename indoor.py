# Implement a program that prompts the user for input and then outputs that input in lowercase

def main():
    response = input("What do you see in the mirror? ")
    response = response.lower()
    print("The mirror sees...")
    print(response)

main()