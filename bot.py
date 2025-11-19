import streamlit as st
from datetime import datetime

# Predefined rules for chatbot responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    # Greeting patterns
    if "hello" in user_input or "hi" in user_input or "hey" in user_input or "greetings" in user_input:
        return "Hello! How can I assist you today?"

    # Asking name
    elif "your name" in user_input or "who are you" in user_input or "what are you" in user_input:
        return "I am a simple rule-based chatbot!"

    # Asking about well‑being
    elif "how are you" in user_input:
        return "I'm doing great! Ready to chat with you."

    # Asking for help
    elif "help" in user_input or "support" in user_input or "assist" in user_input:
        return "Sure! Tell me what you need help with."

    # Time-Telling Rule
    elif "what is the time" in user_input or "tell me the time" in user_input or "current time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # Addition
    elif "add" in user_input or "+" in user_input:
        try:
            if "add" in user_input:
                parts = user_input.split("add")[1].strip().split("and")
            else:
                parts = user_input.split("+")
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            result = num1 + num2
            return f"The result is {result}."
        except:
            return "Please provide two numbers to add."

    # Subtraction
    elif "subtract" in user_input or "-" in user_input:
        try:
            if "subtract" in user_input:
                parts = user_input.split("subtract")[1].strip().split("from")
                num2 = float(parts[0].strip())
                num1 = float(parts[1].strip())
            else:
                parts = user_input.split("-")
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
            result = num1 - num2
            return f"The result is {result}."
        except:
            return "Please provide two numbers to subtract."

    # Multiplication
    elif "multiply" in user_input or "*" in user_input:
        try:
            if "multiply" in user_input:
                parts = user_input.split("multiply")[1].strip().split("and")
            else:
                parts = user_input.split("*")
            num1 = float(parts[0].strip())
            num2 = float(parts[1].strip())
            result = num1 * num2
            return f"The result is {result}."
        except:
            return "Please provide two numbers to multiply."

    # Thank you
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Let me know if you need anything else."

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return "Goodbye! Have an amazing day ahead!"

    else:
        return "I didn't fully understand that, but I'm improving! Try rephrasing your message."

# Streamlit UI
st.set_page_config(page_title="Rule-Based Chatbot", page_icon="🤖")
st.title("🤖 Rule-Based Chatbot (Streamlit Interface)")
st.write("Chat with the intelligent rule-based bot.")

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")

# User input
user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input.strip():
        st.session_state.chat_history.append(("user", user_input))
        bot_reply = get_bot_response(user_input)
        st.session_state.chat_history.append(("bot", bot_reply))
        st.rerun()







# import tkinter as tk
# from tkinter import scrolledtext

# # Predefined rules for chatbot responses

# def get_bot_response(user_input):
#     user_input = user_input.lower()

#     # Greeting patterns
#     if "hello" in user_input or "hi" in user_input or "hey" in user_input or "greetings" in user_input:
#         return "Hello! How can I assist you today?"
    
#     # Asking name
#     elif "your name" in user_input or "who are you" in user_input or "what are you" in user_input:
#         return "I am a simple rule-based chatbot!"
    
#     # Asking about well‑being
#     elif "how are you" in user_input:
#         return "I'm doing great! Ready to chat with you."
    
#     # Asking for help
#     elif "help" in user_input or "support" in user_input or "assist" in user_input:
#         return "Sure! Tell me what you need help with."

#     # Time-Telling Rule   
#     elif "what is the time" in user_input or "tell me the time" in user_input or "current time" in user_input:
#         from datetime import datetime
#         current_time = datetime.now().strftime("%H:%M:%S")
#         return f"The current time is {current_time}."
    
#     # Addition
#     elif "add" in user_input or "+" in user_input:
#         try:
#             if "add" in user_input:
#                 parts = user_input.split("add")[1].strip().split("and")
#             else:
#                 parts = user_input.split("+")
#             num1 = float(parts[0].strip())
#             num2 = float(parts[1].strip())
#             result = num1 + num2
#             return f"The result is {result}."
#         except:
#             return "Please provide two numbers to add."

#     # Subtraction
#     elif "subtract" in user_input or "-" in user_input:
#         try:
#             if "subtract" in user_input:
#                 parts = user_input.split("subtract")[1].strip().split("from")
#                 num2 = float(parts[0].strip())
#                 num1 = float(parts[1].strip())
#             else:
#                 parts = user_input.split("-")
#                 num1 = float(parts[0].strip())
#                 num2 = float(parts[1].strip())
#             result = num1 - num2
#             return f"The result is {result}."
#         except:
#             return "Please provide two numbers to subtract."

#     # Multiplication
#     elif "multiply" in user_input or "*" in user_input:
#         try:
#             if "multiply" in user_input:
#                 parts = user_input.split("multiply")[1].strip().split("and")
#             else:
#                 parts = user_input.split("*")
#             num1 = float(parts[0].strip())
#             num2 = float(parts[1].strip())
#             result = num1 * num2
#             return f"The result is {result}."
#         except:
#             return "Please provide two numbers to multiply."
    
#     # Thank you
#     elif "thanks" in user_input or "thank you" in user_input:
#         return "You're welcome! Let me know if you need anything else."
    
#     # Goodbye
#     elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
#         return "Goodbye! Have an amazing day ahead!"

#     else:
#         return "I didn't fully understand that, but I'm improving! Try rephrasing your message."


# # GUI Application

# root = tk.Tk()
# root.title("Rule-Based Chatbot")
# root.geometry("400x400")
# root.configure(bg="#cdcdcd")

# chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=17, bg="#f7f5f5", fg="black", font=("Arial", 10))
# chat_window.pack(pady=10)
# chat_window.config(state=tk.DISABLED)

# user_input_field = tk.Entry(root, width=40, font=("Arial", 10))
# user_input_field.pack(pady=10)


# def send_message():
#     user_msg = user_input_field.get()
#     if user_msg.strip() == "":
#         return

#     chat_window.config(state=tk.NORMAL)
#     chat_window.insert(tk.END, "You: " + user_msg + "\n")

#     bot_response = get_bot_response(user_msg)
#     chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n")
#     chat_window.config(state=tk.DISABLED)

#     user_input_field.delete(0, tk.END)
#     chat_window.see(tk.END)

# send_button = tk.Button(root, text="Send", command=send_message, bg="#E6EFE6", fg="black", font=("Arial", 10)) 
# send_button.pack()

# root.mainloop()
