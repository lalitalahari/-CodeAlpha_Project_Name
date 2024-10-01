# Function to preprocess text: converts to lowercase and removes punctuation
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    # Remove punctuation by keeping only alphanumeric characters and spaces
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text
# General response function based on some basic conversation patterns
def generate_response(user_input):
    # Preprocess the user's input
    processed_input = preprocess_text(user_input)
    # Responding to greetings
    if any(greeting in processed_input for greeting in ["hello", "hi", "hey", "greetings"]):
        return "Hello! How can I assist you today?"
    # Asking for the chatbot's name
    elif "your name" in processed_input:
        return "I am ChatBot, your friendly assistant."
    # Responding to how the chatbot is doing
    elif "how are you" in processed_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    # Responding to goodbye
    elif any(bye in processed_input for bye in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"
    # If the user says something like "what" or "why"
    elif "what" in processed_input or "why" in processed_input:
        return "That's an interesting question! I'm here to help you with anything you need."
    # Respond to questions about feelings
    elif any(word in processed_input for word in ["feel", "feeling", "happy", "sad"]):
        return "Emotions are complicated! How can I assist you with that?"
    # Catch-all for any other input
    else:
        return "I didn't quite understand that. Could you please rephrase?"
# The main chatbot loop
def chatbot():
    print("ChatBot: Hello! I am ChatBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        # Exit the conversation if the user says "bye"
        if 'bye' in preprocess_text(user_input):
            print("ChatBot: Goodbye!")
            break
        # Generate a response for any input
        response = generate_response(user_input)
        print("ChatBot:", response)
# Run the chatbot
if __name__ == "__main__":
    chatbot()
