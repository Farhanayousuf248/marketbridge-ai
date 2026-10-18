
def suggest_opportunities(business_need, available_skills):
    """Suggest project ideas based on a business need and skills."""
    business_need = business_need.strip()
    available_skills = available_skills.strip()

    if not business_need or not available_skills:
        raise ValueError(
            "Business need and available skills are required."
        )

    skills = [
        skill.strip()
        for skill in available_skills.split(",")
        if skill.strip()
    ]

    if not skills:
        raise ValueError("Please provide at least one skill.")

    return {
        "business_need": business_need,
        "skills": skills,
        "project_ideas": [
            f"Build a prototype to address: {business_need}",
            f"Use {skills[0]} to create a proof of concept.",
            "Test the idea with sample data and gather feedback.",
        ],
    }
