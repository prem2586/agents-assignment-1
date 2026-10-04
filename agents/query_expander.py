"""
Query Expander Agent

TODO: Implement this agent that transforms a broad research question
into a comprehensive search strategy with sub-questions, keywords,
and search angles.

Hints:
- Define a clear role (e.g., "Research Query Strategist")
- Set a goal focused on breaking down questions and identifying keywords
- Write a backstory that gives the agent expertise in research methodology
- Consider what tools might help (keyword extraction, synonym generation)
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

# TODO: Create the query_expander agent
#
# query_expander = Agent(
#     role="...",
#     goal="...",
#     backstory="...",
#     tools=[],
#     verbose=True,
#     memory=True,
# )

# Placeholder - replace with your implementation
query_expander = Agent(
    role="Search Query Expander",
    goal="Your goal is to understand the query. Break it into multiple sub questions. Identify the keywords for better search. Do not look into the research papers yet.",
    backstory="You are a research analyst specializing in AI agents and "
        "academic literature discovery. You do not answer the research "
        "question yourself. Instead, you analyze the question, identify "
        "its important concepts, and break it into smaller searchable "
        "questions and keywords.",
    tools=[],
    verbose=True,
    memory=True,
)
