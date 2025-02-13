print("Hello, GitHub Project!")

def greet_user(name):
    return f"Hello, {name}! Welcome to the GitHub Project."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))