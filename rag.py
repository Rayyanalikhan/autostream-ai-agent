import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

def get_answer(query):
    kb = load_knowledge()
    query = query.lower()

    if "basic" in query:
        return f"Basic Plan: {kb['pricing']['basic']}"
    
    if "pro" in query:
        return f"Pro Plan: {kb['pricing']['pro']}"
    
    if "refund" in query:
        return kb["policies"]["refund"]

    if "support" in query:
        return kb["policies"]["support"]

    return "I can help with pricing, features, or policies!"
