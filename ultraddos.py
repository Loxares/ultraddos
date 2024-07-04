import time

def display_menu():
    print("        ____                 __    __          ")
    print("  __  __/ / /__________ _____/ /___/ /___  _____")
    print(" / / / / / __/ ___/ __ `/ __  / __  / __ \\/ ___/")
    print("/ /_/ / / /_/ /  / /_/ / /_/ / /_/ / /_/ (__  ) ")
    print("\\__,_/_/\\__/_/   \\__,_/\\__,_/\\__,_/\\____/____/ ")


   
    print("Choose one of these options:")
    print("1. DDoS Attack")
    print("2. Update")
    print("3. About")

def main():
    while True:
        display_menu()
        choice = input("set_start>> ")
        
        if choice == '1':
            print("Enter victim's IP:")
            input()
            print("Please wait..")
            time.sleep(40)  
            print("Proccessing..")
            time.sleep(50)
            print("Almost done!")
            time.sleep(30)
            print("Done!")
        elif choice == '2':
            print("Updating, please wait..")
            time.sleep(50)  # Reduced time for testing
            print("Done!")
        elif choice == '3':
            print("This is just a simple DDoS tool to send DDoS attacks on your victim.")
        else:
            print("Invalid choice.")

        another = input("Continue? (y/n): ")
        if another.lower() != 'y':
            break

if __name__ == "__main__":
    main()
