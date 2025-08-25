import wikipedia
import textwrap
import random

wikipedia.set_lang("en")

print("Hello! I'm Clippy")
print("Type 'quit' anytime to exit.")
print("i'm still an experimental modell(v0.1)")

while True:
    #the tokens
    user_input = input("You: ").lower().strip()
    words = user_input.split()
    #quiting
    if user_input == "quit" or user_input == "q":
        print("Clippy: Goodbye!")
        break
    #hi(extend this)
    elif "hello" in words or "hi" in words:
        print("Clippy: Hi there! Need any help?")
    #help if written (extend it like linux)
    elif "help" in words:
        print("Clippy: I can give tips, fetch Wikipedia summaries, or just chat. Try typing: wiki <topic>")

    elif "thanks" in words or ("thank" in words and "you" in words):
        print("Clippy: You're welcome!")
    #what is this question.
    elif ("what" in words and "are" in words and "you" in words) or ("who" in words and "are" in words and "you" in words):
        print("Clippy: I am a text-based chatbot for your personal needs like answering basic questions.")
    #wiki lekérdezés a wiki kulcsszó után
    elif words[0] == "wiki":
        topic = ' '.join(words[1:]).strip()
        if not topic:
            print("Clippy: Please provide a topic after 'wiki' to search for.")
            continue
        try:
            summary = wikipedia.summary(topic, sentences=6)
            # Wrap the text to 110 characters per line
            wrapped_summary = textwrap.fill(summary, width=110)
            print(f"Clippy (Wikipedia):\n{wrapped_summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Clippy: Your topic is ambiguous. Did you mean: {', '.join(e.options[:3])}?" )
        except wikipedia.exceptions.PageError:
            print("Clippy: Sorry, I couldn't find that page.")
    #ha randommot írnak akkor random wiki oldalt nyom be 
    elif "random" in words:
        # get a random article title
        random_title = wikipedia.random()
        print(" Random article:", random_title)
        # now fetch its summary
        try:
            summary_random = wikipedia.summary(random_title, sentences=3)  # 3 sentences only
            print("\nSummary:\n", summary_random)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f" The title '{random_title}' is ambiguous. Options include: {e.options[:5]}")
        except wikipedia.exceptions.PageError:
            print(f" The page '{random_title}' does not exist.")
    #a végén
    else:
        print("Clippy: Hmm, I don't understand that yet... (I'm still limited)")
