import random
import string

def generate_password(length, complexity, num_passwords=None):
    if num_passwords is None:
        if complexity == "low":
            characters = string.ascii_letters + string.digits
        elif complexity == "medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "high":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
        else:
            print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    else:
        passwords = []
        for _ in range(num_passwords):
            characters = string.printable
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.append(password)
        return passwords

def main():
    print("Welcome to the Password Generator!")
    while True:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate (enter 1 for single password): "))

        if num_passwords == 1:
            while True:
                complexity = input("Enter the complexity level ('low', 'medium', or 'high'): ")
                if complexity.lower() in ['low', 'medium', 'high']:
                    password = generate_password(length, complexity)
                    if password:
                        print("Generated Password:", password)
                    break
                else:
                    print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")

        else:
            print("\nGenerated Passwords:")
            passwords = generate_password(length, None, num_passwords)
            if passwords:
                for password in passwords:
                    print(password)

        while True:
            generate_another = input("Do you want to generate another password set? (yes/no): ")
            if generate_another.lower() in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if generate_another.lower() != "yes":
            break

if __name__ == "__main__":
    main()
