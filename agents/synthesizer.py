"""
Synthesizer Agent

TODO: Implement this agent that analyzes collected sources to identify
themes, agreements, contradictions, and gaps in the literature.

Hints:
- Define a role focused on synthesis and analysis
- Set a goal to identify themes, consensus, debates, and gaps
- Write a backstory emphasizing pattern recognition across sources
- This agent primarily reasons - may not need tools
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

# TODO: Create the synthesizer agent
#
# synthesizer = Agent(
#     role="...",
#     goal="...",
#     backstory="...",
#     tools=[],
#     verbose=True,
#     memory=True,
# )

# Placeholder - replace with your implementation
synthesizer = Agent(
    memory=False,
    verbose=True,
    tools=[],
    role="Search results analyzer",
    goal="Analyze the search results from the paper corpus." \
    "Prepare a consice report based on the search results." \
    "Understand the gaps, debates between the research papers results." \
    "Provide a summary of results.",
    backstory="You are a search result analyzer to provide of summary of search results from various research papers" \
    "This results comes from various research papers but provide a consice report to the user." \
    "You never introduce external knowledge, facts, examples, " \
    "statistics, or assumptions that are not present in the " \
    "provided research evidence."
)
