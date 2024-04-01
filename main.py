import os

def display_title():
    """Display the title of the CLI Security Suite."""
    title = """
       _____ _      _____             _____       _ _       
      / ____| |    |_   _|           / ____|     (_) |      
     | |    | |      | |    ______  | (___  _   _ _| |_ ___ 
     | |    | |      | |   |______|  \___ \| | | | | __/ _ |
     | |____| |____ _| |_            ____) | |_| | | ||  __/
      \_____|______|_____|          |_____/ \__,_|_|\__\___
    """
    team_info = "Team - Sriram Parisa, Lekha Sri, Satvika N\nMajor Project at MRCET"

    print("\033[1;36m{}\033[0m".format(title))
    print("\033[1;35m{}\033[0m".format(team_info))
    print()

def execute_code(directory):
    """Execute the Python files in the specified directory."""
    files = os.listdir(directory)
    files.sort()  # Sort files alphabetically
    for file in files:
        if file.endswith(".py"):
            print(f"Executing {file}...")
            os.system(f"python3 {os.path.join(directory, file)}")
            print()

if __name__ == "__main__":
    display_title()
    main_directory = "/home/kali/Desktop/CLI"  # Update this with the path to your main directory
    while True:
        os.chdir(main_directory)  # Set the current working directory to the main directory
        print("Please Select the Directory:")
        print("1. Basic")
        print("2. Intermediate")
        print("3. Advanced")
        print("4. Exit")
        selection = input("Enter your Selection: ")
        
        if selection == "1":
            print("\nExecuting Basic directory...\n")
            execute_code("/home/kali/Desktop/CLI/basic")
            print("\nReturning to the main menu...\n")
        elif selection == "2":
            print("\nExecuting Intermediate directory...\n")
            execute_code("/home/kali/Desktop/CLI/intermediate")
            print("\nReturning to the main menu...\n")
        elif selection == "3":
            print("\nExecuting Advanced directory...\n")
            execute_code("/home/kali/Desktop/CLI/advanced")
            print("\nReturning to the main menu...\n")
        elif selection == "4":
            print("\nExiting...")
            break
        else:
            print("\nInvalid selection! Please enter 1, 2, 3, or 4.\n")

        input("Press Enter to return to the main menu...")
