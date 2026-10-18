
def generate_marketing_plan(business, audience, goal):
    """Generate rule-based demo marketing recommendations."""
    business = business.strip()
    audience = audience.strip()
    goal = goal.strip()

    if not business or not audience or not goal:
        raise ValueError("Business, audience, and goal are required.")

    return {
        "business": business,
        "audience": audience,
        "goal": goal,
        "actions": [
            f"Create helpful content for {audience}.",
            f"Explain how {business} can solve a customer problem.",
            "Share a clear offer and contact method.",
            "Review engagement weekly and improve future posts.",
        ],
        "content_calendar": [
            {"day": "Day 1", "content": "Introduce your business"},
            {"day": "Day 2", "content": "Share a useful tip"},
            {"day": "Day 3", "content": "Highlight a product or service"},
        ],
    }
