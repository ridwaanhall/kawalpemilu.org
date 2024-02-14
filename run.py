from base.base import OptionHandler

if __name__ == "__main__":
    print("+-----------------------------------------------+")
    print("|         Welcome to Kawal Pemilu 2024!         |")
    print("+-----------------------------------------------+")
    print("| Choose an option:                             |")
    print("| 1. Fetch report data                          |")
    print("| 2. Fetch JSON TPS data v1                     |")
    print("| 3. Fetch JSON TPS data v2                     |")
    print("+-----------------------------------------------+")
    option = input("Enter your choice (1 or 2 or 3): ")

    OptionHandler.perform_option(option)
