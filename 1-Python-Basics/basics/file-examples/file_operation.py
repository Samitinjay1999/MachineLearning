import os

path = "example2.txt"
if os.path.exists(path):
    print(f"The path '{path}' already exists.")
else:
    ui = input(f"The path doesn't exist. Want to create it? (y/n): ").lower()
    if ui == 'y':
        with open(path, 'w') as file:
            print(f"File '{path}' is created.")
            ui2 = input("Want to write something? (y/n): ").lower()
            if ui2 == 'y':
                text = input("Enter the text to write: ")
                file.write(text)
                print("Write successful.\nThank You...")
            elif ui2 == 'n':
                print("OK! Have a good day.")
            else:
                print("SORRY! Wrong command...")
    elif ui == 'n':
        print("Thank You!")
    else:
        print("SORRY! Wrong command...")
