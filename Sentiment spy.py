
import colorama
from colorama import Fore,Style
from textblob import TextBlob
import sys
import time


colorama.init()

user_name = ""
print(f"{Fore.CYAN}🥳🥳 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")
    
conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_processing_animation():
    print(f"{Fore.CYAN}🕵️ Detecting sendiment clues", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
        
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
    
    
def execute_command(command):
    """
    Executes predefined commands:
    -'summary': Displays sentiment statisics
    -'reset': Clears conversation history and counters
    -'help': lists avalible commands
    """
    
    global conversation_history,positive_count,negative_count,neutral_count
    
    
    if command == "summary":
        return(f"{Fore.CYAN}🕵️ Mission Report:\n"
               f"{Fore.GREEN}Positive messages detected:{positive_count}\n"
               f"{Fore.RED}Negative sentences detected:{negative_count}\n"
               f"{Fore.RED}Neutral senteces detected:{neutral_count}\n")
    elif command == "reset":
        conversation_history.clear()
        positive_count = neutral_count = negative_count = 0
        return f"{Fore.CYAN}🕵️ Mission reset! All previous data has been cleared!"
    elif command == "history":
        return "\n".join([f"{Fore.CYAN}Message {i+1}: {msg}" for i, msg in enumerate(conversation_history)]) \
            if conversation_history else f"{Fore.YELLOW}No conversation history avalible."
    elif command == "help":
        # Display a list of available commands
        return (f"{Fore.CYAN}🔍 Available commands:\n"
                f"- Type any sentence to analyze its sentiment.\n"
                f"- Type 'summary' to get a mission report on analyzed sentiments.\n"
                f"- Type 'reset' to clear all mission data and start fresh.\n"
                f"- Type 'history' to view all previous messages and analyses.\n"
                f"- Type 'exit' to conclude your mission and leave the chat.")
    
    else:
        
        return f"{Fore.RED}Unknown command. Type 'help for a list of commands."
    
def get_valid_name():
    """
    Contuniously promps the user until they give vald name
    """
    
    while True:
        name = input("what your name? ").strip()
        if name and name.isalpha():
            return name
        else:
            print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")
            
def save_sentiment_report():
    '''
    Saves the sentiment analysis results to a file named 'username_sentiment_analysis' based on the user's input.
    '''
    
    global user_name, positive_count, negative_count, neutral_count
    
    filename = f"Agent {user_name}'s_sentiment_analysis.txt"
    with open(filename, "w") as file:
        file.write(f"Sentiment Analysis Report for Agent {user_name}\n")
        file.write(f"Positive Sendiments: {positive_count}\n")
        file.write(f"Negative Sentiments: {negative_count}\n")
        file.write(f"Neutral Sentiments Detected: {neutral_count}\n")
        file.write(f"\nConversation History:\n")
        for idx, sentence in enumerate(conversation_history):
            file.write(f"{idx + 1}. {sentence}\n")
    print(f"{Fore.CYAN}Sentiment analysis report saved as {filename}.")
    
    
def start_sentiment_chat():
     """
    Main loop for interacting with the Sentiment Spy chatbot. Users can:
    - Analyze the sentiment of sentences
    - Use commands like 'help', 'summary', and 'reset'
    - Exit the chat anytime
    """
     print(f"{Fore.CYAN}{Style.BRIGHT}🕵️ Welcome to Sendiment Spy! Your personal  detective is here!")
     
     global user_name
     user_name = get_valid_name()
     print(f"\n{Fore.CYAN}Nice to meet you, Agent {user_name}! Type your sentences to analyze emotions. Type 'help' for options. ")
     
     while True:
         
         user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent{user_name}: {Style.RESET_ALL}").strip()
         
         if not user_input:
             print(f"{Fore.RED}Please enter a non-empty message or type 'help' for avalible options.")
             continue
         
         if user_input.lower() == "exit":
             print(f"\n{Fore.BLUE}🔚Mission complete! Exiting Sentiment. Farewell, Agent {user_name}!")
             print(execute_command("summary"))
             
             save_sentiment_report()
             break
         
         elif user_input.lower() in ["summary", "reset", "history", "help"]:
             print (execute_command(user_input.lower()))
         else:
             
             show_processing_animation()
             result = analyze_sentiment(user_input)
             print(result)
             
if __name__ == "__main__":
    start_sentiment_chat()