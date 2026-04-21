from agent import run_agent

print("AutoStream AI Agent 🤖 (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break

    response = run_agent(user_input)
    print("Bot:", response)
