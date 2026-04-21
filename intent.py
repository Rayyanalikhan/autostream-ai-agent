def detect_intent(user_input):
    text = user_input.lower()

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in text for x in ["price", "plan", "cost", "features"]):
        return "inquiry"

    elif any(x in text for x in ["buy", "subscribe", "sign up", "try pro", "get started"]):
        return "high_intent"

    return "unknown"
