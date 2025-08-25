import wikipedia #importing an online wiki page 
import random  #importing random function
import textwrap  # Import textwrap for wrapping long text
import time #imported time
import os  # Import os for launching applications

wikipedia.set_lang("en")

print("Hello! I'm Clippy")
print("Type 'quit' anytime to exit.")
print("I'm still an experimental model (v0.2)")

# Define command functions
def handle_greeting():
    print("Clippy: Hi there! Need any help?")

def handle_help():
    print("Clippy: I can give tips, fetch Wikipedia summaries, open apps, or just chat. Try typing: wiki <topic>")

def handle_thanks():
    print("Clippy: You're welcome!")

def handle_identity():
    print("Clippy: I am a text-based chatbot for your personal needs like answering basic questions.")

def handle_wiki(topic):
    if not topic:
        print("Clippy: Please provide a topic after 'wiki' to search for.")
        return
    try:
        summary = wikipedia.summary(topic, sentences=6)
        # Wrap the text to 110 characters per line
        wrapped_summary = textwrap.fill(summary, width=110)
        print(f"Clippy (Wikipedia):\n{wrapped_summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Clippy: Your topic is ambiguous. Did you mean: {', '.join(e.options[:3])}?")
    except wikipedia.exceptions.PageError:
        print("Clippy: Sorry, I couldn't find that page.")

def handle_random():
    random_title = wikipedia.random()
    print("Clippy: Random article:", random_title)
    try:
        summary = wikipedia.summary(random_title, sentences=5)
        # Wrap the text to 110 characters per line
        wrapped_summary = textwrap.fill(summary, width=110)
        print("\nSummary:\n", wrapped_summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Clippy: The title '{random_title}' is ambiguous. Options include: {', '.join(e.options[:5])}")
    except wikipedia.exceptions.PageError:
        print(f"Clippy: The page '{random_title}' does not exist.")

def handle_open_app(app_name):
    apps = {
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "steam": r"C:\Program Files (x86)\Steam\Steam.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    }
    if app_name in apps:
        app_path = apps[app_name]
        try:
            os.startfile(app_path)
            print(f"Clippy: Opening {app_name.capitalize()}...")
        except Exception as e:
            print(f"Clippy: Failed to open {app_name}. Error: {e}")
    else:
        print(f"Clippy: I don't know how to open '{app_name}'. Try adding it to my app list!")

def handle_unknown():
    print("Clippy: Hmm, I don't understand that yet... (I'm still limited)")

# Command handler mapping
commands = {
    "hello": handle_greeting,
    "hi": handle_greeting,
    "help": handle_help,
    "thanks": handle_thanks,
    "thank you": handle_thanks,
    "what are you": handle_identity,
    "who are you": handle_identity,
    "wiki": handle_wiki,
    "random": handle_random,
    "open": handle_open_app, 
}

# Main loop
while True:
    user_input = input("You: ").lower().strip()
    if user_input in ["quit", "q"]:
        print("Clippy: Goodbye!")
        break

    words = user_input.split()
    command = words[0]
    args = ' '.join(words[1:])

    # Execute the corresponding command function
    if command in commands:
        if command == "wiki":
            handle_wiki(args)
        elif command == "open":
            handle_open_app(args)
        else:
            commands[command]()
    else:
        handle_unknown()