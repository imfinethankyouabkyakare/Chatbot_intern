import streamlit as st
import re
from datetime import datetime

def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def get_bot_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Dictionary of patterns and their corresponding responses
    responses = {
        r'\b(hi|hello|hey)\b': [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to meet you!"
        ],
        r'\bhow are you\b': [
            "I'm doing well, thank you for asking! How about you?",
            "I'm great! How can I assist you today?"
        ],
        r'\b(bye|goodbye)\b': [
            "Goodbye! Have a great day!",
            "See you later! Take care!"
        ],
        r'\btime\b': [
            f"The current time is {datetime.now().strftime('%H:%M:%S')}",
        ],
        r'\b(weather|temperature)\b': [
            "I'm sorry, I don't have access to real-time weather data. You might want to check a weather app or website.",
        ],
        r'\bthanks|thank you\b': [
            "You're welcome!",
            "Glad I could help!",
            "My pleasure!"
        ],
        r'\bname\b': [
            "I'm ChatBot, nice to meet you!",
            "You can call me ChatBot!"
        ],
        r'\bjoke\b': [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
    }
    
    # Default response if no pattern matches
    default_responses = [
        "I'm not sure I understand. Could you rephrase that?",
        "I'm still learning! Could you try asking in a different way?",
        "I didn't quite catch that. Can you explain more?"
    ]
    
    # Check each pattern for a match
    for pattern, response_list in responses.items():
        if re.search(pattern, user_input):
            # Return the first response (you could also randomize this)
            return response_list[0]
    
    # If no pattern matches, return a default response
    return default_responses[0]

def main():
    st.title("🤖 Simple Chatbot")
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Generate and display assistant response
        response = get_bot_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

if __name__ == "__main__":
    main()
