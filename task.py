## Task definitions for the financial document analyzer
from crewai import Task

from finance_agents import financial_analyst, verifier, investment_advisor, risk_assessor


## Main financial document analysis task
analyze_financial_document = Task(
    description=(
        "Use the following financial document content:\n\n{document_text}\n\n"
        "And the user's query: {query} "
        "to produce a structured, data-driven analysis. "
        "Focus on revenue, profitability, cash flow, balance sheet strength, guidance, and key disclosures."
    ),
    expected_output=(
        "A clear, well-structured analysis that includes:\n"
        "- Summary of the company's recent financial performance\n"
        "- Discussion of growth, margins, cash flow and leverage\n"
        "- Notable management commentary or guidance from the document\n"
        "- Key strengths and weaknesses supported by numbers from the report\n"
        "- Open questions or uncertainties that require further investigation"
    ),
    agent=financial_analyst,
    async_execution=False,
)


## Investment analysis task
investment_analysis = Task(
    description=(
        "Based on the following document content:\n\n{document_text}\n\n"
        "And the financial analysis with the user's query: {query}, "
        "outline possible investment considerations, scenarios, and factors to monitor. "
        "Do not provide personalized financial advice; instead, describe frameworks and trade-offs."
    ),
    expected_output=(
        "A concise set of investment considerations that:\n"
        "- Highlight potential upside and downside drivers\n"
        "- Describe relevant valuation or risk metrics (without fabricating data)\n"
        "- Outline multiple scenarios (bull/base/bear) when appropriate\n"
        "- Emphasize diversification, time horizon, and risk tolerance\n"
        "- Clearly state that this is not personalized financial advice"
    ),
    agent=investment_advisor,
    async_execution=False,
)


## Risk assessment task
risk_assessment = Task(
    description=(
        "Review the following financial document content:\n\n{document_text}\n\n"
        "to identify key risks related to liquidity, leverage, profitability, competitive position, and macro environment. "
        "Explain how these risks might impact the business and investors."
    ),
    expected_output=(
        "A structured risk assessment that:\n"
        "- Lists major risk categories and specific risk factors\n"
        "- Explains why each risk matters and how it could show up in results\n"
        "- Mentions any mitigating factors mentioned in the document\n"
        "- Distinguishes between known risks and areas of uncertainty\n"
        "- Avoids exaggeration while remaining transparent about downside scenarios"
    ),
    agent=risk_assessor,
    async_execution=False,
)


## Verification task
verification = Task(
    description=(
        "Check whether the following uploaded content appears to be a financial or corporate document:\n\n{document_text}\n\n"
        "Identify its main type (e.g., earnings report, 10-Q, investor presentation), "
        "and summarize its structure before detailed analysis."
    ),
    expected_output=(
        "A brief verification summary that:\n"
        "- States whether the document appears financial in nature and why\n"
        "- Identifies the likely type of document (if possible)\n"
        "- Lists the main sections or headings\n"
        "- Notes any limitations or uncertainties in the verification"
    ),
    agent=verifier,
    async_execution=False,
)