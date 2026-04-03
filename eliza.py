from nltk.chat.util import Chat, reflections

# Personalized ELIZA patterns and responses
pairs = [

    (r"hello|hi",
     ["Hey! How are you feeling today?",
      "Hi there 😊 what's on your mind?"]),

    (r"my name is (.*)",
     ["Nice to meet you %1! How can I help you today?",
      "Hello %1 😊 what would you like to talk about?"]),

    (r"i feel (.*)",
     ["Why do you feel %1?",
      "What is making you feel %1 lately?",
      "Do your studies or life contribute to feeling %1?"]),

    (r"i am tired",
     ["You've been working hard. Are you getting enough rest?",
      "University life can be exhausting. What's draining your energy?"]),

    (r"because (.*)",
     ["That sounds important. Tell me more about %1.",
      "Do you think %1 is the main reason?"]),

    (r"i have exams",
     ["Exams can be stressful 😓 How are you preparing?",
      "Do you feel ready for your exams?"]),

    (r"my mother is (.*)",
     ["Family relationships can be complex. How does that make you feel?",
      "Does your mother being %1 affect your daily life?"]),

    (r"i need (.*)",
     ["Why do you need %1?",
      "What would happen if you got %1?"]),

    (r"(.*)",
     ["Tell me more.",
      "I see.",
      "Can you explain that further?",
      "That's interesting, go on."])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def get_eliza_response(user_input: str) -> str:
    return chatbot.respond(user_input)

if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.\n")
    chatbot.converse()