
import streamlit as st

from src.modules.market_minds import generate_marketing_plan
from src.modules.skill_bridge import generate_career_roadmap
from src.modules.opportunity_connector import suggest_opportunities

st.set_page_config(
    page_title="MarketBridge AI",
    page_icon="🌉",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffffff 55%, #f3efff 100%);
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #5936a8;
}
[data-testid="stSidebar"] {
    background: #f5f1ff;
}
div.stButton > button {
    background: linear-gradient(90deg, #7048d8, #5085ed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    font-weight: 600;
}
div.stButton > button:hover {
    color: white;
    border: 1px solid #5936a8;
}
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e8e0ff;
    padding: 16px;
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌉 MarketBridge AI")
st.caption("One platform. Smarter marketing. Stronger skills. Better opportunities.")

st.info(
    "DEMO MODE · Results are generated using rule-based Python logic. "
    "Live AI integration is not enabled yet."
)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("AI Workspaces", "03")
with col2:
    st.metric("Core Modules", "03")
with col3:
    st.metric("Mode", "Demo")

st.divider()

section = st.sidebar.radio(
    "YOUR WORKSPACE",
    [
        "Dashboard",
        "MarketMinds AI",
        "SkillBridge AI",
        "Opportunity Connector",
    ],
)

st.sidebar.divider()
st.sidebar.caption("MarketBridge AI · Hackathon Demo")

if section == "Dashboard":
    st.subheader("Welcome to your AI workspace")
    st.write(
        "Explore tools designed to help small businesses grow, "
        "people develop career skills, and teams discover project ideas."
    )

    a, b = st.columns(2)
    with a:
        st.markdown("### 📈 MarketMinds AI")
        st.write("Create marketing plans and a sample content calendar.")
        if st.button("Open Marketing", key="open_marketing"):
            st.session_state["workspace"] = "MarketMinds AI"
            st.rerun()

    with b:
        st.markdown("### 🎯 SkillBridge AI")
        st.write("Turn your current skills into a practical career roadmap.")
        if st.button("Open Career", key="open_career"):
            st.session_state["workspace"] = "SkillBridge AI"
            st.rerun()

    st.markdown("### 🤝 Opportunity Connector")
    st.write("Connect a business need with skills and project ideas.")
    if st.button("Open Opportunities", key="open_opportunities"):
        st.session_state["workspace"] = "Opportunity Connector"
        st.rerun()

    if "workspace" in st.session_state:
        st.info(
            f"Use the sidebar to open {st.session_state['workspace']}."
        )

elif section == "MarketMinds AI":
    st.subheader("📈 MarketMinds AI")
    st.write("Build a simple marketing plan for your business.")

    with st.form("marketing_form"):
        business = st.text_input("Business name or type")
        audience = st.text_input("Target customers")
        goal = st.selectbox(
            "Main marketing goal",
            ["Get more customers", "Increase sales", "Build brand awareness"],
        )
        submitted = st.form_submit_button("Generate Marketing Plan")

    if submitted:
        try:
            result = generate_marketing_plan(business, audience, goal)
            st.success(f"Marketing plan created for {result['business']}")

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### Business overview")
                st.write(f"**Business:** {result['business']}")
                st.write(f"**Audience:** {result['audience']}")
                st.write(f"**Goal:** {result['goal']}")

            with c2:
                st.markdown("#### Recommended actions")
                for action in result["actions"]:
                    st.markdown(f"- {action}")

            st.markdown("#### 3-day content calendar")
            st.table(result["content_calendar"])
        except (ValueError, KeyError, TypeError) as exc:
            st.error(f"Could not create the plan: {exc}")

elif section == "SkillBridge AI":
    st.subheader("🎯 SkillBridge AI")
    st.write("Build a practical roadmap around your career goal.")

    with st.form("career_form"):
        skills = st.text_area(
            "Your current skills",
            placeholder="Python, communication, Excel",
        )
        career = st.selectbox(
            "Career goal",
            ["Software Developer", "Data Analyst", "Digital Marketer", "AI Engineer"],
        )
        experience = st.selectbox(
            "Experience level",
            ["Beginner", "Intermediate", "Experienced"],
        )
        submitted = st.form_submit_button("Create Career Roadmap")

    if submitted:
        try:
            result = generate_career_roadmap(skills, career, experience)
            st.success(f"Roadmap created for {result['career_goal']}")

            c1, c2 = st.columns(2)
            with c1:
                st.markdown("#### Your profile")
                st.write("**Skills:** " + ", ".join(result["skills"]))
                st.write(f"**Career goal:** {result['career_goal']}")
                st.write(f"**Experience:** {result['experience_level']}")

            with c2:
                st.markdown("#### Your next steps")
                for i, step in enumerate(result["roadmap"], start=1):
                    st.markdown(f"{i}. {step}")
        except (ValueError, KeyError, TypeError) as exc:
            st.error(f"Could not create the roadmap: {exc}")

else:
    st.subheader("🤝 Opportunity Connector")
    st.write("Match a business challenge with available skills.")

    with st.form("opportunity_form"):
        need = st.text_area(
            "What does the business need?",
            placeholder="Example: A local shop needs a simple online ordering system.",
        )
        skills = st.text_input(
            "Available skills",
            placeholder="Python, web development, design",
        )
        submitted = st.form_submit_button("Find Project Opportunities")

    if submitted:
        try:
            result = suggest_opportunities(need, skills)
            st.success("Project ideas generated.")

            st.markdown("#### Business challenge")
            st.write(result["business_need"])
            st.markdown("#### Available skills")
            st.write(", ".join(result["skills"]))
            st.markdown("#### Suggested project ideas")

            for i, idea in enumerate(result["project_ideas"], start=1):
                st.markdown(f"**Idea {i}.** {idea}")
        except (ValueError, KeyError, TypeError) as exc:
            st.error(f"Could not generate opportunities: {exc}")

st.divider()
st.caption("MarketBridge AI · Prototype for demonstration and learning")
