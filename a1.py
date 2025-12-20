
import colorama
from colorama import Fore,Style
from textblob import TextBlob
import sys
import time


colorama.init()


print(f"{Fore.CYAN}🥳🥳 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")
user_name = input (f"{Fore.MAGENTA} Please enter your name:{Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent" 
    
conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_processing_animation():
    print(f"{Fore.CYAN}🕵️ Detecting sendiment clues", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stydout.flush()
        
def analyze_sentiment(text):
    """
      Analyzes the sentiment of the input text using TextBlob.
    Categories:
    - Positive: Polarity > 0.25
    - Neutral: Polarity between -0.25 and 0.25
    - Negative: Polarity < -0.25
    """
    global positive_count, negative_count, neutral_count
    
    try: 
        blob = TextBlob(text)
        
        sentiment = blob.sentiment.polarity
        
        conversation_history.append(text)
        
        if sentiment > 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN}🌟 Very Positive sentiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
        
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN}😊 Positive sendiment detected, Agent {user_name}! (Score: {sentiment:.2f})"
        
        elif -0.25 <= sentiment <= 0.25:
            neutral_count +=1
            return f"\n {Fore.YELLOW}😐 Neutral sentiment detected"
        
        elif -0.75 <= sentiment < -0.25:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"
        else:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Very Negative sentiment detected, Agent {user_name}. (Score: {sentiment:.2f})"

    except Exception as e:
                  return f"{Fore.RED}An error occurred during sentiment analysis: {str(e)}"
       
        
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your scenteces using textblob and show you the sentiment")
print(f"Type {Fore.YELLOW}-'reset'{Fore.CYAN}, {Fore.YELLOW}-'history'{Fore.CYAN},"
     f"or {Fore.YELLOW}-'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter text or  valid command")
        continue
    
    
    if user_input.lower() == "exit":
        print (f"\n{Fore.BLUE}   Exiting Sendiment Spy. Farewell, Agent {user_name}!  {Style.RESET_ALL}")
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🗞️ Conversation History cleared!{Style.RESET_ALL}")
    elif user_input.lower() == "history":
        if not conversation_history:
            print("No conversation history yet")