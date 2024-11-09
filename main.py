import requests


def get_joke():
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    joke = response.json()
    return joke


def cat_facts():
    url = 'https://catfact.ninja/facts'
    response = requests.get(url)
    facts = response.json()
    return facts


def get_name():
    url = 'https://tools.estevecastells.com/api/cats/v1'
    response = requests.get(url)
    name = response.json()
    return name


def main():
    cat = """ _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-

"""

    print("Welcome to Catagotchi! Your new (cute) cat friend!")
    print(cat)
    print("What would you like to do?")
    print("1. Get a fun joke")
    print("2. Get a cat fact")
    print("3. Get a cat name")
    print("4. Pet the cat :3")
    print("5. Quit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            joke = get_joke()
            print(joke[0]['setup'])
            print(joke[0]['punchline'])
        elif choice == '2':
            facts = cat_facts()
            print(facts['data'][0]['fact'])
        elif choice == '3':
            name = get_name()
            print(name[0])
        elif choice == '4':
            print("You pet the cat! :3")
            print(cat)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
