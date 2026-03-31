from tracker import start_session, stop_session, show_summary

def menu():
    while True:
        print("\n1. Start Study Session")
        print("2. Stop Session")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            subject = input("Enter subject: ")
            start_session(subject)

        elif choice == '2':
            stop_session()

        elif choice == '3':
            show_summary()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

menu()
