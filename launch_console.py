name = input("Enter your name: ")
print(f"Welcome to {name}'s launch console!")
while True:
    print("""
    --- Menu ---
    1) About me
    2) My goals
    3) Launch day plan
    4) Exit
    """)
    try:
        choice = int(input("Pick 1-4: "))
    except ValueError:
        print("Enter a number!")
        choice = -1

    if choice == 1:
        print(f"I am {name} and I am a student in Code2College!")
    elif choice == 2:
        print("My goal for this term is to learn GitHub and ship a fully completed project.")
    elif choice == 3:
        print("This term, I plan to build the flashcard/quiz generator project.")
    elif choice == 4:
        print("Exiting! Thank you!")
        break
    else:
        print("Please pick 1, 2, 3, or 4.")