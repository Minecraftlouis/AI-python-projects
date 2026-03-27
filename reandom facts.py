import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_ussles_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact.")

while True:
    print("Disclaimer!!! the facts that you are getting are from a website that is literally: https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")

    user_input = input("Press Enter to get a random technology fact or type 'q' to quit...")

    if user_input.lower() == 'q':
        break
    else:
        get_random_ussles_technology_fact()