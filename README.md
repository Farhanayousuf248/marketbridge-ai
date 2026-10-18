
# 🌉 MarketBridge AI

### Smarter Marketing. Stronger Skills. Better Opportunities.

**Created & Developed by Farhana Yousuf**  
*AI Agent Developer & Backend Engineer*

MarketBridge AI is a multi-workspace Python application prototype designed to help small businesses explore marketing strategies, help individuals plan career development, and connect business challenges with practical project ideas.

The goal is to bring three useful workspaces together in one simple, accessible application.

---

## ✨ Core Features

### 📈 1. MarketMinds AI — Marketing Workspace

Helps small businesses organize their marketing activities.

- Generate structured marketing recommendations.
- Define target customers and marketing goals.
- Create a sample 3-day content calendar.
- Explore practical actions to improve business visibility.

### 🎯 2. SkillBridge AI — Career Workspace

Helps users explore possible next steps in their career development.

- Enter existing skills.
- Select a career goal and experience level.
- Generate a structured career roadmap.
- Identify practical learning and project-building steps.

### 🤝 3. Opportunity Connector — Business & Skills Matching

Helps connect a business challenge with available skills.

- Describe a business problem or need.
- Enter relevant skills.
- Generate possible project ideas.
- Explore ways to turn an idea into a prototype.

---

## 🛠️ Technology Stack

- **Language:** Python
- **User Interface:** Streamlit
- **Architecture:** Modular Python functions
- **Automated Testing:** Python `unittest`
- **Version Control Ready:** Git

---

## 🚀 Getting Started

### Prerequisites

Install Python on your computer and ensure that Python is available from your terminal.

### Step 1 — Open the project folder

Open the MarketBridge AI project directory in VS Code or a terminal.

### Step 2 — Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3 — Launch the application

```bash
python -m streamlit run app.py
```

### Step 4 — Open the dashboard

Visit this address in your browser:

`http://localhost:8501`

---

## 🧪 Automated Testing

Run the project's automated tests with:

```bash
python -m unittest discover -s tests -v
```

The current test suite checks core module behavior and validation for empty inputs.

**Latest local test result:** 6 tests passed.

---

## 🏗️ Project Structure

```text
MarketBridge AI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── market_minds.py
│   │   ├── skill_bridge.py
│   │   └── opportunity_connector.py
│   └── utils/
│       └── __init__.py
└── tests/
    └── test_business_logic.py
```

---

## ⚠️ Current Project Status

MarketBridge AI is currently a **working rule-based prototype**.

The application uses Python logic to produce structured recommendations. Live AI API integration, persistent user accounts, and production deployment are not currently implemented.

The project can be extended with AI services, secure data storage, user authentication, and additional business intelligence features in future versions.

---

## 🎯 Project Vision

To make useful digital tools more accessible by connecting business challenges, career skills, and practical opportunities through one unified platform.

## 👩‍💻 About the Creator

**Farhana Yousuf**  
AI Agent Developer & Backend Engineer

MarketBridge AI was developed as a project exploring how software can help small businesses organize their marketing, help individuals plan their professional growth, and encourage practical problem-solving.

### Project Goals

- Build a useful and accessible application.
- Demonstrate modular Python development.
- Provide a clean, easy-to-navigate interface.
- Test core functionality with automated tests.
- Create a foundation for future AI-powered features.

---

## 📌 Hackathon Project

**Project:** MarketBridge AI  
**Creator:** Farhana Yousuf  
**Status:** Working prototype — demo mode  
**Focus Areas:** Business Support, Career Development, Skills Matching

*Built to explore practical solutions and create opportunities through technology.*
