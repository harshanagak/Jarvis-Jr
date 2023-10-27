import tkinter as tk
import openai

# OpenAI API Key
openai.api_key = "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"

# Function to handle the conversation and update the text box
def handle_openai_response():
    user_input = user_input_box.get()
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    chat_box.insert(tk.END, f"\nUser: {user_input}\nAssistant: {reply}\n")
    user_input_box.delete(0, tk.END)

# GUI Elements
root = tk.Tk()
root.title("OpenAI Chatbot")

chat_box = tk.Text(root, width=50, height=20)
chat_box.pack()

user_input_box = tk.Entry(root, width=50)
user_input_box.pack()

send_button = tk.Button(root, text="Send", command=handle_openai_response)
send_button.pack()

# Initial message
messages = []
system_msg = "What type of chatbot would you like to create?"
messages.append({"role": "system", "content": system_msg})
chat_box.insert(tk.END, f"System: {system_msg}\n")

root.mainloop()
