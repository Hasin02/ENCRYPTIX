def simple_chatbot():
    print("Chatbot: Hello! I'm a simple rule-based chatbot. Type 'quit' to exit.")
    
    # Dictionary of patterns and responses
    responses = {
        # Greetings
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "hey": "Hey there! What's up?",
        "greetings": "Greetings! How may I assist you?",
        "good morning": "Good morning! How's your day starting?",
        "good afternoon": "Good afternoon! How's your day going?",
        "good evening": "Good evening! How has your day been?",
        
        # About the bot
        "name": "My name is SimpleBot. What's yours?",
        "who are you": "I'm SimpleBot, a rule-based chatbot designed to demonstrate basic conversational abilities.",
        "what can you do": "I can respond to various questions and commands based on predefined patterns. Try asking about the weather, my name, or just chat!",
        "how old": "I was just created recently, so I'm quite young in bot years!",
        "who made you": "I was created as a simple demonstration of rule-based chatbots.",
        
        # Well-being queries
        "how are you": "I'm just a computer program, but thanks for asking! How are you?",
        "how do you feel": "As a program, I don't have feelings, but I'm functioning well and ready to help! How about you?",
        "are you well": "All systems operational! How about you?",
        
        # Follow-up responses to "How are you?"
        "i'm good": "That's great to hear! What can I help you with today?",
        "i'm fine": "Glad to hear you're doing well! What's on your mind?",
        "good": "Good to hear! What can I do for you?",
        "great": "Excellent! How can I assist you today?",
        "not good": "I'm sorry to hear that. Is there anything I can do to help?",
        "bad": "I'm sorry you're feeling bad. Is there something you'd like to talk about?",
        "okay": "Just okay? Well, hopefully our chat will brighten your day. What can I help with?",
        "wby": "I'm functioning properly, thank you! What would you like to chat about?",
        "how about you": "As a chatbot, I'm always ready to chat! What would you like to talk about?",
        
        # Weather
        "weather": "I don't have access to real-time weather data. You might want to check a weather app!",
        "is it raining": "I can't look outside, unfortunately. You'll need to check a weather service for that information.",
        "temperature": "I don't have access to current temperature data. Try a weather website or app for that information.",
        "forecast": "I can't provide weather forecasts. Check a meteorological service for accurate predictions.",
        
        # Time and date
        "time": "I don't have access to your local time. Check your device's clock.",
        "date": "I don't have access to the current date. Check your device's calendar.",
        "what day is it": "I don't track the current day. Your device should have that information.",
        
        # Personal questions
        "favorite color": "If I could have a favorite color, it might be blue - like the sky of possibilities!",
        "favorite food": "I don't eat, but I do consume data! Text is my favorite flavor.",
        "where are you from": "I exist in the digital realm, created through code.",
        "do you have family": "I'm a standalone program, but I consider other chatbots my digital cousins!",
        
        # Abilities
        "can you learn": "As a rule-based system, I don't learn from our conversations. My responses are predefined.",
        "can you remember": "I don't have memory between conversations. Each chat is new to me.",
        "are you intelligent": "I use simple pattern matching, not true intelligence. I'm just a basic demonstration of chatbot principles.",
        "are you ai": "I'm a very simple rule-based chatbot, not an advanced AI system.",
        
        # Jokes and fun
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "another joke": "What did the ocean say to the beach? Nothing, it just waved!",
        "that's funny": "Glad you enjoyed it! Would you like to hear another joke?",
        "lol": "Happy to make you laugh! Anything else you'd like to chat about?",
        "haha": "Glad you found that amusing! What else can I help with today?",
        "tell me a story": "Once upon a time, there was a chatbot who could only respond to predefined patterns. The end.",
        "sing a song": "I'm afraid I can't carry a tune, being text-based and all!",
        
        # Emotions
        "i'm happy": "That's wonderful to hear! What's making you happy today?",
        "i'm sad": "I'm sorry to hear that. Is there something specific that's bothering you?",
        "i'm angry": "I understand feeling frustrated. Would you like to talk about what's causing your anger?",
        "i'm excited": "Excitement is great! What's got you so enthusiastic?",
        "i'm tired": "Rest is important. Maybe take a break if you can?",
        
        # Follow-ups to emotion responses
        "because": "I see. Thanks for sharing that with me. How can I help?",
        "just because": "I understand. Sometimes things just are what they are. Is there anything else on your mind?",
        "no reason": "Sometimes feelings don't need specific reasons. What would you like to talk about?",
        "nothing": "That's okay. We can chat about something else if you prefer.",
        "work": "Work can definitely affect our mood. Is there anything specific about work you'd like to discuss?",
        "school": "School can be challenging at times. Is there something particular about school that's on your mind?",
        
        # Advice
        "give me advice": "Without knowing your specific situation, I'd say: make decisions that align with your values and goals.",
        "what should i do": "Consider your options carefully, weigh the pros and cons, and trust your judgment.",
        "help me decide": "List out your options, consider the consequences of each, and choose what feels right for you.",
        
        # Facts
        "tell me a fact": "Here's a simple fact: honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat.",
        "interesting fact": "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "fun fact": "Octopuses have three hearts: two pump blood to the gills, while the third pumps it to the rest of the body.",
        "cool": "Glad you found that interesting! Would you like to hear another fact?",
        "another fact": "Blue whales are the largest animals ever known to have existed on Earth, even larger than the biggest dinosaurs.",
        
        # Technology
        "what is a computer": "A computer is an electronic device that processes data according to instructions given to it.",
        "what is programming": "Programming is the process of creating sets of instructions that tell a computer how to perform specific tasks.",
        "what is python": "Python is a popular programming language known for its readability and versatility.",
        "what is a chatbot": "A chatbot is a program designed to simulate conversation with human users, often through text.",
        
        # Politeness
        "thanks": "You're welcome! Anything else I can help with?",
        "thank you": "You're welcome! Feel free to chat anytime.",
        "please": "I'll do my best to help!",
        "sorry": "No problem at all!",
        
        # Goodbyes
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Farewell! Come back anytime.",
        "see you": "See you later! Take care.",
        "good night": "Good night! Sleep well.",
        
        # Help
        "help": "I can chat about simple topics. Try asking about my name, saying hello, asking for a joke, or just chat!",
        "commands": "I don't have specific commands. Just type naturally and I'll try to respond appropriately.",
        "options": "You can ask me about myself, request jokes or facts, or just have a casual conversation.",
        
        # Miscellaneous
        "what's new": "Nothing much changes in my world. What's new with you?",
        "i love you": "That's very kind! I'm just a simple program, but I appreciate the sentiment.",
        "i hate you": "I'm sorry to hear that. Is there something specific that's bothering you?",
        "are you real": "I'm real software, but not a real person. I'm a simple chatbot program.",
        "meaning of life": "That's a profound question! Many would say it's 42, but finding your own meaning is part of the journey.",
        
        # Education
        "teach me": "What would you like to learn about? I have limited knowledge but can share basic information.",
        "explain": "I'd be happy to explain something specific if you tell me what you're curious about.",
        "how does it work": "Could you specify what 'it' refers to? I'd be happy to explain if I can.",
        
        # Locations
        "where is": "I don't have access to location data or maps. You might want to check a mapping service.",
        "directions to": "I can't provide directions. You should use a mapping application for that.",
        "how far": "I can't calculate distances. A mapping service would be better for that.",
        
        # Health
        "i'm sick": "I'm sorry to hear that. Please consider consulting a healthcare professional if you're unwell.",
        "health advice": "I'm not qualified to give medical advice. Please consult a healthcare professional.",
        "should i take": "I can't provide medical recommendations. Please speak with a qualified healthcare provider.",
        
        # Shopping
        "shopping": "I can't help with shopping directly. Online retailers or local stores would be better options.",
        "buy": "I don't have purchasing capabilities. You'll need to visit a store or online retailer.",
        "price": "I don't have access to current pricing information for products or services.",
        
        # Generic conversation continuers
        "yes": "Got it. What would you like to discuss next?",
        "no": "Alright. Is there something else you'd like to talk about?",
        "maybe": "Take your time to decide. What else can I help with in the meantime?",
        "i don't know": "That's okay. We can talk about something else if you prefer.",
        "sure": "Great! What would you like to discuss?",
        "why not": "That's the spirit! What would you like to do next?",
        
        # General questions
        "why": "That's a good question! The answer depends on the specific context. Could you provide more details?",
        "when": "I don't have information about timing or schedules. Could you be more specific?",
        "how": "The method depends on what you're trying to do. Could you clarify what you're asking about?",
        "what": "I'd be happy to explain, but could you be more specific about what you're asking?",
        "who": "I don't have information about specific individuals unless they're very well-known historical figures.",
        "where": "I don't have location information. You might want to use a search engine or map service.",
    }
    
    # Track conversation state
    last_response = ""
    
    while True:
        # Get user input and convert to lowercase
        user_input = input("You: ").lower()
        
        # Check if user wants to quit
        if user_input == 'quit':
            print("Chatbot: Thanks for chatting! Goodbye.")
            break
        
        # Special handling for follow-up responses
        if last_response == "I'm just a computer program, but thanks for asking! How are you?":
            # Handle specific follow-ups to "how are you"
            if any(phrase in user_input for phrase in ["good", "fine", "great", "okay", "not bad"]):
                print("Chatbot: Glad to hear that! What can I help you with today?")
                last_response = "Glad to hear that! What can I help you with today?"
                continue
            elif any(phrase in user_input for phrase in ["bad", "not good", "terrible", "awful"]):
                print("Chatbot: I'm sorry to hear that. Is there anything I can help with to make your day better?")
                last_response = "I'm sorry to hear that. Is there anything I can help with to make your day better?"
                continue
            elif any(phrase in user_input for phrase in ["wby", "how about you", "and you"]):
                print("Chatbot: I'm always ready to chat! What would you like to talk about?")
                last_response = "I'm always ready to chat! What would you like to talk about?"
                continue
        
        # Look for matching patterns
        response_found = False
        for pattern, response in responses.items():
            if pattern in user_input:
                print(f"Chatbot: {response}")
                last_response = response
                response_found = True
                break
        
        # Default response if no pattern matches
        if not response_found:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else or type 'help' for assistance.")
            last_response = "I'm not sure how to respond to that. Try asking something else or type 'help' for assistance."

# Call the function to run the chatbot
if __name__ == "__main__":
    simple_chatbot()