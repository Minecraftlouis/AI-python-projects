print ("Hello, I am AI bot. What's your name:")

name = input()

print(f"Hello, {name}")
print("How are you feeling today? (good/bad/angryLo)")
mood = input().lower()


if mood == "good":
    print ("I'm so happy to hear that! Hope you stay happy!")
elif mood == "bad":
    print("I'm sorry to hear that. Try taking a walk in the park, maeby your mood will change.")
elif mood == "angry":
    print("Oh no! Try meditating to cool down.")
else:
    print ("Sorry, I didn't get that")
    
print (f"I hope I helped you, {name}, Bye!")