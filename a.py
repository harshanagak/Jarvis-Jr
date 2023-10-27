import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
user_input = ""
while user_input != "quit()":
    user_input = input()
    if user_input == "quit()":
        break

    messages.append({"role": "user", "content": user_sefcvdhusefwalfel;input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
