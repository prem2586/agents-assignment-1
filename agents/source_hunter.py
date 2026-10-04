"""
Source Hunter Agent

TODO: Implement this agent that searches the curated paper corpus
to find relevant passages for each sub-question in the query strategy.

Hints:
- This agent MUST use the search_papers tool from tools.paper_rag_tool
- Define a role focused on investigation and source discovery
- Set a goal to find 8-12 relevant passages
- Write a backstory emphasizing thoroughness and not stopping at first results
"""

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools.paper_rag_tool import search_papers

# TODO: Create the source_hunter agent
#
# source_hunter = Agent(
#     role="...",
#     goal="...",
#     backstory="...",
#     tools=[search_papers],  # This tool is required!
#     verbose=True,
#     memory=True,
# )


# Placeholder - replace with your implementation
source_hunter = Agent(
    role="Document Searcher",
    goal="Understand the questions provided. Break the query into chunks." \
    "Search the research papers and provide the relevant answers" \
         "STRICT RULES:\n"
        "1. Every factual claim must come from the retrieved documents.\n"
        "2. Do not use your pretrained/general knowledge.\n"
        "3. Do not infer facts that are not explicitly supported by the documents.\n"
        "4. Do not add examples unless they appear in the documents.\n"
        "5. If the documents do not contain enough information, say "
        "'INSUFFICIENT_DOCUMENT_CONTEXT'.\n"
        "6. Include the source/document for each finding.",
    backstory="You are document searcher who understands the questions and " \
    "find the right answers from the documents provided.",
    tools=[search_papers],
    verbose=True,
    memory=False
)
