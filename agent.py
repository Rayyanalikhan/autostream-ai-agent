from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture
from memory import Memory

memory = Memory()

def run_agent(user_input):
    intent = detect_intent(user_input)
    memory.update("intent", intent)

    # Greeting
    if intent == "greeting":
        return "Hey! 👋 I can help you with AutoStream pricing or features."

    # Inquiry → RAG
    if intent == "inquiry":
        return get_answer(user_input)

    # High Intent → Lead Flow
    if intent == "high_intent":
        if not memory.get("name"):
            return "Awesome! What's your name?"

    # Collect Name
    if not memory.get("name"):
        memory.update("name", user_input)
        return "Got it! Please share your email."

    # Collect Email
    elif not memory.get("email"):
        memory.update("email", user_input)
        return "Which platform do you create content on? (YouTube/Instagram)"

    # Collect Platform + Call Tool
    elif not memory.get("platform"):
        memory.update("platform", user_input)

        mock_lead_capture(
            memory.get("name"),
            memory.get("email"),
            memory.get("platform")
        )

        return "🎉 You're all set! Our team will reach out soon."

    return "How can I help you?"
