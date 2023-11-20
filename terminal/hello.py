from decouple import config

def main():
    name = config('NAME', default=None)
    if username:
        print(f"Hello {username}!")
    else:
        name = input('Username: ')
        save_username(name)
        print(f"Hello {name}")

main()