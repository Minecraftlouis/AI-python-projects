import re,random
from colorama import Fore, init


init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phunket"],
    "mountains":["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Damascus", "Athens", "Vancouver", "Yerevan"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Beacuse it had a virus!"
    "Why did the penny arrest the nickel? Beacuse it was a copper!"\
    
]

def normalise_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalise_input(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + "Travel bot: How about {suggestion}!")
        print(Fore.CYAN + "Travel Bot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        
        if answer == "yes":
            print (Fore.GREEN +f"TravelBot: Awesome! Enjoy {suggestion}!")
            
        elif answer == "no":
            print(Fore.RED + "Travel Bot: Let's try another.")
        else:
            print(Fore.RED + "I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that kind of destination")
    
    show_help()
        