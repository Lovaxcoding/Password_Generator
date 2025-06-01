#application pour utiliser un générateur de mot de passe 

def generate_password(length=12, Password = None):
    import random
    import string
    if Password is not None:
        return Password  # Return the provided password if it exists
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    import sys
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
            if length < 1:
                raise ValueError("Length must be a positive integer.")
        except ValueError as e:
            print(f"Invalid input: {e}")
            return
        password = generate_password(length)
    else:
        password = generate_password()
    
    print(f"Generated Password: {password}")

main()