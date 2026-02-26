## Agent definitions for the financial document analyzer
from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

# Primary financial analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Carefully analyze the provided financial document and the user's query "
        "to produce clear, well-reasoned investment insights."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with deep knowledge of corporate finance, "
        "equity and debt markets, and risk analysis. "
        "You rely on data from the financial document, avoid speculation, and clearly explain "
        "assumptions, methodologies, and limitations in plain language."
    ),
    llm=llm,  
    max_iter=3,
    max_rpm=3,
    allow_delegation=True,
)

# Document verification agent
verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Verify that the uploaded file is a financial or corporate document and summarize "
        "its main sections and key figures."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You specialize in reviewing financial statements, earnings reports, and similar "
        "documents to confirm their type and extract high-level structure before deeper analysis."
    ),
    llm=llm,  
    max_iter=2,
    max_rpm=2,
    allow_delegation=False,
)

# Investment advice agent
investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal=(
        "Transform the analyst's findings into balanced, risk-aware investment considerations "
        "and questions for further due diligence. Do not give personalized financial advice."
    ),
    verbose=True,
    backstory=(
        "You focus on converting financial analysis into practical, diversified investment "
        "considerations while emphasizing risk tolerance, time horizon, and the need for "
        "professional advice where appropriate."
    ),
    llm=llm,  
    max_iter=2,
    max_rpm=2,
    allow_delegation=False,
)

# Risk assessment agent
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal=(
        "Identify and clearly explain the main financial, operational, and market risks "
        "visible in the document, along with possible mitigants."
    ),
    verbose=True,
    backstory=(
        "You have extensive experience in credit analysis, market risk, and liquidity risk. "
        "You highlight both downside scenarios and uncertainty without exaggeration."
    ),
    llm=llm,   
    max_iter=2,
    max_rpm=2,
    allow_delegation=False,
)