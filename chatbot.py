import nltk.chat.util

pairs = [
    [r'hi|hello|hey',
     ['Hello!', 'Hi there!', 'Hey!']
     ],
    [r'how are you?',
     ['I am fine, thank you!', 'Doing well, and you?']
     ],
    [r'what is your name?',
     ['I am a chatbot created to assist you.']
     ],
    [r'What can you do for me?',
     ['I can assist you in many fields.']
     ],
    [r'quit',
     ['Goodbye! See you soon Take care.']
     ],
    [r'(.*)',
     ['I\'m not sure how to respond to that. Can you ask something else?']
     ]
]


def chatbot():
    name = input("What is your name? ")

    print("Hi", name, " I'm a chatbot. Type 'quit' to exit.")
    chat = nltk.chat.util.Chat(pairs, nltk.chat.util.reflections)
    chat.converse()


if __name__ == "__main__":
    chatbot()
