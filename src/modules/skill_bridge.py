
def generate_career_roadmap(skills, career_goal, experience_level):
    """Create a general rule-based career roadmap for demo mode."""
    skills = skills.strip()
    career_goal = career_goal.strip()
    experience_level = experience_level.strip()

    if not skills or not career_goal or not experience_level:
        raise ValueError(
            "Skills, career goal, and experience level are required."
        )

    skill_list = [
        item.strip()
        for item in skills.split(",")
        if item.strip()
    ]

    if not skill_list:
        raise ValueError("Please provide at least one skill.")

    return {
        "skills": skill_list,
        "career_goal": career_goal,
        "experience_level": experience_level,
        "roadmap": [
            f"Review the core requirements for {career_goal}.",
            "Choose one relevant skill to improve this week.",
            "Build a small project using your existing skills.",
            "Document the project and ask someone for feedback.",
            "Compare your skills against real job descriptions.",
        ],
    }
