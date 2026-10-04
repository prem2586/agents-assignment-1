"""
Task Definitions for Research Crew

TODO: Define the four sequential tasks:
1. Query Expansion - Break down the research question
2. Source Hunting - Search the paper corpus
3. Synthesis - Analyze and synthesize findings
4. Report Writing - Generate the literature review

Each task should:
- Have a clear description telling the agent what to do
- Specify the agent responsible
- Define expected_output format
- Use context parameter to pass information between tasks
"""

from crewai import Task
from agents import query_expander, source_hunter, synthesizer, report_writer
from datetime import datetime
import re




def create_research_tasks(research_question: str) -> list[Task]:
    """
    Create the task pipeline for a research question.

    Args:
        research_question: The user's research question

    Returns:
        List of 4 tasks in execution order

    TODO: Implement the four tasks below
    """
  

    stop_words = {
        "what", "are", "the", "to", "a", "an", "and","give","provide","tell",
        "or", "of", "in", "for", "that", "can", "how", "is"
    }

    # Extract words
    words = re.findall(r'[a-zA-Z0-9]+', research_question.lower())

    # Remove common words
    meaningful_words = [
        word for word in words
        if word not in stop_words
    ]

    # Take first 3 meaningful words
    question_slug = "_".join(meaningful_words[:3])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = f"outputs/report_{question_slug}_{timestamp}.md"

    print(output_file)

  
    # =========================================
    # Task 1: Query Expansion
    # =========================================
    # TODO: Create a task that breaks down the research question
    # into sub-questions, keywords, and search angles
    #
    # expand_task = Task(
    #     description=f"... {research_question} ...",
    #     agent=query_expander,
    #     expected_output="..."
    # )
    expand_task = Task(
        description=f"Analyse the {research_question}. Break it into 3-5 sub questions which will be helpful for searching the research papers." \
        "Provide 2-3 keywords for better search in the research papers. " \
        "Do not search on the research papers yet.",
        agent=query_expander,
        expected_output="Provide results in the below format:" \
        "1. 2-3 sub questions for searching in the research papers." \
        "2. Keywords for the semantic search."
    )
    # =========================================
    # Task 2: Source Hunting
    # =========================================
    # TODO: Create a task that searches the paper corpus
    # Hint: Use context=[expand_task] to pass the query strategy
    #
    # search_task = Task(
    #     description="...",
    #     agent=source_hunter,
    #     context=[expand_task],
    #     expected_output="..."
    # )

    search_task = Task(
        description=f"Search for each sub questions in the paper corpus stored under /data/papers folder." \
            "Provide a relevant answers back. " \
            "Search for keywords using semantic search and consolidate the answers. Do not search beyond the research papers provided under /data/papers folder." \
            "If you don't find the relevant answer, respond saying relevant documents are not available for this query.",
        agent=source_hunter,
        context=[expand_task],
        expected_output="Provide results in the below format:" \
        "1. 4-5 bullet points" \
        "2. References with document name in the bullet format"
    )

    # =========================================
    # Task 3: Synthesis
    # =========================================
    # TODO: Create a task that synthesizes findings into themes
    # Hint: Use context=[expand_task, search_task] for full context
    #
    # synthesis_task = Task(
    #     description="...",
    #     agent=synthesizer,
    #     context=[expand_task, search_task],
    #     expected_output="..."
    # )
    synthesis_task = Task(
        description="Create a report from the search result . Identify the gaps and debates and provide a consice report." \
        "Validate if the results are matching with the papers under /data/papers folder. If it doesn't match send a response no document found for this query.",
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output="Create a summary in 5-10 lines report and provide first 3 references in a bullet points"
     )
    # =========================================
    # Task 4: Report Writing
    # =========================================
    # TODO: Create a task that writes the final literature review
    # Hint: Use context=[expand_task, search_task, synthesis_task]
    #
    report_task = Task(
        description="Create a well defined summary with clear callouts and references",
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        output_file=output_file,
        expected_output="Create a summary output as below:" \
        "The output should be in markdown with sections:" \
            "1. Executive Summary" \
            "2. Introduction" \
            "3. Methodology" \
            "4. Findings (organized by theme)" \
            "5. Discussion" \
            "6. Conclusion" \
            "7. References." 
    )

    

    # TODO: Return your tasks in order
    return [expand_task,search_task,synthesis_task,report_task]

    # Placeholder - replace with your implementation
    raise NotImplementedError(
        "TODO: Implement create_research_tasks() in tasks/task_definitions.py"
    )
