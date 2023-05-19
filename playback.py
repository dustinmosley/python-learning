# Implement a Python program that prompts the user for input and the outputs that to replace each space with "..."

def main():
    response = input("How did you meet your spouse? ")
    response = response.replace(" ", "...")
    print(response)

main()