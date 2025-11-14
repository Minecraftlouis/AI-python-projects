print ("Hello, I am AI bot. What's your name:")

name = input()

print(f"Hello, {name}")
print("How are you feeling today? (good/bad)")
mood = input().lower()


if mood == "good":
    print ("I'm so happy to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print ("I see, sometimes it's hard to put feelings into words")
    
print (f"It was nice chatting with you, {name}")