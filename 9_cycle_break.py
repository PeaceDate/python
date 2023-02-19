# Task
# Give priveleges to users work in our company
# Programmers work in VCS
# Designers work in Illustrator
# Managers not need any priveleges
# With help of input function we get email and his occupation from user and create system list with users priveleges.
# Also we don't know how many users need to be added to system and privilege for Illustrator can be given only from third try + on one run we can't add more than 5 users, if limit is reached we need tell about it.

if __name__ == '__main__':
    limit_of_users = 0

    while limit_of_users < 5:
        email = input("Enter email: ")
        if email == "":
            print("Email can't be empty")
            break
        occupation = input("Enter occupation: ").lower()

        system = None
        access_attempts = None

        if occupation == "programmer":
            system = "VCS"
            access_attempts = 1
        elif occupation == "designer":
            system = "Illustrator"
            access_attempts = 3
        elif occupation == "manager":
            print("You don't need any privileges")
            continue

        for _ in range(access_attempts):
            print(f"User {email} can work in {system}")

        limit_of_users += 1 
        print(f"Added {limit_of_users} users, left {5 - limit_of_users} users")
